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