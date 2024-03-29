from numbers import Number
import numpy as np
import sympy as sp



def calc_fixpunkt(F, x0: Number, n: Number, log: bool = True):
    '''
    Fuehrt eine Fixpunktiteration durch
    F: Funktion
    x0: Startwert
    n: Anzahl Iterationen
    '''
    
    x = np.zeros(n+1)
    x[0] = x0
    
    if log:
        print (f"x\t F(x)")
        print (f"x{0}\t {x0}")
        
    for i in range(1, n+1):
        x[i] = F(x[i-1])
        
        if log:
            print (f"x{i}\t {x[i]}")
        
    return x
    
def calc_fixpunkt_with_tolerance(F,
    x0: Number,
    xq: Number,
    tolerance: Number, log: bool = True):
    '''
    Fuehrt eine Fixpunktiteration solange x - xq > tolerance durch
    F: Funktion
    x0: Startwert
    xq: xQuer
    n: Anzahl Iterationen
    '''
    i = 0
    x = [x0]
    
    f = sp.sympify(f)
    
    if log:
         print (f"i\t F(x)")
         print (f"{0}\t {x[i]}")
    
    while np.abs(x[i] - xq > tolerance):
        x.append(F(x))
        
        if log:
            print (f"{i}\t {x[i]}")
        
        i += 1
    return x

    
def calc_sekante(f, x0, x1, epsilon, log: bool = True):
    '''
    Iteriert nach dem sekanten Verfahren
    x0: Number
    x1: Number
    epsilon: Fehler
    '''
    
    x = [x0, x1]
    x.append(x1 - f(x1)/(x1+x0))
    i = 2
    
    if log:
         print (f"i\t F(x)")
         print (f"{0}\t {x[0]}")
         print (f"{1}\t {x[1]}")
    
    while f(x[i] - epsilon) * f(x[i] + epsilon) >= 0:
        
        xn_1 = x[i-1]
        xn_2 = x[i-2]
        
        xn = xn_1 - f(xn_1) / (xn_1+ xn_2)
        
        if log:
            print (f"{i}\t {xn}")
        
            
        i += 1
            
        x.append(xn)
        
    return x  

def do_newton_step(f: str, x_last: Number):
    '''
    Berechnet einen Schritt des Newtonverfahren
    f: Funktion
    x0: Startwert
    n: Anzahl Iterationen
    Returns: x nach n Iterationen
    '''
    f = sp.sympify(f)
    x = sp.symbols('x')
    df = sp.diff (f, x)
    
    expr = f / df
    
    xn = expr.evalf(subs={'x': x_last})
    
    return x_last - xn
    
def calc_newton(f: str, x0: Number, n: Number, log: bool = True):
    '''
    Berechnet das Newtonverfahren
    f: Funktion
    x0: Startwert
    n: Anzahl Iterationen
    Returns: x nach n Iterationen
    '''
    f = sp.sympify(f)
    x = sp.symbols('x')
    df = sp.diff (f, x)
    
    i = 0
    x = np.zeros(n+1)
    x[0] = x0
    
    if log:
        print (f"i\t F(x)")
        print (f"{0}\t {x[0]}")
    expr = f / df
    for i in range(1, n+1):
        xn = expr.evalf(subs={'x': x[i-1]})
        
        x[i] = x[i-1] - xn
        if log:
            print (f"{i}\t {x[i]}")
            
    return x
    
    
    
def calc_newton_with_tolerance(f: str, x0: Number, tolerance: Number, log: bool = True):
    '''
    Berechnet das Newtonverfahren
    f: Funktion
    x0: Startwert
    tolerance: Wird solange wiederholt, bis err < tolerance
    Returns: x
    '''
    f = sp.sympify(f)
    x = sp.symbols('x')
    df = sp.diff (f, x)
    i = 0
    x = [x0]
    err = np.inf
    
    if log:
        print (f"i\t F(x)\tErr")
        print (f"{0}\t {x[0]}, np.inf")
        
    expr = f / df
    
    i = 1
    while err > tolerance:
        xn = x[i-1] - expr.evalf(subs={'x': x[i-1]})
        x.append(xn)
        err = np.abs(x[i] - x[i-1])
        if log:
            print (f"{i}\t {x[i]},\t{err}")
        
        i += 1
    
    return x