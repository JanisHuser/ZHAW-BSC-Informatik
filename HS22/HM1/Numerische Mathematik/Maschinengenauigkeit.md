## Abschätzung
Beim Runden einer reellen Zahl $x$ auf eine Maschinenzahl $\tilde{x}$ mit n-stelliger Mantisse zur Basis B gilt für den relativen Rundungsfehler folgene Abschätzung:

$$
\left|
\frac{\tilde{x}-x}{x} 
\right|

\leq

\frac{B}{2}
\cdot
B^{-n}
$$

## Obere Schranke
Auch Maschinengenauigkeit oder Maschinenepsilon genannt

$$
eps =
\frac{1}{2}
\cdot
B^{1-n}
$$

```python
from Scripts.Maschinengenauigkeit import calc_eps

B = 2 # Basis
n = 8 # Mantissenlänge

print (f"Relativer Fehler <= {calc_eps(B, n)}")
```

# Fehlerfortpflanzung


## Bei Addition
```python
from Scripts.Maschinengenauigkeit import add
from Scripts.Fehlerrechnung import calc_err_rel, calc_err_abs

a = 1350
b = 245
prec = 2

xr = add(a, b, prec)
x = a + b

rel_err = calc_err_rel(x, xr)
abs_err = calc_err_abs(x, xr)

print (f"Rel. Fehler {rel_err}")
print (f"Abs. Fehler {abs_err}")
```

## Bei Multiplikation

```python
from Scripts.Maschinengenauigkeit import multiply
from Scripts.Fehlerrechnung import calc_err_rel, calc_err_abs

a = 1350
b = 245
prec = 2

xr = multiply(a, b, prec)
x = a * b

rel_err = calc_err_rel(x, xr)
abs_err = calc_err_abs(x, xr)

print (f"Rel. Fehler {rel_err}")
print (f"Abs. Fehler {abs_err}")
```
