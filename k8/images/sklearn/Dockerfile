# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    cython==0.29.21 \
    pandas==1.0.5 \
    pytest==5.4.3

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://scikit-learn.org/stable/developers/advanced_installation.html#building-from-source
RUN git clone \
    --branch 0.23.1 \
    --depth 1 \
    git://github.com/scikit-learn/scikit-learn.git \
    .
ENV SKLEARN_FAIL_NO_OPENMP=true
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    --no-build-isolation \
    --editable \
    . \
    -v \
    pytest-custom_exit_code

RUN python -c "import sklearn; sklearn.show_versions()"

ENV PYTHON_RECORD_API_FROM_MODULES=sklearn
CMD [ "pytest", "sklearn", "--suppress-tests-failed-exit-code"  ]