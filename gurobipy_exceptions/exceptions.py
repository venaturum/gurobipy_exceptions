from gurobipy_exceptions import base


class GRBOutOfMemory(base.GurobiError):
    errno = 10001
    message = "Available memory was exhausted"


class GRBNullArgument(base.GurobiError):
    errno = 10002
    message = "NULL input value provided for a required argument"


class GRBInvalidArgument(base.GurobiError):
    errno = 10003
    message = "An invalid value was provided for a routine argument"


class GRBUnknownAttribute(base.GurobiError):
    errno = 10004
    message = "Tried to query or set an unknown attribute"


class GRBDataNotAvailable(base.GurobiError):
    errno = 10005
    message = (
        "Attempted to query or set an attribute that could not be accessed at that time"
    )


class GRBIndexOutOfRange(base.GurobiError):
    errno = 10006
    message = "Tried to query or set an attribute, but one or more of the provided indices (e.g., constraint index, variable index) was outside the range of valid values"


class GRBUnknownParameter(base.GurobiError):
    errno = 10007
    message = "Tried to query or set an unknown parameter"


class GRBValueOutOfRange(base.GurobiError):
    errno = 10008
    message = "Tried to set a parameter to a value that is outside the parameter's valid range"


class GRBNoLicense(base.GurobiError):
    errno = 10009
    message = "Failed to obtain a valid license"


class GRBSizeLimitExceeded(base.GurobiError):
    errno = 10010
    message = (
        "Attempted to solve a model that is larger than the limit for a demo license"
    )


class GRBCallback(base.GurobiError):
    errno = 10011
    message = "Problem in callback"


class GRBFileRead(base.GurobiError):
    errno = 10012
    message = "Failed to read the requested file"


class GRBFileWrite(base.GurobiError):
    errno = 10013
    message = "Failed to write the requested file"


class GRBNumeric(base.GurobiError):
    errno = 10014
    message = "Numerical error during requested operation"


class GRBIisNotInfeasible(base.GurobiError):
    errno = 10015
    message = "Attempted to perform infeasibility analysis on a feasible model"


class GRBNotForMip(base.GurobiError):
    errno = 10016
    message = "Requested operation not valid for a MIP model"


class GRBOptimizationInProgress(base.GurobiError):
    errno = 10017
    message = "Tried to query or modify a model while optimization was in progress"


class GRBDuplicates(base.GurobiError):
    errno = 10018
    message = "Constraint, variable, or SOS contained duplicated indices"


class GRBNodefile(base.GurobiError):
    errno = 10019
    message = "Error in reading or writing a node file during MIP optimization"


class GRBQNotPsd(base.GurobiError):
    errno = 10020
    message = "Q matrix in QP model is not positive semi-definite"


class GRBQcpEqualityConstraint(base.GurobiError):
    errno = 10021
    message = "QCP equality constraint specified (only inequalities are supported unless the NonConvex parameter is set to 2)"


class GRBNetwork(base.GurobiError):
    errno = 10022
    message = "Problem communicating with the Gurobi Compute Server"


class GRBJobRejected(base.GurobiError):
    errno = 10023
    message = "Gurobi Compute Server responded, but was unable to process the job (typically because the queuing time exceeded the user-specified timeout or because the queue has exceeded its maximum capacity)"


class GRBNotSupported(base.GurobiError):
    errno = 10024
    message = "Indicates that a Gurobi feature is not supported under your usage environment (for example, some advanced features are not supported in a Compute Server environment)"


class GRBExceed2bNonzeros(base.GurobiError):
    errno = 10025
    message = "Indicates that the user has called a query routine on a model with more than 2 billion non-zero entries, and the result would exceed the maximum size that can be returned by that query routine. The solution is typically to move to the GRBX version of that query routine."


class GRBInvalidPiecewiseObj(base.GurobiError):
    errno = 10026
    message = "Piecewise-linear objectives must have certain properties (as described in the documentation for the various setPWLObj methods). This error indicates that one of those properties was violated."


class GRBUpdatemodeChange(base.GurobiError):
    errno = 10027
    message = (
        "The UpdateMode parameter can not be modified once a model has been created."
    )


class GRBCloud(base.GurobiError):
    errno = 10028
    message = "Problems launching a Gurobi Instant Cloud job."


class GRBModelModification(base.GurobiError):
    errno = 10029
    message = "Indicates that the user has modified the model in such a way that the model became invalid. For example, this happens when a general constraint exists in the model and the user deletes the resultant variable of this constraint. In such a case, the general constraint does not have any meaningful interpretation anymore. The solution is to also delete the general constraint when a resultant variable is deleted."


class GRBCsworker(base.GurobiError):
    errno = 10030
    message = "When you are using a client-server feature, this error indicates that there was an application problem."


class GRBTuneModelTypes(base.GurobiError):
    errno = 10031
    message = "Indicates that tuning was invoked on a set of models, but the models were of different types (e.g., one an LP, another a MIP)."


class GRBSecurity(base.GurobiError):
    errno = 10032
    message = "Indicates that an authentication step failed or that an operation was attempted for which the current credentials do not warrant permission."


class GRBNotInModel(base.GurobiError):
    errno = 20001
    message = "Tried to use a constraint or variable that is not in the model, either because it was removed or because it has not yet been added."


class GRBFailedToCreateModel(base.GurobiError):
    errno = 20002
    message = "Failed to create the requested model"


class GRBInternal(base.GurobiError):
    errno = 20003
    message = "Internal Gurobi error"
