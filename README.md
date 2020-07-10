# Python Record API

This module is mean to help you understand how a Python module is being used by other modules.

Currently, this logs all function calls from running a module, or when running pytest, from a specified module to another module.

Then it builds hypothetical API for the target module, given all the calls it has taken.

This is supported on Python version 3.8.


## Usage

```bash
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


## Development

First install the local package:

```bash
pip install -e .
# run the tests
env PYTEST_DISABLE_PLUGIN_AUTOLOAD=true pytest record_api/test.py
```

Now run the traces and build the results:

```bash
make
```

You can look in `data/typing/` for the final results of the generated API.

Here are some notes on getting set up locally with a few projects. However,
I had to disregard these and git clone things for some of them to get the tests to run:

```bash
git clone git@github.com:scikit-image/scikit-image.git
conda create -n python-record-api -c conda-forge \
    jupyterlab \
    scikit-image \
    dask \
    scipy \
    scikit-learn \
    xarray \
    altair \
    pandas \
    swifter \
    cython \
    pytest \
    hypothesis \
    python=3.8

conda activate python-record-api
pip install -e .
pip install altair_data_server

conda uninstall -c conda-forge --force matplotlib scikit-image

# install matplotlib from source so we have tests
# https://matplotlib.org/3.2.1/devel/contributing.html#other-ways-to-contribute
env MPLSETUPCFG=$PWD/matplotlib.setup.cfg pip install matplotlib --no-binary :all:

# TODO: Fix install of pandas and skimage
# Install scikit-image from source so we have tests as well
pip install scikit-image --no-binary :all:

make
```

## How?

This uses the `sys.settrace` function to trace all the bytecode operations. It also uses
[@crusaderky's helpful gist](https://gist.github.com/crusaderky/cf0575cfeeee8faa1bb1b3480bc4a87a)
to get access to the top of the stack in the settrace function.

It records all usage of the modules you specify, both all functions called that were defined in those modules, and all core operations that use objects defined in those libraries.

## Limitations

It doesn't currently track return values, so we don't know if someone called something whether it was actually a proper cal or not.
We just assume it is.

Also it doesn't currently record calls from Cython compiled code. This could be added later possibly by plugging into lldb.

## Why?

The goal is to give us a sense of how different APIs are used in Python data science libraries, in order to have some data to back up decisions about creating future APIs.

This let's us understand not only what exact functions are called, but the ways in which they are called, includig the type and values of their arguments.

## Tests

There are some tests in the `record_api_test.py` which you can run with `python -m unittest record_api_test`. Unfortunately, we can't run coverage on our module, because it also uses `sys.settrace`.
