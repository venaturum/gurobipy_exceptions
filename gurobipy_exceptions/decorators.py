import functools

import gurobipy as gp

from gurobipy_exceptions import conversion


def convert_error(func):
    """decorator for converting gurobipy.GurobiError to child error defined in gurobipy_exceptions package"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except gp.GurobiError as e:
            conversion.convert_error(e)

    return wrapper


def patch_error_message(func):
    """decorator for patching missing argument (the message) in gurobipy.GurobiError"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except gp.GurobiError as e:
            conversion.patch_error_message(e)

    return wrapper
