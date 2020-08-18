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
    --branch v1.1.0 \
    --depth 1 \
    git://github.com/pandas-dev/pandas.git \
    .


# Don't install all depenedencies, so we only run tests
# that use these!
# Otherwise tests run out of memory
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    pytest \
    hypothesis \
    setuptools \
    numpy \
    python-dateutil \
    pytz \
    cython \
    pytest-custom_exit_code


RUN python setup.py build_ext --inplace -j 4
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -e . \
    --no-build-isolation \
    --no-use-pep517

RUN python -c "import pandas"


ENV PYTHON_RECORD_API_FROM_MODULES=pandas
CMD [ "pytest", "pandas", "-m", "not slow and not network and not clipboard", "--strict", "--suppress-tests-failed-exit-code"  ]
