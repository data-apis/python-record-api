all: images

BASE_BUILD_TAG := 1.1.0
BASE_USE_TAG := 1.1.0

TAG := 1.1.0v3

IMAGES := dask matplotlib pandas sample-usage skimage sklearn xarray 

all: $(addprefix ../data/api/,$(addsuffix .json,$(IMAGES)))

../data/api/%.json: .
	argo wait record-$(*F)
	argo get record-$(*F) -o json \
		| jq -r '.status.nodes."record-$(*F)".outboundNodes[0]' \
		| xargs -n 1 -I% mc cat 'argo-artifacts-local/my-bucket/record-$(*F)/%/api.tgz' \
		| tar -xvf - -C $(@D)
	mv -f $(@D)/api.json $@

# 	| xargs -n 1 -I% wget 'http://localhost:2746/artifacts/argo/record-$(*F)/%/api'
# tar -xvf api
# rm api
# mv -f api.json $@


argo-submit: $(addprefix argo-submit-,$(IMAGES))

argo-submit-%:
	-argo delete record-$(*F)
	# Wait for pod to be deleted before re-creating
	sleep 10
	argo submit --from workflowtemplate/python-record-api -p label="$(*F)" -p tag="$(TAG)" -p base-tag="$(BASE_USE_TAG)" --name 'record-$(*F)'


argo-workflow-submit:
	-argo template delete python-record-api
	argo template create workflow-template.yml


push-images: docker-bake.json
	docker buildx bake --push


# push-images:  $(addprefix push-image-,$(IMAGES))

# push-image-%:
# 	docker push saulshanabrook/python-record-api:$(*F)-$(TAG)

# build-images: docker-bake.json
# 	docker buildx bake


# Generate docker bake file with default group
# https://github.com/docker/buildx/issues/183#issuecomment-551216260

define JQ_DOCKER_BAKE
{	
	group: {
		default: {
			targets: (["base"] + ($$ARGS.positional))
		}
	},
	target: (
		{
			base: {
				context: "images/base",
				dockerfile: "Dockerfile",
				tags: [
					"saulshanabrook/python-record-api:base-${BASE_BUILD_TAG}"
				]
			}
		} +
		(
			reduce 
			(
				($$ARGS.positional[]) | {
					(.): {
						context: ("images/" + .),
						dockerfile: "Dockerfile",
						args: {
							FROM: "saulshanabrook/python-record-api:base-${BASE_USE_TAG}"
						},
						tags: [
							("saulshanabrook/python-record-api:" + . + "-${TAG}")
						]
					}
				}
			) as $$i
			({}; $$i + .)
		)
	)
}
endef

export JQ_DOCKER_BAKE
# https://stackoverflow.com/a/649462/907060
docker-bake.json: Makefile
	jq "$$JQ_DOCKER_BAKE" \
		--null-input \
		--args $(IMAGES) \
		> $@


port-forward:
	kubectl -n argo port-forward deployment/argo-server 2746:2746

set-namespace:
	kubectl config set-context --current --namespace=argo