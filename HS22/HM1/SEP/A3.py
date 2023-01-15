print ("3a")

from Scripts.Iterationen import calc_newton_with_tolerance

f = "exp(x) - (sqrt(2) +2)"

x0 = 0.5
eps = 10**(-7)
x = calc_newton_with_tolerance(f, x0, eps, True)

print ("================")
print (f"Resultat: {x[len(x)-1]}")

def three():
	print("3b")

	import sympy as sp
	import numpy as np

	from sympy.abc import x

	a1 = sp.exp(x) - (sp.sqrt(2) +2)
	a2 = sp.ln(sp.sqrt(x) + 2)


	print ("1. Gleiche Funktion", a1.equals(a1))

	f = sp.sympify(a2)
	a = 0.5
	b = 1.5

	print ("2. ")
	print("a", f.evalf(subs={x: a}))
	print("b", f.evalf(subs={x: b}))


	from Scripts.LinalgHelpers import calc_a_priori_iteration


	print ("4. A priori")
	x = sp.symbols('x')
	df = sp.diff (f, x)

	print(df)



three()