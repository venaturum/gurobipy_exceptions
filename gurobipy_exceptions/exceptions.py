from gurobipy_exceptions import base


class GRBOutOfMemory(base.GurobiError):
    errno = 10001
    message = "Available memory was exhausted."


class GRBNullArgument(base.GurobiError):
    errno = 10002
    message = "NULL input value provided for a required argument."


class GRBInvalidArgument(base.GurobiError):
    errno = 10003
    message = "An invalid value was provided for a routine argument."


class GRBUnknownAttribute(base.GurobiError):
    errno = 10004
    message = "Tried to query or set an unknown attribute."


class GRBDataNotAvailable(base.GurobiError):
    errno = 10005
    message = "Attempted to query or set an attribute that could not be accessed at that time."


class GRBIndexOutOfRange(base.GurobiError):
    errno = 10006
    message = "Tried to query or set an attribute but one or more of the provided indices is invalid."


class GRBUnknownParameter(base.GurobiError):
    errno = 10007
    message = "Tried to query or set an unknown parameter."


class GRBValueOutOfRange(base.GurobiError):
    errno = 10008
    message = "Tried to set a parameter to a value that is outside the parameter's valid range."


class GRBNoLicense(base.GurobiError):
    errno = 10009
    message = "Failed to obtain a valid license."


class GRBSizeLimitExceeded(base.GurobiError):
    errno = 10010
    message = (
        "Attempted to solve a model that is larger than the limit for a demo license."
    )


class GRBCallback(base.GurobiError):
    errno = 10011
    message = "Problem in callback."


class GRBFileRead(base.GurobiError):
    errno = 10012
    message = "Failed to read the requested file."


class GRBFileWrite(base.GurobiError):
    errno = 10013
    message = "Failed to write the requested file."


class GRBNumeric(base.GurobiError):
    errno = 10014
    message = "Numerical error during requested operation."


class GRBIisNotInfeasible(base.GurobiError):
    errno = 10015
    message = "Attempted to perform infeasibility analysis on a feasible model."


class GRBNotForMip(base.GurobiError):
    errno = 10016
    message = "Requested operation not valid for a MIP model."


class GRBOptimizationInProgress(base.GurobiError):
    errno = 10017
    message = "Tried to query or modify a model while optimization was in progress."


class GRBDuplicates(base.GurobiError):
    errno = 10018
    message = "Constraint, variable, or SOS contained duplicated indices."


class GRBNodefile(base.GurobiError):
    errno = 10019
    message = "Error in reading or writing a node file during MIP optimization."


class GRBQNotPsd(base.GurobiError):
    errno = 10020
    message = "Q matrix in QP model is not positive semi-definite."


class GRBQcpEqualityConstraint(base.GurobiError):
    errno = 10021
    message = "QCP equality constraint specified (only inequalities are supported unless the NonConvex parameter is set to 2)"


class GRBNetwork(base.GurobiError):
    errno = 10022
    message = "Problem communicating with the Gurobi Compute Server."


class GRBJobRejected(base.GurobiError):
    errno = 10023
    message = "Gurobi Compute Server responded but was unable to process the job."


class GRBNotSupported(base.GurobiError):
    errno = 10024
    message = "A Gurobi feature is not supported under your usage environment."


class GRBExceed2bNonzeros(base.GurobiError):
    errno = 10025
    message = "A query routine has been called on a model with more than 2 billion non-zero entries."


class GRBInvalidPiecewiseObj(base.GurobiError):
    errno = 10026
    message = "Violated property for Piecewise-linear objective."


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
    message = "The model has been modified and now is invalid."


class GRBCsworker(base.GurobiError):
    errno = 10030
    message = "That there was an application problem client-server feature."


class GRBTuneModelTypes(base.GurobiError):
    errno = 10031
    message = "Tuning was invoked on a set of models but the models were of different types (e.g. one an LP another a MIP)."


class GRBSecurity(base.GurobiError):
    errno = 10032
    message = (
        "Authentication step failed or current credentials for attempted operation."
    )


class GRBNotInModel(base.GurobiError):
    errno = 20001
    message = (
        "Constraint or variable not in the model (either removed or not yet been added."
    )


class GRBFailedToCreateModel(base.GurobiError):
    errno = 20002
    message = "Failed to create the requested model."


class GRBInternal(base.GurobiError):
    errno = 20003
    message = "Internal Gurobi error."
