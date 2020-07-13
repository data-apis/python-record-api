# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install numpy

ENV PYTHON_RECORD_API_FROM_MODULES=record_api.sample_usage
CMD [ "python", "-m", "record_api" ]