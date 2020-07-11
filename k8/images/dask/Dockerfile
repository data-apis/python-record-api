FROM saulshanabrook/python-record-api:base-1.1.0

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://docs.dask.org/en/latest/develop.html
RUN git clone \
    --branch 2.20.0 \
    --depth 1 \
    git://github.com/dask/dask.git \
    .
ENV SKLEARN_FAIL_NO_OPENMP=true
RUN pip install \
    --no-cache-dir \
    --editable \
    '.[complete]'

RUN python -c "import dask"

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=dask
CMD [ "pytest", "dask", "--verbose", "--doctest-modules" ]