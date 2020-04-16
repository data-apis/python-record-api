import dis
import functools
import inspect
import io
import sys
import types
import json
from typing import *
import os
import runpy
import importlib


FILE_NAME = os.environ["PYTHON_API_OUTPUT_FILE"]
TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]
RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]
IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")


def get_name(value) -> str:
    return f"{value.__module__}.{value.__name__}"


def save_log(
    fn: str,
    caller_args: List[str],
    caller_kwargs: List[str],
    signature_available: bool,
    fn_arguments: Optional[Dict[str, str]],
    fn_varargs: Optional[List[str]],
    fn_varkw: Optional[Dict[str, str]],
) -> None:
    data = {
        "function": fn,
        "caller_args": caller_args,
        "caller_kwargs": caller_kwargs,
        "signature_available": signature_available,
        "function_arguments": fn_arguments,
        "function_var_positional": fn_varargs,
        "function_var_keyword": fn_varkw,
    }
    writer.write((json.dumps(data) + "\n").encode())


def log_call(fn: types.FunctionType, args: Sequence, kwargs: Sequence):
    fn_name = get_name(fn)
    arg_types = list(map(get_name, map(type, args)))
    kwarg_types = {key: get_name(type(value)) for key, value in kwargs.items()}

    try:
        sig = inspect.signature(fn)
    except ValueError:
        bound_arguments = None
        vararg_types = None
        varkw_types = None
        signature_available = False
    else:
        # pop off var args and var kwargs from bound arguments
        # so we can save log them seperately
        vararg_param = None
        varkw_param = None
        for param in sig.parameters.values():
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                vararg_param = param.name
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                varkw_param = param.name

        bound_arguments = sig.bind(*arg_types, **kwarg_types).arguments

        vararg_types = (
            bound_arguments.pop(vararg_param, []) if vararg_param is not None else []
        )
        varkw_types = (
            bound_arguments.pop(varkw_param, {}) if varkw_param is not None else {}
        )
        signature_available = True

    save_log(
        fn_name,
        arg_types,
        kwarg_types,
        signature_available,
        bound_arguments,
        vararg_types,
        varkw_types,
    )


def tracer(frame, event, arg):
    if event != "call":
        return
    module = inspect.getmodule(frame)
    if not module or not module.__name__.startswith(TRACE_MODULE):
        return tracer

    fn_var = frame.f_code.co_name
    if fn_var.startswith("<"):
        return tracer
    try:
        fn = frame.f_globals[fn_var]
    except KeyError:
        print(f"Could not get {fn_var}")
        return tracer

    arg_vars, varargs_var, varkw_var, frame_locals = inspect.getargvalues(frame)

    # list of args passed in
    args = [frame_locals[arg] for arg in arg_vars]
    # variable args (*...) passed in
    varargs = list(frame_locals[varargs_var]) if varargs_var else []
    # variable kwargs (**...) passed in
    varkw = frame_locals[varkw_var] if varkw_var else {}

    log_call(fn, args + varargs, varkw)


rand_file = io.FileIO(FILE_NAME, "w")
writer = io.BufferedWriter(rand_file)

if IMPORT_MODULES:
    for module in IMPORT_MODULES.split(","):
        importlib.import_module(module)
try:
    sys.settrace(tracer)
    runpy.run_module(RUN_MODULE, run_name="__main__", alter_sys=True)
except Exception:
    sys.settrace(None)
    raise Exception(f"Error running {RUN_MODULE}")
else:
    sys.settrace(None)
finally:
    writer.flush()
    rand_file.close()
