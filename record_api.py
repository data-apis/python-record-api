import importlib
import inspect
import io
import json
import opcode
import os
import runpy
import sys
import types
from typing import *

from get_stack import OpStack

FILE_NAME = os.environ["PYTHON_API_OUTPUT_FILE"]
TRACE_MODULE = os.environ["PYTHON_API_TRACE_MODULE"]
RUN_MODULE = os.environ["PYTHON_API_RUN_MODULE"]
IMPORT_MODULES = os.environ.get("PYTHON_API_IMPORT_MODULES", "")


def type_name(value: object) -> str:
    tp = type(value)
    module = inspect.getmodule(tp)
    return f"{module.__name__}.{tp.__qualname__}"


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


def log_call(fn: types.FunctionType, module_name: str, *args, **kwargs):
    fn_name = f"{module_name}.{fn.__qualname__}"
    arg_types = list(map(type_name, args))
    kwarg_types = {key: type_name(value) for key, value in kwargs.items()}

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


# Keep a set of frames that we have recorded a call
# from. We should add to this when we record a bytecode
# trace from a function call
# we should pop one off this to check if we should keep tracing
# below this frame
RECORDED_CALL_FRAMES = set()


def tracer(frame, event, arg):
    frame.f_trace_opcodes = True
    if event == "call":
        try:
            RECORDED_CALL_FRAMES.remove(frame.f_back)
        except KeyError:
            # we didnt record the call frame, so keep tracing
            return tracer
        # we did record this call frame, so dont trace below here
        return None
    if event != "opcode":
        return
    stack = OpStack(frame)
    opname = opcode.opname[frame.f_code.co_code[frame.f_lasti]]
    if opname == "UNARY_POSITIVE":
        arg = stack[-1]
        tp = type(arg)
        module_name = inspect.getmodule(tp).__name__

        if module.startswith(TRACE_MODULE):
            log_call(tp.__pos__, module_name, arg)


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
