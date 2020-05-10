# Python Record API

This module is mean to help you understand how a Python module is being used by other modules.

Currently there is a `record_api.py` script that logs all function calls to the module of your choice.

This is supported on Python version 3.8.

## Example

First install the local package:

```bash
pip install -e .
# run tests
env PYTEST_DISABLE_PLUGIN_AUTOLOAD=true pytest record_api/test.py
```

To test out a local small usage of NumPy:

```bash
env PYTHON_RECORD_API_OUTPUT_FILE=data/raw/sample_usage.jsonl \
    PYTHON_RECORD_API_TO_MODULE=numpy \
    PYTHON_RECORD_API_FROM_MODULE=record_api.sample_usage \
    PYTHON_RECORD_API_IMPORT_MODULES=numpy \
    python -m record_api

env PYTHON_RECORD_API_INPUT=data/raw/sample_usage.jsonl \
    PYTHON_RECORD_API_OUTPUT_TYPED=data/counts_typed/sample_usage.csv \
    PYTHON_RECORD_API_OUTPUT_UNTYPED=data/counts_untyped/sample_usage.csv \
    python -m record_api.line_counts
```

Here is how I can use it to see all the functions the scikit image tests call in NumPy:

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
pip install altair_data_server

conda uninstall -c conda-forge --force matplotlib scikit-image

# install matplotlib from source so we have tests
# https://matplotlib.org/3.2.1/devel/contributing.html#other-ways-to-contribute
env MPLSETUPCFG=$PWD/matplotlib.setup.cfg pip install matplotlib --no-binary :all:

# TODO: Fix install of pandas and skimage
# Install scikit-image from source so we have tests as well
pip install scikit-image --no-binary :all:

# TODO: trace all of dask
# TODO: add special pandas command
echo "skimage
dask.array
sklearn
matplotlib
xarray
pandas" | xargs -I % \
env PYTHON_RECORD_API_OUTPUT_FILE=data/raw/%.jsonl \
    PYTHON_RECORD_API_TO_MODULE=numpy \
    PYTHON_RECORD_API_FROM_MODULE=% \
    pytest --pyargs %

env PYTHON_RECORD_API_INPUT=data/raw/dask.array.jsonl \
    PYTHON_RECORD_API_OUTPUT_TYPED=data/counts_typed/dask.array.csv \
    PYTHON_RECORD_API_OUTPUT_UNTYPED=data/counts_untyped/dask.array.csv \
    python -m record_api.line_counts
```

## How?

This uses the `sys.settrace` function to trace all the bytecode operations. It also uses
[@crusaderky's helpful gist](https://gist.github.com/crusaderky/cf0575cfeeee8faa1bb1b3480bc4a87a)
to get access to the top of the stack in the settrace function.

It records all usage of the modules you specify, both all functions called that were defined in those modules, and all core operations that use objects defined in those libraries.

## Why?

The goal is to give us a sense of how different APIs are used in Python data science libraries, in order to have some data to back up decisions about creating future APIs.

This let's us understand not only what exact functions are called, but the ways in which they are called, includig the type and values of their arguments.


## Tests

There are some tests in the `record_api_test.py` which you can run with `python -m unittest record_api_test`. Unfortunately, we can't run coverage on our module, because it also uses `sys.settrace`. 