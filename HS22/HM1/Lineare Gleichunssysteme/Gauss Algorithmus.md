# Idee
1. Bringe das lineare Gleichungssystem duch Äquivalenzumformungen auf rechtsobere Dreiecksform.
2. Berechne die Lösung $x_1^*, \cdots, x_n^*$ rückwärts von $x_n^*$ zu $x_1^*$  durch Auflösen und Einsetzen:

$$
x_n^*
=
\frac{b_n}{a_nn}
$$

## Elementare Zeilenoperationen
In der Numerik werden beim Gauss-Algorithmus nur zwei Äquivalenzumformungen verwendet:
- **Zeilensubtraktion**: Von einer Zeile wird ein Vielfaches einer darüber liegenden subtrahiert
- **Zeilenvertauschen**: Zwei Zeilen werden, *wenn nötig* vertauscht.

```python
import numpy as np
from Scripts.NumSolve import calc_gauss

A = np.array([
    [2, 1, 0],
    [4, 0, -2],
    [1, 2, 4]
])
b = np.array([
    [1],
    [1],
    [0]
])

calc_gauss(A, b, True)
```

