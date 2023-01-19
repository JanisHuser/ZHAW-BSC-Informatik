import numpy as np
import sympy as sp

def calc_cond(f: str, df: str="", log: bool = True):
    '''
    Berechnet die Konditionszahl der Funktion f
    
    f: Funktion als String
    log: False wenn keine Schritte ausgegeben werden sollen
    Returns: evaluated string
    '''
    
    x = sp.symbols('x')
    if len(df) == 0:
        df = sp.diff(f, x)
    if log:
        print (f"f(x) = {f}")
        print (f"f'(x) = {df}")
        
    eq = f"(({str(df)}) *x)/({f})"
    
    if log:
        print (f"k(x) = {eq}")
    
    return sp.simplify(eq)


def a():
    print ("Teil a")
    
    abs_err = 0.1
    x0 = 3
    
    f = "x / ln(x)"
    df = "(ln(x) - 1)/((ln(x))**2)"
    
    cond = calc_cond(f, df, True)
    print (f"Konditionszahl k(x) = {cond}")
    k = sp.sympify(cond)
    x = sp.symbols('x')
    
    print ("Relativer Fehler f(x0)")
    print (f"k(x0) = k({x0})", round(k.evalf(subs={'x': x0}),5))

def b():
    
    import matplotlib.pyplot as plot
    
    print ("Teil b")
    def k(x):
        return 1 - 1/np.log(x)
    
    # Display grid
    x = np.arange(0. ,10., 0.1)
    plot.grid(True, which="both")
    # Linear X axis, Logarithmic Y axis
    
    plot.semilogx(x, k(x) )
    plot.xlim([0,10])
    
    
    # K(x) <= 1 für x > b
    # K(X) > 1 für x < b
print ("AUFGABE 2")
a()
b()