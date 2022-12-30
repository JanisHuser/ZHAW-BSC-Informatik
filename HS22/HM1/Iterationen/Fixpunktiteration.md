# Fixpunkt
Es seien
- $I$ eine Intervall von $\mathbb{R}$
- $F$ eine Funktion von $I$
- $\overline{x}$ eine Zahl aus $I$ mit $F(\overline{x}) = \overline{x}$

$$
x_0, x_1 = F(x_0), x2= F(x_1), ... x_{n+1} = F(x_n)
$$


## Beispiel
$F(x) = x^2$

| x     | F(x)                  |
| ----- | --------------------- |
| $x_0$ | $1.2$                 |
| $x_1$ | $F(x_1)=1.2^2 = 1.44$ |
| $x_2$ | $F(x_2) = 1.44^2 = 2.0736$                      |

-> Folge divergiert gegen $\infty$

| x     | F(x)                  |
| ----- | --------------------- |
| $x_0$ | $0.8$                 |
| $x_1$ | $F(x_1)=0.8^2 = 0.64$ |
| $x_2$ | $F(x_2) = 0.64^2 = 0.4096$                      |

-> Folge konvergiert gegen $0$

```python
from Scripts.Iterationen import calc_fixpunkt

def F(x):
    return (x**3 + 12) / 13

x0 = 2.
n = 5

# Berechne Fixpunktiteration und gib einzelne Schritte aus
steps = calc_fixpunkt(F, x0, n, True)

```


**Anziehender Fixpunkt**: Wenn die Folge gegen $\tilde{x}$ konvergiert.
**Abstossender Fixpunkt**: Wenn die Folge *nicht* gegen \tilde{x} konvergiert.


# Fixpunktiteration mit Toleranz

```python
from Scripts.Iterationen import calc_fixpunkt_with_tolerance

def F(x):
    return x ** 0.5

x0 = 2.
xq = 1.
tolerance = 1e-6

iterations =  calc_fixpunkt_with_tolerance(F, x0, xq, tolerance, True)

print (f"Benötigte Iterationen: {iterations}")
```