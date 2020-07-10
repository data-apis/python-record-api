import runpy

from .core import *

if __name__ == "__main__":

    setup()
    tracer = get_tracer()
    try:
        with tracer:
            runpy.run_module(
                tracer.calls_from_modules[0], run_name="__main__", alter_sys=True
            )
    except Exception:
        raise Exception(f"Error running {tracer.calls_from_modules}")
    finally:
        finalize()
