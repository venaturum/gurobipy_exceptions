import gurobipy as gp

from gurobipy_exceptions.decorators import convert_error, patch_error_message
from gurobipy_exceptions.exceptions import *


def _isPyCFunction(object):
    try:
        return str(type(object)) == "<class 'cython_function_or_method'>"
    except:
        return False


def _make_patch_method(obj):
    import inspect

    assert obj in (gp, gp.Model)

    def patch(convert=False):
        """Modifies methods on {obj} to either fix missing messages in GurobiError objects,
        or replace GurobiError objects with more specific subclasses, corresponding to error numbers.

        Parameters
        ----------
        convert : bool, default False
            If true then GurobiErrors will be replaced with custom exceptions from gurobipy_exceptions.
            If false then empty messages will be overwritten with messages taken from Gurobi documentation.
        """
        method = convert_error if convert else patch_error_message
        for (
            name,
            f,
        ) in inspect.getmembers(obj, _isPyCFunction):
            if name[0] != "_":
                setattr(obj, name, method(f))

    patch.__doc__ = patch.__doc__.format(obj=obj)
    return patch


patch_model_methods = _make_patch_method(gp.Model)
patch_module_methods = _make_patch_method(gp)
