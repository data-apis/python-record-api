import sys
import dis
import numpy as np
import functools
import types
from typing import *

import inspect


DESIRED_MODULE = "numpy"


def get_name(value) -> str:
    return f"{value.__module__}.{value.__name__}"


def save_log(
    fn: str,
    caller_args: List[str],
    caller_kwargs: List[str],
    fn_arguments: Dict[str, str],
    fn_varargs: List[str],
    fn_varkw: Dict[str, str],
) -> None:
    data = {
        "function": fn,
        "caller_args": caller_args,
        "caller_kwargs": caller_kwargs,
        "function_arguments": fn_arguments,
        "function_var_positional": fn_varargs,
        "function_var_keyword": fn_varkw,
    }
    print(data)


def log_call(fn: types.FunctionType, args: Sequence, kwargs: Sequence):
    fn_name = get_name(fn)
    arg_types = list(map(get_name, map(type, args)))
    kwarg_types = {key: get_name(type(value)) for key, value in kwargs.items()}

    sig = inspect.signature(fn)

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

    vararg_types = bound_arguments.pop(vararg_param) if vararg_param is not None else []
    varkw_types = bound_arguments.pop(varkw_param) if varkw_param is not None else {}

    save_log(
        fn_name, arg_types, kwarg_types, bound_arguments, vararg_types, varkw_types
    )


def tracer(frame, event, arg):
    if event != "call":
        return
    fn_var = frame.f_code.co_name
    fn = frame.f_globals[fn_var]
    module = fn.__module__
    # if we aren't tracing in a module we want, keep tracing down
    if not module.startswith(DESIRED_MODULE):
        return tracer
    arg_vars, varargs_var, varkw_var, frame_locals = inspect.getargvalues(frame)

    # list of args passed in
    args = [frame_locals[arg] for arg in arg_vars]
    # variable args (*...) passed in
    varargs = frame_locals[varargs_var] if varargs_var else []
    # variable kwargs (**...) passed in
    varkw = frame_locals[varkw_var] if varkw_var else {}

    log_call(fn, args + varargs, varkw)


def fn():
    x = np.arange(10)
    # np.arange(10)
    z = 10
    # np.arange(z)
    x.reshape((2, 5))
    x.reshape((5, 2))
    x.reshape((10, 1))
    # y = x[0:2] + x[2:4]
    z = np.power(100, 10)
    z.sum()
    z.max()
    z.mean()
    # z = np.power(x, y)
    # z * 10000
    # print(z)
    # print("SCIIKIT")
    # detected = detector.detect_multi_scale(
    #     img=img, scale_factor=1.2, step_ratio=1, min_size=(60, 60), max_size=(123, 123)
    # )
    # print("DONE")


# import cProfile

# cProfile.run('fn()')

sys.settrace(tracer)
# sys.setprofile(profiler)
fn()
sys.settrace(None)
# sys.setprofile(None)
