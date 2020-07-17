# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# https://scipy.github.io/devdocs/building/linux.html#debian-ubuntu
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        gcc gfortran python-dev libopenblas-dev liblapack-dev pybind11-dev \
    && apt-get clean

# https://scipy.github.io/devdocs/dev/contributor/development_workflow.html
RUN git clone \
    --branch v1.5.1 \
    --depth 1 \
    git://github.com/scipy/scipy.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install pytest-custom_exit_code cython numpy pytest

RUN --mount=type=cache,target=/root/.cache/pip \
    python setup.py build_ext --inplace

RUN python -c "import scipy"
RUN python runtests.py --build-only
ENV PYTHON_RECORD_API_FROM_MODULES=scipy
CMD python runtests.py -v -- --suppress-tests-failed-exit-code