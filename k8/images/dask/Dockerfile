# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://docs.dask.org/en/latest/develop.html
RUN git clone \
    --branch 2.20.0 \
    --depth 1 \
    git://github.com/dask/dask.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    --editable \
    '.[complete]' \
    pytest \
    moto

RUN python -c "import dask"

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=dask
CMD [ "pytest", "dask", "--verbose", "--doctest-modules" ]