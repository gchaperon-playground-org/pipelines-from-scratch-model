import kfp.dsl

import pipelines_from_scratch


DOCKER_REGISTRY = "us-central1-docker.pkg.dev/pipelines-from-scratch"
COMPONENTS_REPO = "components"
# NOTE: Python version uses "+" (plus sign) to separate version from local
# specifier, e.g. 1.2.1.dev2+g42eecf3.d20241126224450. The plus sign is an
# invalid character in a Docker tag, so we replace it for a valid character.
# References:
# https://packaging.python.org/en/latest/specifications/version-specifiers/#local-version-identifiers
# https://docs.docker.com/reference/cli/docker/image/tag/#description
DOCKER_TAG = pipelines_from_scratch.__version__.replace("+", "-")


@kfp.dsl.component(
    base_image="python:3.10-slim",
    target_image=f"{DOCKER_REGISTRY}/{COMPONENTS_REPO}/add:{DOCKER_TAG}",
)
def add(a: int, b: int) -> int:
    return a + b
