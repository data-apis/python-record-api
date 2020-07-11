This directory adds the ability to do runs in a distributed manner through kubernetes and Argo.

It doesn't put everything in one giant workflow, but instead we run different workflows for each library.

This is because they are long running and can fail, and we want to be able to re-try them easily. Plus once we have the results from each library, combining their APIs into one file and creating the API is not too intensive and can be done locally. (This could maybe be moved to the [Work Avoidance](https://argoproj.github.io/argo/work-avoidance/) mechanism, we we want to be able to run it all as one large workload).

Run `make` here to submit a number of Argo jobs and wait for them to finish. It will take the artifacts and save them to the `../data` folder.

Then run the parent `make` to combine those APIs.

I chose to keep them separate, so we can still run things locally for testing and debugging.


This runs with experimental Docker for building, so we can
have build caches: https://stackoverflow.com/a/58021389/907060

Requires docker buildx >= 0.4.0


```bash
# To create buildx 
kubectl create ns buildx
docker buildx create --driver kubernetes --use
docker buildx bake --push

# To create argo
kubectl create ns argo
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/quick-start-minimal.yaml
# set default NS
kubectl config set-context --current --namespace=argo
kubectl port-forward deployment/argo-server 2746:2746
open http://localhost:2746


# To create argo
make argo-workflow-submit
make argo-submit
make all
```