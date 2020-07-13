# syntax = docker/dockerfile:1.1.7-experimental
ARG FROM
FROM ${FROM}

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        libproj-dev \
        libgeos-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app

# Must build from source to be able to run tests
# http://xarray.pydata.org/en/stable/contributing.html#creating-a-development-environment
RUN git clone \
    --branch v0.15.1 \
    --depth 1 \
    git://github.com/pydata/xarray.git \
    .
# for cartopy
# https://scitools.org.uk/cartopy/docs/latest/installing.html#required-dependencies


# Must install numpy before cartopy
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    numpy

# Manually convered conda -> pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -v \
    black \
    boto3 \
    bottleneck \
    cartopy \
    # cdms2 \
    cfgrib \
    cftime \
    coveralls \
    dask \
    distributed \
    flake8 \
    h5netcdf \
    h5py \
    hypothesis \
    # iris \
    isort==4.3.21 \
    lxml \
    matplotlib \
    mypy==0.780  \
    nc-time-axis \
    netcdf4 \
    numba \
    pandas \
    pint \
    pip \
    pseudonetcdf \
    pydap \
    # pynio \
    pytest \
    pytest-cov \
    pytest-env \
    rasterio \
    scipy \
    seaborn \
    setuptools \
    sparse \
    toolz \
    zarr \
    numbagg \
    pytest-custom_exit_code

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    -v \
    -e \
    .

RUN python -c "import xarray"

ENV PYTHON_RECORD_API_FROM_MODULES=xarray
CMD [ "pytest", "xarray", "--suppress-tests-failed-exit-code" ]