# Running the record api tooling on notebooks

First of all, clone the record api repo

```
git clone https://github.com/data-apis/python-record-api.git
```

And create a new conda env for installing all the notebook's dependencies and the record api tooling.

```
conda create -n record-api python=3.8
conda activate record-api
cd python-record-api
pip install record_api
```

We have an example of a notebook under `/notebooks/data`, so we need to transform it
to a python file so the record api tooling work.

```
cd notebooks
python notebook_to_python.py data
```

A new folder named `scripts` under the `notebooks` directory will be created with
all the files converted into python files.

Then, run the file `run_record_api.sh` to generate the inferred API calls in each notebook.
The output will be under `infer_apis` directory as a json per notebook file.
