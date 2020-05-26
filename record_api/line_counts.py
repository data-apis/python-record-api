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

from .type_analysis import *

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
        return f"{create_type(p['0'])}.{p['1']}"
    if f == "builtins.setattr":
        return f"{create_type(p['obj'])}.{p['name']} ="
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
        return f"{create_type(p['0'])}.{p['1']}"
    if f == "builtins.setattr":
        return f"{create_type(p['obj'])}.{p['name']} = {create_type(p['value'])}"
    if f == "builtins.iter":
        return f"*{create_type(p['0'])}"
    elif f.startswith("_operator"):
        op = getattr(operator, f[len("_operator.") :])
        # special case cotains b/c we ordered wrong
        format_str = (
            get_operator_format(op) if op is not operator.contains else "a in b"
        )
        for arg, val in p.items():
            format_str = format_str.replace(arg, str(create_type(val)))
        return format_str
    args, kwargs = from_params(p)
    return f"""{f}({', '.join(
        list(map(str, args)) +
        [f'{key}={kwargs[key]}' for key in sorted(kwargs.keys())])
    })"""


reg = re.compile(r"Same\ as\ ([^.(]+)")


def get_operator_format(o):
    return reg.match(o.__doc__)[1]


if __name__ == '__main__':
    __main__()
