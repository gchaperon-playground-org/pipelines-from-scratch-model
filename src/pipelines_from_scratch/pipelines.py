import kfp.dsl

import pipelines_from_scratch.components as components


@kfp.dsl.pipeline
def math_pipeline(a: int, b: int, c: int) -> str:
    t1 = components.add(a=a, b=b)
    t2 = components.add(a=t1.output, b=c)
    return t2.output
