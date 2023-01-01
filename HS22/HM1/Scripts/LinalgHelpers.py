import numpy as np 

def calc_a_priori_iteration(B, x0, x1, tol):
    '''
    Estimates the iterations to reach tolerance
    B
    x0
    x1
    tol
    '''
    B_norm = np.linalg.norm(B, np.inf)
    x_norm = np.linalg.norm(x1 - x0, np.inf)

    n = np.log(((1 - B_norm) / x_norm) * tol) / np.log(B_norm)

    return n
    
    
def calc_a_posteriori_error(B, x, xn):
    '''
    Mittels a-posteriori die Fehlerabschätzung
    von x und x+1 berechnen
    B
    x
    xn
    '''
    B_norm = np.linalg.norm(B, np.inf)
    x_norm = np.linalg.norm(xn - x, np.inf)

    err = (B_norm / (1 - B_norm)) * x_norm

    return err
    
    
