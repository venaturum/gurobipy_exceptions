import gurobipy as gp


class GurobiError(gp.GurobiError):

    errno = -1
    message = ""

    def __init__(self):
        super().__init__(self.errno, self.message)
