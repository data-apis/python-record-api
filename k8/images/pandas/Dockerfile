FROM saulshanabrook/python-record-api:base-1.1.0

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://pandas.pydata.org/pandas-docs/stable/development/contributing.html#creating-a-development-environment
RUN git clone \
    --branch v0.15.1 \
    --depth 1 \
    git://github.com/pandas-dev/pandas.git \
    .

RUN pip install \
    --no-cache-dir \
     -r requirements-dev.txt


RUN python setup.py build_ext --inplace -j 4
RUN pip install \
    -e . \
    --no-build-isolation \
    --no-use-pep517 \
    --no-cache-dir

RUN python -c "import pandas"

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=sklearn
CMD [ "pytest", "pandas", "--skip-slow", "--skip-network", "--skip-db", "-m", "'not single'", "-r", "sxX", "--strict" ]
