import subprocess
import dataclasses
import contextlib
import orjson
import tqdm
import typing
import io
import warnings


__all__ = ["read", "write"]


@contextlib.contextmanager
def read(path: str) -> typing.Iterator[typing.Iterable[dict]]:

    print("Counting lines...")

    n = lines_in_file(path)

    file = io.FileIO(path, "r")
    buffer = io.BufferedReader(file)
    stream = io.TextIOWrapper(buffer)  # type: ignore
    yield read_lines(path, n, stream)
    stream.close()
    buffer.close()
    file.close()


def read_lines(path, n: int, stream: io.TextIOWrapper) -> typing.Iterable[dict]:
    for _ in tqdm.trange(n, desc=f"reading {path}"):
        line = stream.readline()
        try:
            yield orjson.loads(line)
        except orjson.JSONDecodeError:
            warnings.warn(f"Could not decode line:\n{line}")


@contextlib.contextmanager
def write(path: str, **kwargs) -> typing.Iterator[typing.Callable[[dict], None]]:
    file = io.FileIO(path, "w")
    buffer = io.BufferedWriter(file)

    def write_line(o: dict, buffer=buffer) -> None:
        buffer.write(orjson.dumps(o, **kwargs))
        buffer.write(b"\n")

    yield write_line
    buffer.close()
    file.close()


def lines_in_file(filename: str) -> int:
    """
    https://gist.github.com/zed/0ac760859e614cd03652#file-gistfile1-py-L41
    """
    out = subprocess.Popen(
        ["wc", "-l", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ).communicate()[0]
    return int(out.lstrip().partition(b" ")[0])
