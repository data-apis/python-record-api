ARG label
FROM dataapis/python-record-api:base-$label

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# http://xarray.pydata.org/en/stable/contributing.html#creating-a-development-environment
RUN git clone \
    --branch v0.15.1 \
    --depth 1 \
    git://github.com/pydata/xarray.git \
    .
# TODO: Manually version?
# for cartopy
# https://scitools.org.uk/cartopy/docs/latest/installing.html#required-dependencies
RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    # https://proj.org/install.html#debian
        proj-bin \
        libgeos-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Manually convered conda -> pip
RUN pip install \
    --no-cache-dir \
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
    hdf5 \
    hypothesis \
    iris \
    isort==4.3.21 \
    lxml \
    matplotlib \
    mypy==0.780  \
    nc-time-axis \
    netcdf4 \
    numba \
    numpy \
    pandas \
    pint \
    pip \
    pseudonetcdf \
    pydap \
    pynio \
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
    numbagg

RUN pip install \
    --no-cache-dir \
    -e \
    .

RUN python -c "import xarray"

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=sklearn
CMD [ "pytest", "xarray" ]