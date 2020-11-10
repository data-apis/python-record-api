# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

WORKDIR /usr/src/app

RUN apt-get install libgeos-dev

# Must build from source to be able to run tests
# https://github.com/geopandas/geopandas
RUN git clone \
    --branch v0.8.1 \
    --depth 1 \
    https://github.com/geopandas/geopandas \
    .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    cython \
    fiona \
    pyproj \
    geos \
    pytest \
    pytest-cov \
    pytest-xdist \
    fsspec \
    SQLalchemy \
    pyarrow \
    geopy \
    mapclassify>=2.2.0 \
    pandas \
    matplotlib \
    shapely \
    pygeos \
    pytest-custom_exit_code

RUN python -c "import geopandas"

ENV PYTHON_RECORD_API_FROM_MODULES=seaborn
CMD [ "pytest", "geopandas", "--verbose", "--suppress-tests-failed-exit-code"]
