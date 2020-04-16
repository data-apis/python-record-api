# Python Record API

This module is mean to help you understand how a Python module is being used by other modules.

Currently there is a `record_api.py` script that logs all function calls to the module of your choice.


## Example


To test out a local small usage of NumPy:

```bash
env PYTHON_API_OUTPUT_FILE=use_numpy_api.jsonl PYTHON_API_RUN_MODULE=use_numpy_api PYTHON_API_TRACE_MODULE=numpy PYTHON_API_IMPORT_MODULES=numpy python record_api.py
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
    PYTHON_API_IMPORT_MODULES=numpy,pytest \
    python record_api.py ./scikit-image/
```

## Documentation

