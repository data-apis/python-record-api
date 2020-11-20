# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Instructions taken from:
# https://github.com/ericmjl/pyjanitor.git
RUN git clone \
    --branch v0.18.1 \
    --depth 1 \
    https://github.com/ericmjl/pyjanitor.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e .[all]

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    unyt \
    hypothesis \
    pytest-cov \
    pytest-custom_exit_code

RUN python -c "import janitor"

ENV PYTHON_RECORD_API_FROM_MODULES=janitor
CMD [ "pytest", "--verbose", "--suppress-tests-failed-exit-code"]
