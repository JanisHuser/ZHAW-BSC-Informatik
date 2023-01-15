import sympy as sp
import numpy as np
from numbers import Number



def calc_a_priori_iteration(f: str, x0: Number, a: Number, tolerance: Number):
    '''
    Berechnet a priori abschätzung einer Funktion
    f: Funktion als String
    x0: Anfangswert
    a: needed to get L, usualy start of range
    tolerance: Toleranz
    return n: Anzahl Iterationen
    '''
    
    f = sp.sympify(f)
    x = sp.symbols('x')
    df = sp.diff (f, x)
    
    x1 = f.evalf(subs={'x': x0})
    
    L = np.float64(df.evalf(subs={'x': a}))

    n = np.log(np.float64(tolerance * (1 - L)/ np.abs(x1 - x0))) / np.log(np.float64(L))
    
    return n
