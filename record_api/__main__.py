import importlib
import runpy
import os

from .core import *

if __name__ == "__main__":
    IMPORT_MODULES = os.environ.get("PYTHON_RECORD_API_IMPORT_MODULES", "")

    if IMPORT_MODULES:
        for name in IMPORT_MODULES.split(","):
            # access dict of module so that apipkg virtual modules will be fully imported
            # (need this or else get weird errors in pytest)
            importlib.import_module(name).__dict__

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
