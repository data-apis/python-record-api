# syntax = docker/dockerfile:1.1.7-experimental
FROM python:3.8.4

ARG PYTHON_PACKAGE

WORKDIR /usr/src/base

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install ${PYTHON_PACKAGE}

