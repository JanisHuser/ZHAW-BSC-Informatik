## Skalarwertige Funktionen mit mehreren Variablen

- Eine Funktion mit  $$ unabhängigen Variablen  $_1, …, x_\) und einer abhängigen Variablen  $$ versteht man eine Vorschrift, die jedem geordneten Zahlentupel ( $_1, x_2, …, x_\)) aus einer Definitionsmenge  $ \in \mathbb{R}^\) genau ein Element  $$ aus einer Wertemenge  $mathbb{W} \in \mathbb{R}$ zuordnet.
Symbolische Schreibweise:

$$
f: \mathbb{D} \in \mathbb{R}^n \rightarrow \mathbb{W} \mathbb{R}
$$
$$
(x_1,x_2,…,x_n) \mapsto y = f(x_1, x_2, …, x_n)
$$
- Da das Ergebnis  $ \in \mathbb{R}$ ein Skalar (eine Zahl) ist, redet man von einer **skalarwertigen** Funktion.

## Partielle Ableitung
$$
z = f(x,y) = x^5 + x^7
$$
### Beispiel

Gegen ist die folgende Funktion:  $(x,y) = x^5 + y^\). Soll diese nach x abgeleitet werden, dann entsteht nachstehendes. Da y als Zahl angesehen wird, fällt dieses weg.
$$
\frac{
\partial f(x,y)
}{
\partial x
}
=
5x^4
$$

### Definition
Für eine Funktion  $: \mathbb{R} \rightarrow \mathbb{R}$ mit einer Variablen ist die Ableitung an der Stelle  $_\) bekanntlich definiert als:
$$
f’(x_0) = \lim\limits_{\Delta x \rightarrow 0}
\frac{
f(x_0 + \Delta x) - f(x_0)
}{
\Delta x
}
$$
Aus geometrischer Sicht entspricht dies der Steigung  $ = f‘(x_0)$ der im Punkt $(x_0, f(x_0))$ angelegten Kurventangente
$$
t(x) = f(x_0) + f‘(x_0)(x- x_0)
$$
### Python
```python
from sympy import symbols, diff

# Variablen in Funktion definieren
x, y = symbols('x y', real=True)

# Funktion definieren
f = x**5 + x**7

print(diff(f, x))
```


## An einer Stelle

$$
\frac{\partial f}{\partial x}
(x, y)
=
x^2 - x\cdot y^2 + \frac{1}{2} \cdot y^3 + 10
$$

```python
from sympy import symbols, diff

# Variablen in Funktion definieren
x, y = symbols('x y', real=True)

# Funktion definieren
f = x**2 -x * y**2 + 1/2. * y**3 + 10

# Partielle ableitungen berechnen
df_x = diff(f, x)
df_y = diff(f, y)

# An einer Stelle (-1, 1)
print ("Partielle Ableitung nach x:", df_x)
print ("Partielle Ableitung nach y:", df_y)

x0 = -1
y0 = 1
df_x_eval = df_x.subs([
    (x, x0),
    (y, y0)
])
    
df_y_eval = df_y.subs([
   (x, x0),
   (y, y0)
])

print(f"An Stelle x={x0}, y={y0} = ({df_x_eval}, {df_y_eval})")
```