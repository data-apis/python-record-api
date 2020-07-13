This directory adds the ability to do runs in a distributed manner through kubernetes and Argo.

It doesn't put everything in one giant workflow, but instead we run different workflows for each library.

This is because they are long running and can fail, and we want to be able to re-try them easily. Plus once we have the results from each library, combining their APIs into one file and creating the API is not too intensive and can be done locally. (This could maybe be moved to the [Work Avoidance](https://argoproj.github.io/argo/work-avoidance/) mechanism, we we want to be able to run it all as one large workload).

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
docker buildx create --driver kubernetes --use --driver-opt namespace=buildx
docker buildx bake --push


# To create argo
kubectl create ns argo
# set default NS
kubectl config set-context --current --namespace=argo
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/namespace-install.yaml 
kubectl port-forward deployment/argo-server 2746:2746
open http://localhost:2746

kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default -n argo

# Add minio
# https://argoproj.github.io/argo/configure-artifact-repository/#configuring-minio
# Configure to use minio
# https://argoproj.github.io/argo/configure-artifact-repository/#s3-compatible-artifact-repository-bucket-such-as-aws-gcs-and-minio
# https://www.alibabacloud.com/blog/installing-argo-in-your-kubernetes-cluster_595446   




# To submit workflow
make argo-workflow-submit
make argo-submit
make all
```