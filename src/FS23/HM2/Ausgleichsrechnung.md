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