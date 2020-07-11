FROM saulshanabrook/python-record-api:base-1.1.0

RUN pip install numpy

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=record_api.sample_usage
CMD [ "python", "-m", "record_api" ]