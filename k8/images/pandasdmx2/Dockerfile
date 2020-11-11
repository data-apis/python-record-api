# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Instructions taken from:
# https://github.com/dr-leo/pandaSDMX/blob/master/.travis.yml
RUN git clone \
    --branch 1.0.0 \
    --depth 1 \
    https://github.com/dr-leo/pandaSDMX.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt \
    pip install . \
    pytest-custom_exit_code

RUN python -c "import pandasdmx"

ENV PYTHON_RECORD_API_FROM_MODULES=pandasdmx
CMD [ "pytest", "-ra", "-m \"not experimental\"", "--verbose", "--suppress-tests-failed-exit-code"]
