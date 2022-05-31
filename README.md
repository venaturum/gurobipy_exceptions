# gurobipy_exceptions

_Extending and patching gurobipy exceptions.  This is neither produced, or endorsed, by Gurobi!_


## Installation

Available as a python package `gurobipy_exceptions` which can be installed with pip:

    pip install git+https://github.com/venaturum/gurobipy_exceptions

or with [Poetry](https://python-poetry.org/) (place the following dependency in pyproject.toml)

    gurobipy_exceptions = {git = "https://github.com/venaturum/gurobipy_exceptions.git", rev = "main"}
    
## Motivation 1

The motivation for `gurobipy_exceptions` is two-fold.  The first is that sometimes error messages go missing (current as of gurobipy 9.5.1).  For example, consider the following piece of code, run in an environment with a demo license from Gurobi.  It fails due to size limit on models for such a license.

    >> import gurobipy as gp
	>>
    >> def run():
    >>     m = gp.Model("Large Model")
    >>     _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >>     m.optimize()
    >> 
    >> run()

    GurobiError: Model too large for size-limited license; visit https://www.gurobi.com/free-trial for a full license

However note the change in behaviour when the `optimize` method is passed a callback:

    >> def callback(model, where):
    >>     pass
    >>
    >> def run():
    >>    m = gp.Model("Large Model")
    >>    _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >>    m.optimize(callback)
    >> 
    >> run()

    GurobiError:

The error number is preserved, but the underlying message is not.

`gurobipy_exceptions` provides decorators which can be used to wrap methods to patch missing error messages.  The error messages used are taken from Gurobi's online documentation.  For example,

    >> import gurobipy_exceptions as gp_exc
    >> 
    >> @gp_exc.patch_error_message
    >> def run():
    >>     m = gp.Model("Large Model")
    >>     _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >>     m.optimize(callback)
    >> 
    >> run()

    GurobiError: Attempted to solve a model that is larger than the limit for a demo license

In this case it is the decorator has worked its magic on the `run` method.  This approach would require defining functions wherever error-patching is to occur.

Alternatively, a module level function `gurobipy_exceptions.patch_model_methods` can be used to patch the methods on `gurobipy.Model`.   For example,

    >> import gurobipy_exceptions as gp_exc
    >> gp_exc.patch_model_methods()
    >>
    >> def callback(model, where):
    >>     pass
    >>
    >> m = gp.Model("Large Model")
    >> _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >> m.optimize(callback)

    GurobiError: Attempted to solve a model that is larger than the limit for a demo license

Note that `gurobipy_exceptions.patch_module_methods` is also available for patching functions defined in the `gurobipy` module.

## Motivation 2

The second motivation is largely a matter of taste, but there is an argument that it makes the code more readable, pythonic, and allows IDE code-completion features to be utilised.

The idea is to replace GurobiError exceptions, which are differentiated with a error code attribute, with explicit exceptions unique for each error code.  Again this can be achieved with a decorator (`gurobipy_exceptions.convert_error`).


    >> @gp_exc.convert_error
    >> def run():
    >>     m = gp.Model("Large Model")
    >>     _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >>     m.optimize(callback)
    >> 
    >> run()

    GRBSizeLimitExceeded: Attempted to solve a model that is larger than the limit for a demo license


Alternatively patching at the `gurobipy.Model` level is possible by using the `gurobipy_exceptions.patch_model_methods` (as demonstrated above), but using *convert=True* as an argument.

    >> gp_exc.patch_model_methods(convert=True)
    >> 
    >> m = gp.Model("Large Model")
    >> _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >> m.optimize(callback)

    GRBSizeLimitExceeded: Attempted to solve a model that is larger than the limit for a demo license

This approach, for example, facilitates handling multiple exceptions without appealing to if-else chains:

    >> try:
    >>     m = gp.Model("Large Model")
    >>     _ = m.addVars(range(10000), vtype=GRB.BINARY)
    >>     m.optimize(callback)
    >> except gp_exc.GRBSizeLimitExceeded as e:
    >>     # handle size limit exception
    >>     pass
    >> except gp_exc.GRBOutOfMemory as e:
    >>     # handle memoryt exception
    >>     pass
    >> except gp_exc.GRBNumeric as e:
    >>     # handle numeric exception
    >>     pass
    >> except gp.GurobiError as e:
    >>     # handle general Gurobi exception
    >>     pass
	>> except Exception as e:
	>>     # handle exception
    >>     pass


## Defined Exceptions

Taken from [https://www.gurobi.com/documentation/9.5/refman/error_codes.html#sec:ErrorCodes:](https://www.gurobi.com/documentation/9.5/refman/error_codes.html#sec:ErrorCodes).

| Error Code               | Error Number | Description                                                                                                                                                                                     | gurobipy_exception Class                                                                                                                                              |                                                                                                                                                                         |                                                       |                                        |
|--------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------|
| OUT_OF_MEMORY            | 10001        | Available memory was exhausted                                                                                                                                                                  | gurobipy_exceptions.GRBOutOfMemory                                                                                                                                    |                                                                                                                                                                         |                                                       |                                        |
| NULL_ARGUMENT            | 10002        | NULL input value provided for a required argument                                                                                                                                               | gurobipy_exceptions.GRBNullArgument                                                                                                                                   |                                                                                                                                                                         |                                                       |                                        |
| INVALID_ARGUMENT         | 10003        | An invalid value was provided for a routine argument                                                                                                                                            | gurobipy_exceptions.GRBInvalidArgument                                                                                                                                |                                                                                                                                                                         |                                                       |                                        |
| UNKNOWN_ATTRIBUTE        | 10004        | Tried to query or set an unknown attribute                                                                                                                                                      | gurobipy_exceptions.GRBUnknownAttribute                                                                                                                               |                                                                                                                                                                         |                                                       |                                        |
| DATA_NOT_AVAILABLE       | 10005        | Attempted to query or set an attribute that could not be accessed at that time                                                                                                                  | gurobipy_exceptions.GRBDataNotAvailable                                                                                                                               |                                                                                                                                                                         |                                                       |                                        |
| INDEX_OUT_OF_RANGE       | 10006        | Tried to query or set an attribute                                                                                                                                                              | but one or more of the provided indices (e.g.                                                                                                                         | constraint index                                                                                                                                                        | variable index) was outside the range of valid values | gurobipy_exceptions.GRBIndexOutOfRange |
| UNKNOWN_PARAMETER        | 10007        | Tried to query or set an unknown parameter                                                                                                                                                      | gurobipy_exceptions.GRBUnknownParameter                                                                                                                               |                                                                                                                                                                         |                                                       |                                        |
| VALUE_OUT_OF_RANGE       | 10008        | Tried to set a parameter to a value that is outside the parameter's valid range                                                                                                                 | gurobipy_exceptions.GRBValueOutOfRange                                                                                                                                |                                                                                                                                                                         |                                                       |                                        |
| NO_LICENSE               | 10009        | Failed to obtain a valid license                                                                                                                                                                | gurobipy_exceptions.GRBNoLicense                                                                                                                                      |                                                                                                                                                                         |                                                       |                                        |
| SIZE_LIMIT_EXCEEDED      | 10010        | Attempted to solve a model that is larger than the limit for a demo license                                                                                                                     | gurobipy_exceptions.GRBSizeLimitExceeded                                                                                                                              |                                                                                                                                                                         |                                                       |                                        |
| CALLBACK                 | 10011        | Problem in callback                                                                                                                                                                             | gurobipy_exceptions.GRBCallback                                                                                                                                       |                                                                                                                                                                         |                                                       |                                        |
| FILE_READ                | 10012        | Failed to read the requested file                                                                                                                                                               | gurobipy_exceptions.GRBFileRead                                                                                                                                       |                                                                                                                                                                         |                                                       |                                        |
| FILE_WRITE               | 10013        | Failed to write the requested file                                                                                                                                                              | gurobipy_exceptions.GRBFileWrite                                                                                                                                      |                                                                                                                                                                         |                                                       |                                        |
| NUMERIC                  | 10014        | Numerical error during requested operation                                                                                                                                                      | gurobipy_exceptions.GRBNumeric                                                                                                                                        |                                                                                                                                                                         |                                                       |                                        |
| IIS_NOT_INFEASIBLE       | 10015        | Attempted to perform infeasibility analysis on a feasible model                                                                                                                                 | gurobipy_exceptions.GRBIisNotInfeasible                                                                                                                               |                                                                                                                                                                         |                                                       |                                        |
| NOT_FOR_MIP              | 10016        | Requested operation not valid for a MIP model                                                                                                                                                   | gurobipy_exceptions.GRBNotForMip                                                                                                                                      |                                                                                                                                                                         |                                                       |                                        |
| OPTIMIZATION_IN_PROGRESS | 10017        | Tried to query or modify a model while optimization was in progress                                                                                                                             | gurobipy_exceptions.GRBOptimizationInProgress                                                                                                                         |                                                                                                                                                                         |                                                       |                                        |
| DUPLICATES               | 10018        | Constraint                                                                                                                                                                                      | variable                                                                                                                                                              | or SOS contained duplicated indices                                                                                                                                     | gurobipy_exceptions.GRBDuplicates                     |                                        |
| NODEFILE                 | 10019        | Error in reading or writing a node file during MIP optimization                                                                                                                                 | gurobipy_exceptions.GRBNodefile                                                                                                                                       |                                                                                                                                                                         |                                                       |                                        |
| Q_NOT_PSD                | 10020        | Q matrix in QP model is not positive semi-definite                                                                                                                                              | gurobipy_exceptions.GRBQNotPsd                                                                                                                                        |                                                                                                                                                                         |                                                       |                                        |
| QCP_EQUALITY_CONSTRAINT  | 10021        | QCP equality constraint specified (only inequalities are supported unless the NonConvex parameter is set to 2)                                                                                  | gurobipy_exceptions.GRBQcpEqualityConstraint                                                                                                                          |                                                                                                                                                                         |                                                       |                                        |
| NETWORK                  | 10022        | Problem communicating with the Gurobi Compute Server                                                                                                                                            | gurobipy_exceptions.GRBNetwork                                                                                                                                        |                                                                                                                                                                         |                                                       |                                        |
| JOB_REJECTED             | 10023        | Gurobi Compute Server responded                                                                                                                                                                 | but was unable to process the job (typically because the queuing time exceeded the user-specified timeout or because the queue has exceeded its maximum capacity)     | gurobipy_exceptions.GRBJobRejected                                                                                                                                      |                                                       |                                        |
| NOT_SUPPORTED            | 10024        | Indicates that a Gurobi feature is not supported under your usage environment (for example                                                                                                      | some advanced features are not supported in a Compute Server environment)                                                                                             | gurobipy_exceptions.GRBNotSupported                                                                                                                                     |                                                       |                                        |
| EXCEED_2B_NONZEROS       | 10025        | Indicates that the user has called a query routine on a model with more than 2 billion non-zero entries                                                                                         | and the result would exceed the maximum size that can be returned by that query routine. The solution is typically to move to the GRBX version of that query routine. | gurobipy_exceptions.GRBExceed2bNonzeros                                                                                                                                 |                                                       |                                        |
| INVALID_PIECEWISE_OBJ    | 10026        | Piecewise-linear objectives must have certain properties (as described in the documentation for the various setPWLObj methods). This error indicates that one of those properties was violated. | gurobipy_exceptions.GRBInvalidPiecewiseObj                                                                                                                            |                                                                                                                                                                         |                                                       |                                        |
| UPDATEMODE_CHANGE        | 10027        | The UpdateMode parameter can not be modified once a model has been created.                                                                                                                     | gurobipy_exceptions.GRBUpdatemodeChange                                                                                                                               |                                                                                                                                                                         |                                                       |                                        |
| CLOUD                    | 10028        | Problems launching a Gurobi Instant Cloud job.                                                                                                                                                  | gurobipy_exceptions.GRBCloud                                                                                                                                          |                                                                                                                                                                         |                                                       |                                        |
| MODEL_MODIFICATION       | 10029        | Indicates that the user has modified the model in such a way that the model became invalid. For example                                                                                         | this happens when a general constraint exists in the model and the user deletes the resultant variable of this constraint. In such a case                             | the general constraint does not have any meaningful interpretation anymore. The solution is to also delete the general constraint when a resultant variable is deleted. | gurobipy_exceptions.GRBModelModification              |                                        |
| CSWORKER                 | 10030        | When you are using a client-server feature                                                                                                                                                      | this error indicates that there was an application problem.                                                                                                           | gurobipy_exceptions.GRBCsworker                                                                                                                                         |                                                       |                                        |
| TUNE_MODEL_TYPES         | 10031        | Indicates that tuning was invoked on a set of models                                                                                                                                            | but the models were of different types (e.g.                                                                                                                          | one an LP                                                                                                                                                               | another a MIP).                                       | gurobipy_exceptions.GRBTuneModelTypes  |
| SECURITY                 | 10032        | Indicates that an authentication step failed or that an operation was attempted for which the current credentials do not warrant permission.                                                    | gurobipy_exceptions.GRBSecurity                                                                                                                                       |                                                                                                                                                                         |                                                       |                                        |
| NOT_IN_MODEL             | 20001        | Tried to use a constraint or variable that is not in the model                                                                                                                                  | either because it was removed or because it has not yet been added.                                                                                                   | gurobipy_exceptions.GRBNotInModel                                                                                                                                       |                                                       |                                        |
| FAILED_TO_CREATE_MODEL   | 20002        | Failed to create the requested model                                                                                                                                                            | gurobipy_exceptions.GRBFailedToCreateModel                                                                                                                            |                                                                                                                                                                         |                                                       |                                        |
| INTERNAL                 | 20003        | Internal Gurobi error                                                                                                                                                                           | gurobipy_exceptions.GRBInternal                                                                                                                                       |                                                                                                                                                                         |                                                       |                                        |