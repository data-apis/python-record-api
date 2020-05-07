import importlib
import runpy
import os

from .core import *

if __name__ == "__main__":
    setup()
    IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")
    RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]
    TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]

    if IMPORT_MODULES:
        for name in IMPORT_MODULES.split(","):
            # access dict of module so that apipkg virtual modules will be fully imported
            # (need this or else get weird errors in pytest)
            importlib.import_module(name).__dict__

    try:
        with Tracer(TRACE_MODULE):
            runpy.run_module(RUN_MODULE, run_name="__main__", alter_sys=True)
    except Exception:
        raise Exception(f"Error running {RUN_MODULE}")
    finally:
        finalize()
