# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://scikit-image.org/docs/stable/contribute.html
RUN git clone \
    --branch v0.17.2  \
    --depth 1 \
    git://github.com/scikit-image/scikit-image.git \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    ls requirements/ \
    | grep .txt \
    | xargs -n 1 -I% pip install -v -r requirements/%

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -e \
    . \
    -v \
    pytest-custom_exit_code

RUN python -c "import skimage"


ENV PYTHON_RECORD_API_FROM_MODULES=skimage
CMD [ "pytest", "skimage", "--doctest-modules", "--suppress-tests-failed-exit-code"  ]