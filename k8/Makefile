
PYTHON_PACKAGE_VERSION := $(shell python -c 'import record_api; print(record_api.__version__)')

$(info Python package version = ${PYTHON_PACKAGE_VERSION})

IMAGE := registry.digitalocean.com/python-record-api

# The tag for base image is base-{python version}-{version-increment}
# The tag for other versions are {name}-{python version}-{base version increment}-{version increment}
# So that if the python version is updated, all are rebuilt, and if the base version is updated, all are also rebuilt.

version = $(shell cat images/$(1)/version)


BASE_IMAGE := ${IMAGE}/base:${PYTHON_PACKAGE_VERSION}-$(call version,base)

BASE_CACHE_IMAGE := ${IMAGE}/base:cache

$(info Base image = ${BASE_IMAGE})

sub_tag = $(1):${PYTHON_PACKAGE_VERSION}-$(call version,base)-$(call version,$(1))
sub_image = ${IMAGE}/$(call sub_tag,$(1))
sub_cache_image = ${IMAGE}/$(1):cache

WORKFLOW_VERSION := $(shell cat argo/version)
$(info Workflow version = ${WORKFLOW_VERSION})

workflow_name = $(subst :,-,$(call sub_tag,$(1)))-${WORKFLOW_VERSION}

IGNORE_IMAGES := django base
IMAGES := $(sort $(filter-out ${IGNORE_IMAGES},$(notdir $(wildcard images/*))))


$(info Names = ${IMAGES})


ifdef WORKFLOW_NAME
$(info )
$(info workflow name = ${WORKFLOW_NAME})
WORKFLOW_LABEL := $(shell python -c 'print("-".join("${WORKFLOW_NAME}".split("-")[:-4]))')
$(info workflow label = ${WORKFLOW_LABEL})
endif



$(info )

$(info jq version = $(shell jq --version))
$(info argo version = $(shell argo version --short))
$(info docker builx version = $(shell docker buildx version))


$(info )
# ARGO_SUBMITTED_WORKFLOWS := $(shell argo list -o name)

# # loop through images, any which have a workflow that is in argos submitted workflows should be notadd
# # if they are not in there, they should be added

# NOT_SUBMITTED_IMAGES := $(foreach \
# 	name,\
# 	$(IMAGES),\
# 	$(if \
# 		$(findstring \
# 			$(call workflow_name,${name}),\
# 			${ARGO_SUBMITTED_WORKFLOWS}\
# 		),\
# 		,\
# 		${name}\
# 	)
# )

# Pass in the WORKFLOW_NAME as a variable
download-workflow:
	argo get ${WORKFLOW_NAME} -o json \
		| jq -r '.status.outputs.artifacts[] | select(.name == "api") | .s3 | "artifact/" + .bucket + "/" + .key' \
		| xargs mc cat \
		| tar -xvzf - -C ../data/api/
	mv -f ../data/api/api.json ../data/api/${WORKFLOW_LABEL}.json


argo-submit: $(addprefix argo-submit-,$(IMAGES))

argo-submit-%:
	-argo submit \
		argo/workflow.yml \
		-p label="$(*F)" \
		-p base-image="$(BASE_IMAGE)" \
		-p image="$(call sub_image,$(*F))" \
		--name "$(call workflow_name,$(*F))"


push-images: docker-bake.json
	docker buildx bake base --push
	docker buildx bake --push


test-%: docker-bake.json
	# docker buildx bake --push $(*F)
	docker run \
		--rm \
		-it \
		-e PYTHON_RECORD_API_TO_MODULES=numpy,pandas \
		-e PYTHON_RECORD_API_OUTPUT_FILE=/tmp/d/out.jsonl \
		-v $$PWD/tmp:/tmp/d \
		$(call sub_image,$(*F))


# push-images:  $(addprefix push-image-,$(IMAGES))

# push-image-%:
# 	docker push saulshanabrook/python-record-api:$(*F)-$(TAG)

# build-images: docker-bake.json
# 	docker buildx bake


# Generate docker bake file with default group
# https://github.com/docker/buildx/issues/183#issuecomment-551216260

# file parsing
# https://github.com/docker/buildx/blob/fd6de6b6aeac780c59e5079a96b068076b676d73/bake/bake.go#L333
define JQ_DOCKER_BAKE
{	
	group: {
		default: {
			targets: ($$ARGS.positional)
		}
	},
	target: (
		{
			"base-base": {
				dockerfile: "Dockerfile",
			},
			base: {
				context: "images/base",
				inherits: ["base-base"],
				"cache-to": ["type=registry,ref=${BASE_CACHE_IMAGE},mode=max"],
				"cache-from": ["type=registry,ref=${BASE_CACHE_IMAGE}"],
				args: {
					PYTHON_PACKAGE_VERSION: "${PYTHON_PACKAGE_VERSION}"
				},
				tags: [
					"${BASE_IMAGE}"
				]
			}
		} +
		(
			reduce 
			(
				($$ARGS.positional[]) | {
					(.): {
						context: ("images/" + .),
						inherits: ["base-base"],
						args: {
							FROM: "${BASE_IMAGE}"
						},
						"cache-to": ["type=registry,ref=" + ($$ARGS.named[(. + "-cache")]) + ",mode=max"],
						"cache-from": ["type=registry,ref=" + ($$ARGS.named[(. + "-cache")])],
						tags: [
							($$ARGS.named[(.)])
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
docker-bake.json: Makefile images/
	jq "$$JQ_DOCKER_BAKE" \
		--null-input \
		$(foreach name,$(IMAGES),--arg $(name) $(call sub_image,$(name))) \
		$(foreach name,$(IMAGES),--arg $(name)-cache $(call sub_cache_image,$(name))) \
		--args $(IMAGES) \
		> $@


buildx-driver:
	docker buildx create --driver kubernetes --use --driver-opt namespace=buildx --node buildx0

k8-argo-default:
	kubectl config set-context --current --namespace=argo