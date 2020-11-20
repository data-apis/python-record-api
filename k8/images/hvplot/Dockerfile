# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

RUN git clone \
    --branch v0.6.0 \
    --depth 1 \
    https://github.com/holoviz/hvplot.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e .[tests] \
    pytest-custom_exit_code

RUN python -c "import hvplot"

COPY rename_tests.py .
RUN python rename_tests.py

ENV PYTHON_RECORD_API_FROM_MODULES=hvplot
CMD ["pytest", "--verbose", "hvplot/tests/", "--suppress-tests-failed-exit-code"]