# Ausgleichsrechnung

Im Gegensatz zur Interpolation versuchen wir bei der Ausgleichsrechnung nicht, eine Funktion $f$ zu finden, die exakt durch sämtliche Datenpunkte geht, sondern diese nur möglichst gut approximiert.

- Gegeben sind $n$ Wertepaare ($x_i$, $y_i$) i=1, ..., n mit $x_i \neq x_j$ für $i \neq j$.
- Gesucht ist eine stetige Funktion $f : \mathbb{R} \to \mathbb{R}$, die die Wertepaare in einem gewissen Sinn bestmöglich annähert, d.h. dass möglichst genau gilt:

$$
f(x_i) \approx y_i
$$

für alle $i = 1, ..., n$


## Ansatzfunktionen

- Gegeben sei eine Menge $F$ von stetzigen **Ansatzfunktionen** $f$ auf dem Intervall $[a, b]$ sowie $n$ Wertepaare ($x_i, y_i$) für $i = i, ..., n$.

- Ein Element $f \in F$ heisst **Ausgleichsfunktion** von $F$ zu den gegebenen Wertepaaren, falls das **Fehlerfunktional**

$$
E(f) :=
\left|
\left|
y - f(x)
\right|
\right|
_{2}^{2}
=
\sum
\limits_{i=1}^n (y_i - f(x_i))^2
$$
für $f$ minimal wird, d.h. $E(f) = min{E(g) | g \in F}$.

- Man nennt das gefundenen $f$ dann optimal im Sinne der **kleinsten Fehlerquadrate** (least squares fit).

## Lineare Ausgleichsprobleme

```python
# Sample data points
x = [1, 2, 3, 4, 5]
y = [2, 1, 3, 2, 4]

# Calculate the coefficients (slope and intercept) of the best-fit line
n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xx = sum(x_i**2 for x_i in x)
sum_xy = sum(x[i] * y[i] for i in range(n))

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
intercept = (sum_y - slope * sum_x) / n

# Evaluate the best-fit line at a specific point
x_new = 2.5
y_new = slope * x_new + intercept

print("Interpolated value at x =", x_new, "is y =", y_new)
```



## Gauss Newton mit QR ohne Dämfpung

```python

import numpy as np

def gauss_newton_no_damping(J, r, x0, max_iter=100, tol=1e-6):
    x = x0
    for i in range(max_iter):
        Jx = J(x)
        rx = r(x)
        Q, R = np.linalg.qr(Jx)
        delta = np.linalg.lstsq(R, -rx, rcond=None)[0]
        x += delta
        if np.linalg.norm(delta) < tol:
            break
    return x

# Beispielanwendung
def J(x):
    # Jacobimatrix
    n = len(observed_x_values)
    Jx = np.zeros((n, 3))  # 3 ist die Anzahl der Parameter (a, b, c)
    Jx[:, 0] = observed_x_values ** 2  # Ableitung nach dem Parameter a
    Jx[:, 1] = observed_x_values  # Ableitung nach dem Parameter b
    Jx[:, 2] = 1  # Ableitung nach dem Parameter c
    return Jx

def r(x):
    # Residuenvektor
    a, b, c = x
    return a * observed_x_values ** 2 + b * observed_x_values + c - observed_y_values

observed_x_values = np.array([0., 1., 2.])
observed_y_values = np.array([1., 2., 8.])

x0 = np.array([1.0, 1.0, 1.0])  # Anfangswert für die Parameter a, b, c
result = gauss_newton_no_damping(J, r, x0)

print("Ergebnis:", result)
```