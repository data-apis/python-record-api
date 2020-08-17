# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

# https://networkx.github.io/documentation/latest/developer/contribute.html
RUN git clone \
    --branch networkx-2.4 \
    --depth 1 \
    git://github.com/networkx/networkx.git \
    .

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        graphviz libgraphviz-dev \
        libxml2-dev libxslt-dev \
    && apt-get clean

# Skip gdal  https://github.com/networkx/networkx/issues/3786
RUN --mount=type=cache,target=/root/.cache/pip \
    bash -c 'env CPLUS_INCLUDE_PATH=/usr/include/gdal C_INCLUDE_PATH=/usr/include/gdal \
        pip install \
        -r requirements/default.txt \
        -r requirements/test.txt \
        pygraphviz \
        pydot \
        numpy \
        pandas \
        lxml \
        pyyaml \
        scipy \
        pytest-custom_exit_code \
        -e .'

RUN python -c "import networkx"
ENV PYTHONPATH=.
ENV PYTHON_RECORD_API_FROM_MODULES=networkx
CMD pytest networkx --suppress-tests-failed-exit-code
