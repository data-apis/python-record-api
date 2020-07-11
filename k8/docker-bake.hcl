# "docs"
# https://github.com/docker/buildx#buildx-bake-options-target
# https://github.com/docker/buildx/blob/fd6de6b6aeac780c59e5079a96b068076b676d73/bake/bake.go#L333

variable "BASE_BUILD_TAG" {
	default = "1.1.0"
}

variable "BASE_USE_TAG" {
	default = "1.1.0"
}

variable "TAG" {
	default = "1.1.0v1"
}

group "default" {
	targets = ["base", "dask", "pandas", "sample-usage", "skimage", "sklearn", "xarray"]
}


function "image" {
	params = [name, tag]
	result = "saulshanabrook/python-record-api:${name}-${tag}"
}


target "base" {
	context = "images/base"
	tags = [image("base", BASE_BUILD_TAG)]
}

target "base-downstream" {
	args = {
		FROM = image("base", BASE_USE_TAG)
	}
}


target "dask" {
	inherits = ["base-downstream"]
	context = "images/dask"
	tags = [image("dask", TAG)]
}

target "pandas" {
	inherits = ["base-downstream"]
	context = "images/pandas"
	tags = [image("pandas", TAG)]
}

target "sample-usage" {
	inherits = ["base-downstream"]
	context = "images/sample-usage"
	tags = [image("sample-usage", TAG)]
}

target "skimage" {
	inherits = ["base-downstream"]
	context = "images/skimage"
	tags = [image("skimage", TAG)]
}

target "sklearn" {
	inherits = ["base-downstream"]
	context = "images/sklearn"
	tags = [image("sklearn", TAG)]
}

target "xarray" {
	inherits = ["base-downstream"]
	context = "images/xarray"
	tags = [image("xarray", TAG)]
}