**Ziel**: Nullstelle $\tilde{x}$ einer differenzierbaren Funktion $y=f(x)$ näherungsweise numerisch bestimmen.

# Vorgehen
1. Startwert $x_0$ in der Nähe von $\overline{x}$ auswählen
2. An der Stelle $x_0$ die Tangente zu den Graphen von f aufstellen und berechne die schnittstelle $x_1$ der Tangente mit der x-Achse.
3. Wiederhole 2 ausgehend von $x_1$ und erhalte so $x_1$

# Formel

## Tangentensteigung

$$
f'(x_0) = \frac{f(x_0)}{x_0 - x_1}
$$

## Iterationsformel
$$
x_{n+1} =
x_n
-
\frac{f(x_n)}{f'(x_n)}
$$

```python
from Scripts.Iterationen import calc_newton

f = "x**3. - 13.*x + 12"
x0 = -5.
n = 5

x = calc_newton(f, x0, n, True)
```