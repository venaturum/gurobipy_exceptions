import gurobipy as gp

from gurobipy_exceptions.exceptions import *

_codes_to_errors = {
    10001: GRBOutOfMemory,
    10002: GRBNullArgument,
    10003: GRBInvalidArgument,
    10004: GRBUnknownAttribute,
    10005: GRBDataNotAvailable,
    10006: GRBIndexOutOfRange,
    10007: GRBUnknownParameter,
    10008: GRBValueOutOfRange,
    10009: GRBNoLicense,
    10010: GRBSizeLimitExceeded,
    10011: GRBCallback,
    10012: GRBFileRead,
    10013: GRBFileWrite,
    10014: GRBNumeric,
    10015: GRBIisNotInfeasible,
    10016: GRBNotForMip,
    10017: GRBOptimizationInProgress,
    10018: GRBDuplicates,
    10019: GRBNodefile,
    10020: GRBQNotPsd,
    10021: GRBQcpEqualityConstraint,
    10022: GRBNetwork,
    10023: GRBJobRejected,
    10024: GRBNotSupported,
    10025: GRBExceed2bNonzeros,
    10026: GRBInvalidPiecewiseObj,
    10027: GRBUpdatemodeChange,
    10028: GRBCloud,
    10029: GRBModelModification,
    10030: GRBCsworker,
    10031: GRBTuneModelTypes,
    10032: GRBSecurity,
    20001: GRBNotInModel,
    20002: GRBFailedToCreateModel,
    20003: GRBInternal,
}


def convert_error(original_error):
    if isinstance(original_error, gp.GurobiError):
        raise _codes_to_errors.get(original_error.errno, original_error)
    raise original_error


def patch_error_message(error):
    if (
        isinstance(error, gp.GurobiError)
        and error.errno in _codes_to_errors
        and error.message == ""
    ):
        error._set_message(_codes_to_errors[error.errno].message)
    raise error
