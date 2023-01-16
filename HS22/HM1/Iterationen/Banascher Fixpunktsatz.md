$$
\left|
F(x) - F(y)
\right|
\le
\alpha
\cdot
\left|
x - y
\right|
$$
$$
I =[a, b]
$$
## Monoton steigend
Wenn die Funktion in einem Intervall $I$ steigend ist
$$
F(a) > a \text{ und }F(b)< b
$$

## Monton fallend
$$
F(a) < a \text{ und }F(b) > b
$$


# Fehlerabschätzung

## A-Priori
$$
\left|
x_n
-
\overline{x}
\right|
\le
\frac{
\alpha^n
}{
1 - \alpha
}
\cdot
\left|
x_1 - x_0
\right|
$$

## A-Posteriori
$$
\left|
x_n
-
\overline{x}
\right|
\le
\frac{
\alpha^n
}{
1 - \alpha
}
\cdot
\left|
x_n- x_{n-1}
\right|
$$

**Es folgt**
$$

\frac{
\left|
F(x) - F(y)
\right|
}{
\left|
x -y
\right|
}
\le
\alpha
$$

$$
\alpha = max_{x0 \in [a,b]}|F'(x_0)|
$$

```python
import numpy as np
import sympy as sp

# Intervalbereich
a = 0.5
b = 1.5

# Startwet
x0 = 1.5 

f = "1/2 * 2 ** x"

# Create Sympy Equations
f = sp.sympify(f)
x = sp.symbols('x')
df = sp.diff(f, x) # Ableitung erstellen

print("F(x) - F(y) | <= alpha * | x - y|")

print(f"F({a}) = {f.evalf(subs={'x': a})}" ,"F(0.5) > 0.5")
print (f"F({b}) = {f.evalf(subs={'x': a})}", "F(1.5) < 1.5")

print ("Daraus folgt, dass die Funktion nur in diesem Bereich ist")
print ("F: I -> I")

print (f"F'(x) = {df}")

# F' = ln(2) * 2^(x-1)
# alpha = max | F'(x) | = max
# Wir wissen ja, dass 1.5 kleiner als 1.5 ist, also sollte  F'(1.5) < 1.5 sein

y_at_x0 = df.evalf(subs={'x': x0})

print (f"F'(x) = {y_at_x0}")
```