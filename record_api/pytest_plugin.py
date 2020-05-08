import pytest
import os

from .core import *


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    with get_tracer():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_sessionstart(*args):
    setup()
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(*args):
    yield
    finalize()
