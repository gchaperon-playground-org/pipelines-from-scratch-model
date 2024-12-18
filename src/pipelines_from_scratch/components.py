import functools

import kfp.dsl

import pipelines_from_scratch


DOCKER_REGISTRY = "us-central1-docker.pkg.dev/pipelines-from-scratch"
COMPONENTS_REPO = "components"
IMAGE_NAME = f"{DOCKER_REGISTRY}/{COMPONENTS_REPO}/{pipelines_from_scratch.__name__}"
# NOTE: Python version uses "+" (plus sign) to separate version from local
# specifier, e.g. 1.2.1.dev2+g42eecf3.d20241126224450. The plus sign is an
# invalid character in a Docker tag, so we replace it for a valid character.
# References:
# https://packaging.python.org/en/latest/specifications/version-specifiers/#local-version-identifiers
# https://docs.docker.com/reference/cli/docker/image/tag/#description
DOCKER_TAG = pipelines_from_scratch.__version__.replace("+", "-")


# NOTE: on the lack of base_image argument, we handle the image ourselves via
# the Dockerfile found in the project root.
component = functools.partial(
    kfp.dsl.component,
    target_image=f"{IMAGE_NAME}:{DOCKER_TAG}",
)


@component
def add(a: int, b: int) -> int:
    return a + b
