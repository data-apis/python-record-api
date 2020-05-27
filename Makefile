.PHONY: groupby_location clean_groupby_location clean all

LIBRARIES := sample_usage skimage

all: groupby_location

clean: clean_groupby_location

clean_groupby_location:
	rm data/groupby_location/*


groupby_location: $(addprefix data/groupby_location/,$(addsuffix .jsonl,$(LIBRARIES)))


data/groupby_location/%.jsonl: data/raw/%.jsonl
	env PYTHON_RECORD_API_OUTPUT=$@ \
		PYTHON_RECORD_API_INPUT=$< \
		python -m record_api.line_counts



data/raw/skimage.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=skimage \
		pytest --pyargs skimage


data/raw/sample_usage.jsonl:
	env PYTHON_RECORD_API_OUTPUT_FILE=$@ \
		PYTHON_RECORD_API_TO_MODULE=numpy \
		PYTHON_RECORD_API_FROM_MODULE=record_api.sample_usage \
		PYTHON_RECORD_API_IMPORT_MODULES=numpy \
		python -m record_api
