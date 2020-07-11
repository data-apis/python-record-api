FROM saulshanabrook/python-record-api:base-1.1.0

WORKDIR /usr/src/app

# Must build from source to be able to run tests
# https://scikit-image.org/docs/stable/contribute.html
RUN git clone \
    --branch v0.17.2  \
    --depth 1 \
    git://github.com/scikit-image/scikit-image.git \
    .

RUN ls requirements/ \
    | grep .txt \
    | xargs -n 1 -I% pip install --no-cache-dir -r requirements/%

RUN pip install \
    --no-cache-dir \
    -e \
    .

RUN python -c "import skimage"

ENV PYTHON_RECORD_API_TO_MODULES=numpy
ENV PYTHON_RECORD_API_FROM_MODULES=skimage
CMD [ "pytest", "skimage", "--doctest-modules" ]