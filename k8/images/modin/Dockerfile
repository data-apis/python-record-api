# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://modin.readthedocs.io/en/latest/developer/contributing.html
RUN git clone \
    --branch 0.8.1.1 \
    --depth 1 \
    git://github.com/modin-project/modin.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt \
    pytest-custom_exit_code

RUN python -c "import modin"

ENV PYTHON_RECORD_API_FROM_MODULES=modin
CMD [ "pytest", "modin/pandas/test", "--verbose", "--suppress-tests-failed-exit-code"]
