# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}


RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        libsnappy-dev \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app


# Must build from source to be able to run tests
# https://pandas.pydata.org/pandas-docs/stable/development/contributing.html#creating-a-development-environment
RUN git clone \
    --branch v1.0.5 \
    --depth 1 \
    git://github.com/pandas-dev/pandas.git \
    .


RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -v \
     -r requirements-dev.txt \
     pytest-custom_exit_code


RUN python setup.py build_ext --inplace -j 4
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -v \
    -e . \
    --no-build-isolation \
    --no-use-pep517

RUN python -c "import pandas"


ENV PYTHON_RECORD_API_FROM_MODULES=pandas
CMD [ "pytest", "pandas", "--skip-slow", "--skip-network", "--skip-db", "-m", "'not single'", "-r", "sxX", "--strict", "--suppress-tests-failed-exit-code"  ]
