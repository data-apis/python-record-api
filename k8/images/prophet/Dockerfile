# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://github.com/facebook/prophet
RUN git clone \
    --branch v0.6 \
    --depth 1 \
    https://github.com/facebook/prophet.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r python/requirements.txt \
    pip install pytest \
    python setup.py develop \
    pytest-custom_exit_code

RUN python -c "import fbprophet"

ENV PYTHON_RECORD_API_FROM_MODULES=seaborn
CMD [ "pytest", "fbprophet", "--verbose", "--suppress-tests-failed-exit-code"]
