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
        libgdal1-dev \
    && apt-get clean

RUN --mount=type=cache,target=/root/.cache/pip \
    ls requirements/ \
    | grep .txt \
    | xargs -n 1 -I% pip install -r requirements/%

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -e . \
    pytest-custom_exit_code

RUN python -c "import networkx"
ENV PYTHONPATH=.
ENV PYTHON_RECORD_API_FROM_MODULES=networkx
CMD pytest networkx --suppress-tests-failed-exit-code
