# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://github.com/facebook/prophet
RUN git clone \
    --branch 0.6 \
    --depth 1 \
    https://github.com/facebook/prophet.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r python/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    pytest \
    numpy \
    pandas \
    convertdate \
    pytest-custom_exit_code

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e python/

RUN cd python \
    python -c "from fbprophet import Prophet"

ENV PYTHON_RECORD_API_FROM_MODULES=fbprophet
CMD ["pytest", "python/fbprophet", "--verbose", "--suppress-tests-failed-exit-code"]
