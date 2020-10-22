# Kubernetes Support

## Goals

The intent of this sub directory is to add support for tracing libraries and produces results in a reproducible manner on cloud hardware. Previously I had been running everything locally, but this becomes time prohibitive when the runs last many hours and also requires a lot of human intervention whenever the software changes.

The goal is to make it entirely source code driven, where all interactions are automated as source code changes.

## Events and Tasks

There are a number of moving parts here, so I think I will start with an overview of the tasks that need to be done. Then we can go over how they are automated.

1. Run a test suite or some notebook or script with tracing enabled, to output a trace file that is often very large, since it has a line for every invocation of every function in the namespace we are testing.
2. Do some post processing on that file to summerize the findings and reduce the size.
3. Combine this with other results and generate typings files that show APIs generated.

So if we think of this repository as some narrative over time, there are a number of events that can happen that can cause some of these steps to be need to be re-run.

1. Any change in the code that affects how libraries are traced, or how the typing is generated. Depending on what part of the code it changes, it may need some or all steps to be executed for all libraries.
2. A new library wants to be added to be tested against, or an existing one needs to be updated. In this case, just that library needs all steps re-run, along with the last step of consolidating all the results.


---

Old notes:


This directory adds the ability to do runs in a distributed manner through kubernetes and Argo.

It doesn't put everything in one giant workflow, but instead we run different workflows for each library.

This is because they are long running and can fail, and we want to be able to re-try them easily. Plus once we have the results from each library, combining their APIs into one file and creating the API is not too intensive and can be done locally. (This could maybe be moved to the [Work Avoidance](https://argoproj.github.io/argo/work-avoidance/) mechanism, we we want to be able to run it all as one large workload. Or use the [new "step cache"](https://github.com/argoproj/argo/issues/944) feature that isnt done yet)

Run `make` here to submit a number of Argo jobs and wait for them to finish. It will take the artifacts and save them to the `../data` folder.

Then run the parent `make` to combine those APIs.

I chose to keep them separate, so we can still run things locally for testing and debugging.


This runs with experimental Docker for building, so we can
have build caches: https://stackoverflow.com/a/58021389/907060

Requires docker buildx master, b/c we need https://github.com/docker/buildx/pull/280
and it hasn't been released yet.

https://github.com/docker/buildx#with-docker-1809



Buildx bake tutorial: https://github.com/FernandoMiguel/BuildKit

```bash
# To create buildx  remote
kubectl create ns buildx
kubectl apply -f ./resource-defaults.yml --namespace=buildx
make buildx-driver
docker buildx bake --push


# To create argo
kubectl create ns argo
# set default NS
kubectl config set-context --current --namespace=argo
# install Argo
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/namespace-install.yaml 
# expose argo UI
kubectl patch svc argo-server -n argo -p '{"spec": {"type": "LoadBalancer"}}'
kubectl get svc argo-server -n argo

# Add  ability to pull images
doctl registry kubernetes-manifest --namespace argo | kubectl apply -f -
# Maybe not needed?
kubectl patch serviceaccount argo-server -p '{"imagePullSecrets": [{"name": "registry-python-record-api"}]}'
kubectl patch serviceaccount argo -p '{"imagePullSecrets": [{"name": "registry-python-record-api"}]}'
kubectl patch serviceaccount default -p '{"imagePullSecrets": [{"name": "registry-python-record-api"}]}'


# These are some magic incarnations, one or both might not be needed 🤷‍♂ :embe
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default -n argo
kubectl create rolebinding namespace-admin --clusterrole=admin --serviceaccount=default:default

# Create Digital OCean spaces (or other s3 compatible backend) with `record-api` bucket and set keys:
kubectl create secret generic artifact-s3 --from-literal=accesskey=ACCESS_KEY --from-literal=secretkey=SECRET_KEY
jq --null-input '{data: {artifactRepository: {archiveLogs: true, s3: {bucket: "record-api", endpoint: "S3_ENDPOINT", accessKeySecret: {name: "artifact-s3", key: "accesskey"}, secretKeySecret: {name: "artifact-s3", key: "secretkey"}}}|tojson}}' --compact-output | xargs -0 -n 1  kubectl patch configmap workflow-controller-configmap --dry-run -p
# Create github token with repo and actions permission to trigger action on completion
kubectl create secret generic github --from-literal=token=TOKEN


# To submit workflow
make argo-submit
make all
```