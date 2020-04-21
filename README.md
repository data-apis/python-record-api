# Python Record API

This module is mean to help you understand how a Python module is being used by other modules.

Currently there is a `record_api.py` script that logs all function calls to the module of your choice.

This is supported on Python version 3.8.

## Example

To test out a local small usage of NumPy:

```bash
env PYTHON_API_OUTPUT_FILE=use_numpy_api.jsonl PYTHON_API_RUN_MODULE=use_numpy_api PYTHON_API_TRACE_MODULE=numpy PYTHON_API_IMPORT_MODULES=numpy python -m cProfile -o out.prof record_api.py
```

Here is how I can use it to see all the functions the scikit image tests call in NumPy:

```bash
git clone git@github.com:scikit-image/scikit-image.git
conda create -c conda-forge -n scikit-image "numpy!=1.18.0" scipy "matplotlib!=3.0.0" networkx pillow=6 imageio tifffile PyWavelets pooch Cython wheel pytest
conda activate scikit-image
pip install -e ./scikit-image pytest-localserver
env PYTHON_API_OUTPUT_FILE=sckimage.jsonl \
    PYTHON_API_RUN_MODULE=pytest \
    PYTHON_API_TRACE_MODULE=numpy \
    PYTHON_API_IMPORT_MODULES=pytest,skimage,networkx,matplotlib,Cython,pooch \
    python record_api.py ./scikit-image/
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