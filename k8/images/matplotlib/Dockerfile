# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app


RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        ghostscript \
        inkscape \
        && rm -rf /var/lib/apt/lists/*


# Must build from source to be able to run tests
# https://matplotlib.org/3.1.1/devel/testing.html
RUN git clone \
    --branch v3.2.2 \
    --depth 1 \
    git://github.com/matplotlib/matplotlib.git \
    .

COPY matplotlib.setup.cfg .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -v \
    --editable \
    . \
    pytest \
    pytest-custom_exit_code

RUN python -c "import matplotlib"
ENV PYTHON_RECORD_API_FROM_MODULES=matplotlib
CMD [ "pytest", "--verbose", "--suppress-tests-failed-exit-code"  ]