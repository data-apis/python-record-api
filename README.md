# Python Record API

![.github/workflows/workflow.yml](https://github.com/data-apis/python-record-api/workflows/.github/workflows/workflow.yml/badge.svg?branch=master)

This module is meant to help you understand how a Python module is being used by other modules. Currently, this logs all function calls from running a module, or when running pytest, from a specified module to another module. Then it builds hypothetical API for the target module, given all the calls it has taken.


*Sample generated function, from [`data/typing/numpy.py`](./data/typing/numpy.py)*

```python
def argmax(
    a: object = ...,
    axis: Union[int, None] = ...,
    out: Union[dask.array.core.Array, int, numpy.ndarray] = ...,
    *,
    keepdims: bool = ...,
):
    """
    usage.dask: 36
    usage.pandas: 23
    usage.scipy: 24
    usage.skimage: 18
    usage.sklearn: 77
    usage.xarray: 17
    """
    ...
```

Contributions are very welcome! Please feel free to open an issue, or reach out directly, if there is anything you would like to discuss or explore! You can also check out the [issue tracker](https://github.com/data-apis/python-record-api/issues) for some possible next steps that we could use help on.


## Usage

```bash
# Supported on Python 3.8
pip install record_api

# First, run some program and gather a trace. Either by:
# a) Running a Python module:
env PYTHON_RECORD_API_OUTPUT_FILE=out.jsonl \
    PYTHON_RECORD_API_TO_MODULES=numpy \
    PYTHON_RECORD_API_FROM_MODULES=record_api.sample_usage \
    python -m record_api
# b) Running pytest, adding tracing around each test:
env PYTHON_RECORD_API_OUTPUT_FILE=out.jsonl \
    PYTHON_RECORD_API_TO_MODULES=numpy \
    PYTHON_RECORD_API_FROM_MODULES=xarray \
    pytest --pyargs xarray

# This gives you a JSONL file with one line per call.
# Next we can groupby function and args and count and count how many
# lines had that call. This reduced the total data size
# to make later processing quicker.
# The assumption here is that the same call with the same types
# from the same line is ignored.
env PYTHON_RECORD_API_OUTPUT=grouped.jsonl \
    PYTHON_RECORD_API_INPUT=out.jsonl \
    python -m record_api.line_counts

# Now we can take the grouped output and create a JSON file with the
# inferred API
# The LABEL is saved to record how many calls to this function happened from that API
env PYTHON_RECORD_API_OUTPUT=xarray-api.json \
    PYTHON_RECORD_API_INPUT=grouped.jsonl \
    PYTHON_RECORD_API_LABEL=xarray \
    PYTHON_RECORD_API_MODULES=numpy \
    python -m record_api.infer_apis

# (optional) Then, if you have produced  multiple apis, from different
# library traces, you can join them
env PYTHON_RECORD_API_OUTPUT=all_api.json \
    PYTHON_RECORD_API_INPUTS=xarray-api.json,pandas-api.json
    python -m record_api.combine_apis

# Finally you can actually generate the mock APIs for the library you were tracing
env PYTHON_RECORD_API_OUTPUT=typing/ \
    PYTHON_RECORD_API_INPUT=all_api.json \
    python -m record_api.write_api
```


## Hosted Usage

We have this repository set up with Kubernetes and Github Actions to automatically analyze a number of libraries. The ones we have added are in [`k8/images`](./k8/images).

Once it's added to the repo, it will be run and the data will be added to `data/api/<library_name>.json` and from there, it will be used to generate the NumPy and Pandas APIs. Those are present in [`data/api.json`](./data/api.json), in machine readable form, as well as in [`data/typing`](data/typing) in human readable form.

### Adding more libraries

Do you have a library that you would also like to see analyzed? We welcome PRs!

You can add a new backend just from the Github editor UX, but you probably want to test it locally first.


First install Docker >= v18.06 and Python.

Then [fork the library](https://github.com/data-apis/python-record-api/fork), clone your fork, and check out a new branch:

```bash
git clone git@github.com:<FORK_NAME>/python-record-api.git
cd python-record-api

git checkout -b <CHANGES_NAME>
```

And install the python package locally:

```bash
pip install flit
flit install
```

Now either:

1. Edit an existing library, by editing a `Dockerfile` in any of the directories in `./k8/images`. If you make any changes, also increment number in the corresponding `version` file.
2. Add a new library, by creating a new directory with the name of the module in the `./k8/images` directory. The name cannot contain any underscores. It should have at least a `Dockerfile` and a `versions` file, with the contents of `0`. You should copy an existing `Dockerfile` and modify it to download some downstream library and run some command as the entrypoint which produces a trace.
3. Add a new module to trace calls against, by modifying the `TO_MODULES` constant in `./k8/Makefile` to add another Python module and also incrementing the `./k8/argo/version` file.

Then you can test an image locally, to make sure the Dockerfile builds correctly and the tracing works:

```bash
cd k8
make test-local-<LIBRARY NAME>

# to test against the local python package, instead of the released one
make PYTHON_PACKAGE=. test-local-<LIBRARY NAME>
```

This should output a number of lines of traces.

Now, commit your changes, push your branch, and open a PR. This will then build the image in CI and attempt to kick off build of it.

Once the PR is merged, every time we update the core library, this tracing will be re-run and the updated data will be added to the repo.


## Development

First install the local package:

```bash
flit install --symlink
# run the tests
env PYTEST_DISABLE_PLUGIN_AUTOLOAD=true pytest record_api/test.py
```

Now run the traces and build the results:

```bash
make
```

You can look in `data/typing/` for the final results of the generated API.

## How?

This uses the `sys.settrace` function to trace all the bytecode operations. It also uses
[@crusaderky's helpful gist](https://gist.github.com/crusaderky/cf0575cfeeee8faa1bb1b3480bc4a87a)
to get access to the top of the stack in the settrace function.

It records all usage of the modules you specify, both all functions called that were defined in those modules, and all core operations that use objects defined in those libraries.

## Limitations

It doesn't currently track return values, so we don't know if someone called something whether it was actually a proper call or not.
We just assume it is.

Also it doesn't currently record calls from Cython compiled code. This could be added later possibly by plugging into lldb.

## Why?

The goal is to give us a sense of how different APIs are used in Python data science libraries, in order to have some data to back up decisions about creating future APIs.

This lets us understand not only what exact functions are called, but the ways in which they are called, including the type and values of their arguments.

## Relationship to MonkeyType

The most similar existing tool, is probably the [MonkeyType](https://github.com/Instagram/MonkeyType) library, created by Instagram, to generate type definitions from usage of Python code. However, they do not stop at every bytecode execution, instead only tracing function calls, leaving out some of the dunder methods. It would likely be useful to explore at some point how the functionality we needed could be added to that existing library.


## Tests

There are some tests in the `record_api_test.py` which you can run with `python -m unittest record_api_test`. Unfortunately, we can't run coverage on our module, because it also uses `sys.settrace`.
