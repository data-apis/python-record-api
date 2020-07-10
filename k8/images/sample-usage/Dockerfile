ARG label
FROM dataapis/python-record-api:base-$label

RUN pip install numpy

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=record_api.sample_usage
CMD [ "python", "-m", "record_api" ]