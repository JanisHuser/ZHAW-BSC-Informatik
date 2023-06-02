# Tangentengleichung

## Verallgemeinerter Tangentengleichung

Es gilt: $f(x) \approx g(x)$ 

$$
g(x)
=
f(x^{(0)})
+
Df(x^{(0)})
\cdot
(x - x^{(0)})
$$

## Spezialfall $f: \mathbb{R}^2 \to \mathbb{R}$ 

## Python
```python
import sympy as sp

x0_values = [1, 0 ,1]

# Variablen definieren
x1, x2, x3 = sp.symbols('x1, x2, x3')

# Aus einzelnen Variablen eine Matrix machen
x = sp.Matrix([x1, x2, x3])

# Gegebene Werte befüllen
x0 = sp.Matrix(x0_values)

# Skalare Terme erzeugen
f1 = x1 * sp.cos(x2) + x3
f2 = x1**2 + sp.sin(x2)*x3**3

# Aus Termen eine Matrix machen
f = sp.Matrix([f1, f2])

# Terme zahlenmässig auswerten
fx0 = f.subs([
    (x1, x0_values[0]),
    (x2, x0_values[1]),
    (x3, x0_values[2])
])

# Jacobi Matrix bilden
Df = f.jacobian(x)

# Jacobi Matrix zahlenmässig auswerten
Dfx0 = Df.subs([
    (x1, x0_values[0]),
    (x2, x0_values[1]),
    (x3, x0_values[2])
])

# Linearisierung von f an Stelle x0 bilden
g = fx0 + Dfx0@(x- x0)

# Skalare Komponenten der Linearisierung herausnehmen
g1 = g[0, 0]
g1_value = g1.subs([
    (x1, x0_values[0]),
    (x2, x0_values[1]),
    (x3, x0_values[2])
])

g2 = g[1, 0]
g2_value = g2.subs([
    (x1, x0_values[0]),
    (x2, x0_values[1]),
    (x3, x0_values[2])
])

print ("Das Resultat lautet (Matrixförmig)")
print (g1)
print (g2)

```

# Mehrdimensionales Newtonverfahren
$$
f:
\mathbb{R}
\to
\mathbb{R}^2
$
$$
$$
x
=
\begin{bmatrix}
x1 \\
x2
\end{bmatrix}
\to
f(x)=
\begin{bmatrix}
f1(x_1, x_2) \\
f2(x_1, x_2)
\end{bmatrix}
=
\begin{bmatrix}
x_1^2 + x_2 - 11 \\
x_1 + x_2^2 - 7
\end{bmatrix}
$$

## Python

```python
import sympy as sp

# Variablen in Funktion definieren
x1, x2 = sp.symbols('x1, x2')

# Funktionen definieren
f1 = x1**2 + x2 - 11
f2 = x1 + x2**2 - 7

f = sp.Matrix([
    [f1],
    [f2]
])

def f_at(x):
    
    return f.subs([
        (x1, x[0]),
        (x2, x[1])
    ])

# x0 definieren
x0 = sp.Matrix([
    [1.],
    [1.]
])

# Partielle Ableitungsmatrix erstellen
Df = sp.Matrix([
    [sp.diff(f1, x1), sp.diff(f1, x2)],
    [sp.diff(f2, x1), sp.diff(f2, x2)]
])

print ("Df = \n", Df)

#x0 in Df einsetzen
def Df_at(x):
    Df_at = Df.subs([
        (x1, x[0, 0]),
        (x2, x[1, 0])
    ])
    
    return Df_at


# Newtonverfahren
x = [ x0 ]

# Nullstelle von f
xstar = sp.Matrix([
    [3],
    [2]
])

# Anzahl Iterationsschritte
print ("Newtonverfahren")
for i in range(1, 5):
    x_prev = x[i-1]
    Df_prev = Df_at(x_prev)
    
    Df_inv = Df_prev.inv()
    
    f_at_xi = f_at(x_prev)
    xi = x_prev - Df_inv @ f_at_xi
    x.append(xi)
    

    print ('----------------------------------------')
    
    print (f"i = {i}")
    print ("xi = \n", xi)
    print (f"Fehler ||xi - xstar || = {(xi - xstar).norm(2)}")
```

## Newtonverfahren mit Dämpfung
```python
import numpy as np
import sympy as sp

x1, x2 = sp.symbols('x1, x2')
x = sp.Matrix([x1, x2])

f1 = x1**2 + x2 - 11
f2 = x1 + x2**2 - 7

f = sp.Matrix([f1, f2])

Df = f.jacobian(x)

f = sp.lambdify([ [[x1],[x2]] ], f, 'numpy')
Df = sp.lambdify([ [[x1],[x2]] ], Df, 'numpy')

x0 = np.array([[1.],[1.]])
print ('x0 =', x0)
print ('|| f(x0) || = ', np.linalg.norm(f(x0), 2))

imax = 5
for i in range(1, imax+1):
    delta0 = np.linalg.solve(Df(x0), -f(x0))
    
    kmax = 4
    k = 0
    while (k <= kmax) and (np.linalg.norm(f(x0 + delta0/2**k),2) >=
                          np.linalg.norm(f(x0), 2)):
        k = k +1 
    
    if k == kmax + 1:
        k = 0
        
    x1 = x0 + delta0 / 2**k
    
    print ('------------------------------------')
    print ('Iteration i =', i)
    print ('Dämpfung k =', k)
    print ('xi =', x1)
    
    print ('|| f(xi) || =', np.linalg.norm(f(x1), 2))
    
    x0 = x1
```

## Jacobi Matrix

$$
Df =
\begin{bmatrix}
\frac{\partial f1}{x1} \frac{\partial f1}{x2} \frac{\partial f1}{x3} \\
\frac{\partial f2}{x1} \frac{\partial f2}{x2} \frac{\partial f2}{x3} \\
\frac{\partial f3}{x1} \frac{\partial f3}{x2} \frac{\partial f3}{x3}
\end{bmatrix}
$$
```python
# Manueller Weg
Df = sp.Matrix([
    [sp.diff(f1, x1), sp.diff(f1, x2)],
    [sp.diff(f2, x1), sp.diff(f2, x2)]
])
```

```python
f = sp.Matrix([f1, f2])
x = sp.Matrix([x1, x2])

Df = f.jacobian(x
			   )
```