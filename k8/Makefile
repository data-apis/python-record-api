all: images

VERSION := 1.1.0

IMAGES := dask pandas sample-usage skimage sklearn xarray 

all: $(addprefix ../data/api/,$(addsuffix .json,$(IMAGES)))

../data/api/%.json:
	argo wait record-$(*F)
	argo get record-$(*F) -o json \
		| jq -r '.status.nodes."record-$(*F)".outboundNodes[0]' \
		| xargs -n 1 -I% wget 'http://localhost:2746/artifacts/argo/record-$(*F)/%/api'
	tar -xvf api
	rm api
	mv -f api.json $@


argo-submit: $(addprefix argo-submit-,$(IMAGES))

argo-submit-%:
	-argo delete record-$(*F)
	-argo wait record-$(*F)
	argo submit --from workflowtemplate/python-record-api -p label="$(*F)" -p tag="$(VERSION)" --name 'record-$(*F)'


argo-workflow-submit:
	-argo template delete python-record-api
	argo template create workflow-template.yml


push-images:  $(addprefix push-image-,$(IMAGES))

push-image-%:
	docker push saulshanabrook/python-record-api:$(*F)-$(VERSION)

build-images:
	docker buildx bake

port-forward:
	kubectl -n argo port-forward deployment/argo-server 2746:2746

set-namespace:
	kubectl config set-context --current --namespace=argo