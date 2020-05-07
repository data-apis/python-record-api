import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_pyfunc_call(pyfuncitem):
    print("calling", pyfuncitem)

    outcome = yield
    # outcome.excinfo may be None or a (cls, val, tb) tuple
    print("done")
