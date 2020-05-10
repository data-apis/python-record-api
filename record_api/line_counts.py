"""
Aggregate outputs by line count.
"""
from __future__ import annotations

import collections
import csv
import dataclasses
import json
import os
import re
import typing
import operator

import tqdm

INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT_TYPED = os.environ["PYTHON_RECORD_API_OUTPUT_TYPED"]
OUTPUT_UNTYPED = os.environ["PYTHON_RECORD_API_OUTPUT_UNTYPED"]


def __main__():
    print(f"Aggregating by line number: {INPUT}")
    # mapping of str representations to locations
    untyped_lines = collections.defaultdict(set)
    typed_lines = collections.defaultdict(set)
    with open(INPUT, "r", encoding="utf-8") as f:
        for line in tqdm.tqdm(f, "reading"):
            row = json.loads(line)
            untyped_result = pretty_print_untyped(row)
            location = row["location"]
            if untyped_result:
                untyped_lines[untyped_result].add(location)
            typed_lines[pretty_print(row)].add(location)
            res = f.readline()

    with open(OUTPUT_UNTYPED, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["function", "count"])
        for name, lines in tqdm.tqdm(untyped_lines.items(), "writing untyped"):
            writer.writerow([name, len(lines)])

    with open(OUTPUT_TYPED, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["function", "count"])
        for name, lines in tqdm.tqdm(typed_lines.items(), "writing typed"):
            writer.writerow([name, len(lines)])



def pretty_print_untyped(row):
    f = row["function"]
    p = row["params"]
    if f == "builtins.getattr":
        return f"{t(p['0'])}.{p['1']}"
    if f == "builtins.setattr":
        return f"{t(p['obj'])}.{p['name']} ="
    elif f.startswith("_operator"):
        return None
    return str(f)


def pretty_print(row):
    """
    Pretty prints a row. Function call is like:
        
        fn_name(FirstArgType, SecondArgType, kw=KwArgType)
    
    getattr is
    
        Type.attr
    
    getitem is
        
        ObjectType[IndexType]
    
    setitem is
        
        ObjectType[IndexType] = ValueType
    
    binary ops are
    
        LeftType * RightType
        etc..
    
    iter is
    
        *Type
    
    inplace binary ops are
    
        Type += OtherType
        etc
    
    setatr is
        
        Type.atrr = AssignType
    """
    f = row["function"]
    p = row["params"]
    if f == "builtins.getattr":
        return f"{t(p['0'])}.{p['1']}"
    if f == "builtins.setattr":
        return f"{t(p['obj'])}.{p['name']} = {t(p['value'])}"
    if f == "builtins.iter":
        return f"*{t(p['0'])}"
    elif f.startswith("_operator"):
        op = getattr(operator, f[len("_operator.") :])
        # special case cotains b/c we ordered wrong
        format_str = (
            get_operator_format(op) if op is not operator.contains else "a in b"
        )
        for arg, val in p.items():
            format_str = format_str.replace(arg, str(t(val)))
        return format_str
    args = {}
    kwargs = {}
    for key, value in p.items():
        try:
            idx = int(key)
        except ValueError:
            kwargs[key] = t(value)
        else:
            args[idx] = t(value)
    return f"""{f}({', '.join(
        [str(args[i]) for i in range(len(args))] +
        [f'{key}={kwargs[key]}' for key in sorted(kwargs.keys())])
    })"""


reg = re.compile(r"Same\ as\ ([^.(]+)")


def get_operator_format(o):
    return reg.match(o.__doc__)[1]


@dataclasses.dataclass(frozen=True)
class GenericType:
    name: str
    args: typing.Tuple[typing.Union[str, GenericType, UnionType], ...]

    def __str__(self):
        return f"{self.name}[{', '.join(map(str, self.args))}]"

    def __repr__(self):
        return str(self)


@dataclasses.dataclass(frozen=True)
class UnionType:
    args: typing.Tuple[typing.Union[str, GenericType], ...]

    def __str__(self):
        return f"Union[{', '.join(sorted(map(str, self.args)))}]"

    def __repr__(self):
        return str(self)


def unify(types):
    types = set(types)
    if len(types) == 1:
        return types.pop()
    if not types:
        return "object"
    # mapping of generic type name and n args to args
    generic_types = collections.defaultdict(set)
    regular_types = []
    while types:
        t = types.pop()
        if isinstance(t, GenericType):
            generic_types[(t.name, len(t.args))].add(t.args)
        elif isinstance(t, UnionType):
            types.update(t.args)
        else:
            regular_types.append(t)

    for keys, args in generic_types.items():
        regular_types.append(GenericType(keys[0], tuple(map(unify, zip(*args)))))

    if len(regular_types) == 1:
        return regular_types[0]
    return UnionType(tuple(regular_types))


def t(v):
    """
    Pretty print type of value
    """
    if isinstance(v, dict):
        tp = v["t"]
        if tp == "tuple" and v["v"]:
            return GenericType("tuple", tuple(map(t, v["v"])))
        if tp == "builtins.module":
            return v["v"]
        if tp == "builtins.type":
            return GenericType("Type", (v["v"],))
        if tp == 'builtins.slice':
            return GenericType("slice", tuple(map(t, v["v"])))
        return tp
    if isinstance(v, list) and v:
        return GenericType("list", (unify(map(t, v)),))
    return type(v).__name__

__main__()
