"""
Aggregate outputs by line count.
"""
from __future__ import annotations

import collections
import csv
import dataclasses
import json
import re
import typing
import operator
import os

import tqdm
import orjson

from . import jsonl

INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT = os.environ["PYTHON_RECORD_API_OUTPUT"]


def __main__():

    # Conceptual mapping of {function, params} to set of locations
    calls: typing.DefaultDict[bytes, typing.Set[str]] = collections.defaultdict(set)
    with jsonl.read(INPUT) as f:
        for row in f:
            location = row.pop("location")
            # Dump so we can hash
            calls[orjson.dumps(row, option=orjson.OPT_SORT_KEYS)].add(location)

    with jsonl.write(OUTPUT) as write:
        for row_bytes, locations in tqdm.tqdm(calls.items(), "writing"):
            row_ = orjson.loads(row_bytes)
            row_["n"] = len(locations)
            write(row_)


if __name__ == "__main__":
    __main__()
