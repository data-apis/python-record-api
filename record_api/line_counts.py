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
    calls: typing.List[typing.Tuple[dict, typing.Set[str]]] = []
    with jsonl.read(INPUT) as f:
        for row in f:
            location = row.pop("location")
            for row_, locations in calls:
                if row_ == row:
                    locations.add(location)
                    break
            else:
                calls.append((row, {location}))

    with jsonl.write(OUTPUT) as write:
        for row_, locations in tqdm.tqdm(calls, "writing"):
            row_["n"] = len(locations)
            write(row_)


if __name__ == "__main__":
    __main__()
