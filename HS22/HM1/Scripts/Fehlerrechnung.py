
from numbers import Number
import sympy as sp
import numpy as np

def calc_err_abs(x, xr):
    '''
    Berechnet den absoluten Fehler von x und xr
    x: Korrektes Ergebnis
    xr: Fehlerhaftes Ergebnis
    '''
    return abs(xr - x)

    
def calc_err_rel(x, xr):
    '''
    Berechnet den relativen Fehler von x und xr
    x: Korrektes Ergebnis
    xr: Fehlerhaftes Ergebnis
    '''
    return abs((xr - x) / x)



def calc_cond(f: str, log: bool = True):
    '''
    Berechnet die Konditionszahl der Funktion f
    
    f: Funktion als String
    log: False wenn keine Schritte ausgegeben werden sollen
    Returns: evaluated string
    '''
    
    x = sp.symbols('x')
    
    fa = sp.diff (f, x)
    if log:
        print (f"f(x) = {f}")
        print (f"f'(x) = {fa}")
        
    eq = f"({str(fa)} *x)/({f})"
    
    if log:
        print (f"k(x) = {eq}")
        
    return sp.sympify(eq)

    
    
def calc_convergence(x, xq):
    '''
    Berechnet die Konvergenz einer Reihe x zu xq
    '''
    n = len(x)
    
    cs = np.zeros(n)
    
    print ("i\txi\t|xi - xq|")
    for i in range(n):
        c = abs(x[i] - xq)
        cs[i] = c
        print (f"{i}\t{round(x[i],5)}\t{round(x[i],c)}")
        
        
    return cs