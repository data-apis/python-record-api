"""
This analysis is meant to run on the raw data and produce a JSON represenation of a minimal
inferred API.
"""
from __future__ import annotations

import collections
import operator
import os
import typing
import warnings
import itertools
import dataclasses
import warnings
import functools
import pathlib
import tqdm.std
import orjson
from typing_extensions import TypedDict
import tqdm
import black

from . import jsonl
from .type_analysis import *
from .apis import *


INPUT = os.environ["PYTHON_RECORD_API_INPUT"]
OUTPUT = os.environ["PYTHON_RECORD_API_OUTPUT"]


def __main__():
    api = API.parse_file(INPUT)

    folder = pathlib.Path(OUTPUT)
    for name, module in tqdm.tqdm(api.modules.items()):
        (folder / f"{name}.py").write_text(
            black.format_str(
                module.source,
                mode=black.FileMode([black.TargetVersion.PY38], is_pyi=False),
            )
        )


if __name__ == "__main__":
    __main__()
