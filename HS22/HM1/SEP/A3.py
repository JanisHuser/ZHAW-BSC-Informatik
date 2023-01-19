from numbers import Number
import numpy as np
import sympy as sp

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
    
    def abbruch(x):
        a = expr.evalf(subs={'x': x - tolerance})
        b = expr.evalf(subs={'x': x + tolerance})
        
        return not (a*b) <= 0
    
    while abbruch(x[i-1]):
        xn = x[i-1] - expr.evalf(subs={'x': x[i-1]})
        x.append(xn)
        err = np.abs(x[i] - x[i-1])
        if log:
            print (f"{i}\t {x[i]},\t{err}")
        
        i += 1
    
    return x

def a():
	print ("Teil a")
	import numpy as np

	def f(x):
		return (np.exp(x)+np.exp(-x))/2-x-2

	x0 = 0.
	x1 = 0.5
	epsilon = 10**(-7)
	x = calc_sekante(f, x0, x1, epsilon, False)
	xr = x[len(x)-1]
	print ("Teil b")
	print(f"Approximativer Wert: {round(xr, 5)}")

	
def do_plot():

	print ("Plot")
	import sympy as sp
	from sympy.plotting import plot

	f = "(exp(x) + exp(-x))/2-x-2"

	# Create Sympy Equations
	f = sp.sympify(f)
	x = sp.symbols('x')

	plot(f)

def b():
	import numpy as np   
	print ("Teil b")
	f = "(exp(x) + exp(-x))/2-x-2"
	x0 = 0
	eps = 10**(-7)
	x = calc_newton_with_tolerance(f, x0, eps, False)

	print ("================")
	print (f"Resultat: {round(x[len(x)-1], 5)}")

print ("Aufgabe 3")
do_plot()
a()
print()
b()