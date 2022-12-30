Möglichst exakte und möglichst effiziente Zahlenmässiges Lösen einer mathematischen Problemstellung auf Rechner mit endlicher Gleitpunktarithmetik.


```python
import numpy as np
import matplotlib.pyplot as plt

SHOW_VALUES = False

# Definiere Funktionen hier
def f(x):
    y = x**2 + x - 4
    return y

def g(x):
    y = 2**x + x - 4
    return y

xrange = np.arange(-3, 3, 0.1) # 0.1 -> Schrittgrösse
fvector = f(xrange)
gvector = g(xrange)

plt.figure(1)
plt.plot(xrange, fvector, marker='.', linestyle='', color='red', label='f(x)')
plt.plot(xrange, gvector, marker='.', linestyle='', color='blue', label='g(x)')
plt.grid()
plt.legend()


if SHOW_VALUES is True:
    print ("x\tf(x)\tg(x)")
    for i in range(0, len(xrange), 1):
        x = round(xrange[i], 4)
        f = round(fvector[i], 4)
        g = round(fvector[i], 4)
        print(f"{x}\t{f}\t{g}")
```

## Berechnen von Nullstellen
1. Wähle Intervall $[x_L,x_R ]$ mit $Y_L = g(x_L) < 0$ und $Y_R = g(x_R) > 0$
2. Bilde Intervallmitte $x_M = \frac{x_L+x_R}{2}$
3. Bilde $Y_m = g(x_M)$
4. 1. Wenn $Y_M < 0$ ist, ersetze $x_L$ durch $x_M$ und erhalte so neues kleineres Intervall $[x_M, x_R]$
4. 2. Wenn $Y_M > 0$ ist, ersetze $X_R$ durch $x_M$ und erhalte Intervall $[x_L, x_M]$
5. Wiederhole 2,3 und 4

```python
from Scripts.Intervallhalbierung import calc_iterative

def g(x):
    y = 2**x + x -4
    return y

# Intervall
xL = 1.0
xR = 2.0
tol = 1e-4

n, xL, xR = calc_iterative(
    g, xL, xR, tol, True)

print (f"n = {n}")
print (f"xL = {xL}")
print (f"xR = {xR}")
```

## Universeller Nullstellenbestimmer
Auch RootFinder genannt

```python
import scipy.optimize

def g(x):
    y = 2**x + x -4
    return y

solution = scipy.optimize.root(g, 1.5)
print(f"x* ={solution.x}")
```

