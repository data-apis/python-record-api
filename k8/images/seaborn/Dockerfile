# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://github.com/mwaskom/seaborn#testing
RUN git clone \
    --branch v0.11.0 \
    --depth 1 \
    https://github.com/mwaskom/seaborn \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt \
    pip install -r ci/utils.txt \
    pytest-custom_exit_code

RUN python -c "import seaborn"

ENV PYTHON_RECORD_API_FROM_MODULES=seaborn
CMD [ "pytest", "seaborn", "-n", "auto", "--doctest-modules", "--cov=seaborn", "--cov-config=.coveragerc", "--verbose", "--suppress-tests-failed-exit-code"]
