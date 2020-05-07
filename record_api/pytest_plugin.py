import pytest
import os

from .core import *


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]
    with Tracer(TRACE_MODULE):
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_sessionstart(*args):
    setup()
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(*args):
    finalize()
    yield

