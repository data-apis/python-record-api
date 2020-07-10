all: images

IMAGES := sample-usage

all: $(addprefix ../data/api/,$(addsuffix .json,$(IMAGES)))

../data/api/%.json: argo-submit-%
	argo wait record-$(*F)
	argo get record-$(*F) -o json \
		| jq -r '.status.nodes."record-$(*F)".outboundNodes[0]' \
		| xargs -n 1 -I% wget 'http://localhost:2746/artifacts/argo/record-$(*F)/%/api'
	tar -xvf api
	rm api
	mv -f api.json $@

argo-submit-%: image-%
	-argo delete record-$(*F)
	argo submit record.workflow.yml -p label="$(*F)" -p tag="1.1.0" --name 'record-$(*F)' --watch



images: $(addprefix image-,$(IMAGES))

image-%: image-record-api
	docker build -t dataapis/$(*F):1.1.0 --build-arg label=1.1.0 ./images/$(*F)



image-record-api:
	docker build -t dataapis/record-api:1.1.0 ./images/record-api