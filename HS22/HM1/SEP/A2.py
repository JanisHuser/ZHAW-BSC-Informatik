
from Scripts.Fehlerrechnung import calc_cond
import numpy as np

from Scripts.Maschinengenauigkeit import Scientific

def K(x):
    return np.abs((2*np.sin(x)+x*np.cos(x))/np.sin(x))

def a_2a():
	f = "x**2 * sin(x)" # Funktion

	print ("2a")
	print (f"Konditionszahl k(x) = {calc_cond(f)}")
	# Resultat = K(x) = x/tan(x) + 2

def a_2b():
	print ("2b")
	
	print ("|(f(x) - f(x0))/f(x0)| = K(x0)*|(x-x0)/x0|")
	print ("nach abs err (x0 -x) umstellen")
	print ("|(f(x) - f(x0))/f(x0)| / K(x0) = |(x-x0)|/|x0|")
	print("|(f(x) - f(x0))/f(x0)| / K(x0) * |x0| = |x -x0|")

	print ("0.1 / K(x0) * x0 = |x-x0|")



	x0 = np.pi/3

	print (round(0.1/ K(x0) * x0,4))

	# Resultat = 0.0405


def a_2c():
	x0 = np.pi / 3


	def f(x):
		return x**2 * np.sin(x)


	for n in range(1, 10):
		print (round(K(10**-n),5))

a_2a()
a_2b()
a_2c()