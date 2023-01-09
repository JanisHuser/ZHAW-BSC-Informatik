from Scripts.Maschinengenauigkeit import Scientific, calc_eps

b = 2 # Basis
e = 3 # Anzahl Stellen im Exponent
n = 5 # Stellen der Mantisse

max_exp = 0
for i in range(e):
    max_exp += b**i

min_exp = -1*max_exp

print ("1a")
print (f"Kleinster Exponent: {min_exp}")
print (f"Grösster Exponent: {max_exp}")

x_min = Scientific(b ** (min_exp-1), 4)
x_max = Scientific((1-b **-n) * b ** max_exp, 4)

print("1b")
print (f"Kleinste darstellbare Zahl: {x_min.get_value()}")
print (f"Grösste darstellbare Zahl: {x_max.get_value()}")


print ("1c")
print (f"eps 2: {calc_eps(2, 5)}")
print (f"eps hex: {calc_eps(16, 2)}")