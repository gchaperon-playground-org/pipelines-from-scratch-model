import kfp.dsl


@kfp.dsl.component(base_image="python:3.10", target_image="us-central1-docker.pkg.dev/pipelines-from-scratch/components/add:0.1.0")
def add(a: int, b: int) -> int:
    return a + b
