"""
Test usage of jsonl writer so we can profile memory consumption
"""

import tempfile
from .jsonl import write

N = 10000 * 1000
print(f"Writing {N} lines to temp file")
with tempfile.NamedTemporaryFile() as fp:
    with write(fp.name) as writer:
        for _ in range(N):
            writer({"hi": "hello"})
