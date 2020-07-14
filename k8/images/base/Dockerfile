# syntax = docker/dockerfile:1.1.7-experimental
FROM python:3.8.4

ARG PYTHON_PACKAGE_VERSION

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install record_api==${PYTHON_PACKAGE_VERSION}

