
def calc_err_abs(x, xr):
    return abs(xr - x)

    
def calc_err_rel(x, xr):
    return abs((xr - x) / x)