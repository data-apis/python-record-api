# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://www.statsmodels.org/stable/dev/test_notes
RUN git clone \
    --branch v0.12.1 \
    --depth 1 \
    https://github.com/statsmodels/statsmodels \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install pytest \
    pytest-custom_exit_code

RUN python -c "import statsmodels"

ENV PYTHON_RECORD_API_FROM_MODULES=statsmodels
CMD [ "pytest", "statsmodels", "--verbose", "--suppress-tests-failed-exit-code"]
