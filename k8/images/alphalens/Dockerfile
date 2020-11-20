# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

RUN git clone \
    --branch v0.4.0 \
    --depth 1 \
    https://github.com/quantopian/alphalens.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e .[test] \
    pytest-custom_exit_code \
    pytest

RUN python -c "import alphalens"

ENV PYTHON_RECORD_API_FROM_MODULES=alphalens
CMD ["pytest", "--verbose", "alphalens/tests/", "--suppress-tests-failed-exit-code"]
