.PHONY: groupby_location clean_groupby_location clean_api clean_raw clean_typing clean all

LIBRARIES := sample_usage skimage xarray sklearn

all: data/typing/numpy.py

clean: clean_groupby_location clean_api clean_typing clean_raw

clean_typing:
	rm -f data/typing/*


data/typing/numpy.py: data/api.json
	env PYTHON_RECORD_API_OUTPUT=data/typing \
		PYTHON_RECORD_API_INPUT="$^"\
		python -m record_api.write_api

clean_api:
	rm -f data/api.json data/api/*


data/api.json: $(addprefix data/api/,$(addsuffix .json,$(LIBRARIES)))
	env PYTHON_RECORD_API_OUTPUT=$@ \
		PYTHON_RECORD_API_INPUTS="$^"\
		python -m record_api.combine_apis


data/api/%.json: data/groupby_location/%.jsonl
	env PYTHON_RECORD_API_OUTPUT=$@ \
		PYTHON_RECORD_API_INPUT=$< \
		PYTHON_RECORD_API_LABEL=$(*F) \
		python -m record_api.infer_apis


clean_groupby_location:
	rm -f data/groupby_location/*


groupby_location: $(addprefix data/groupby_location/,$(addsuffix .jsonl,$(LIBRARIES)))


data/groupby_location/%.jsonl: | data/raw/%.jsonl
	env PYTHON_RECORD_API_OUTPUT=$@ \
		PYTHON_RECORD_API_INPUT=$| \
		python -m record_api.line_counts


clean_raw:
	rm -f data/raw/*


data/raw/skimage.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=skimage \
		pytest --pyargs skimage



data/raw/sklearn.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=sklearn \
		pytest --pyargs sklearn


data/raw/xarray.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=xarray \
		pytest --pyargs xarray


data/raw/sample_usage.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=record_api.sample_usage \
		PYTHON_RECORD_API_IMPORT_MODULES=numpy \
		python -m record_api
