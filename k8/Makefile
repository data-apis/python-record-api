all: images

VERSION := 1.1.0

IMAGES := dask sample-usage skimage sklearn xarray 

all: $(addprefix ../data/api/,$(addsuffix .json,$(IMAGES)))

../data/api/%.json: argo-submit-%
	argo wait record-$(*F)
	argo get record-$(*F) -o json \
		| jq -r '.status.nodes."record-$(*F)".outboundNodes[0]' \
		| xargs -n 1 -I% wget 'http://localhost:2746/artifacts/argo/record-$(*F)/%/api'
	tar -xvf api
	rm api
	mv -f api.json $@

argo-submit-%: image-% argo-workflow-submit
	-argo delete record-$(*F)
	argo submit --from workflowtemplate/python-record-api -p label="$(*F)" -p tag="$(VERSION)" --name 'record-$(*F)' --watch


argo-workflow-submit:
	-argo template delete python-record-api
	argo template create workflow-template.yml


images: $(addprefix image-,$(IMAGES))

image-%: image-record-api
	docker build -t dataapis/python-record-api:$(*F)-$(VERSION) --build-arg label=$(VERSION) ./images/$(*F)


image-record-api:
	docker build -t dataapis/python-record-api:base-$(VERSION) ./images/record-api