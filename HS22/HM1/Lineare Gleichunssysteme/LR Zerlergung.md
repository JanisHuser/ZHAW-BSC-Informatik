
$$
A
=
L
\cdot
U
$$
$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}

=
\begin{bmatrix}
l_{11} & 0 & 0 \\
l_{21} & l_{22} & 0 \\
l_{31} & l_{32} & l_{33}
\end{bmatrix}

\begin{bmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{bmatrix}
$$

# Vorgehen

1. LU Zerlegung der Matrix A bestimmen
2. Lineares Gleichungssystem $L \cdot y = b$ lösen
3. Anschliessen das Gleichungssystem $R \cdot x = y$



$$

$$

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

x = calc_gauss(A, b, True)
print (f"x: {x}")
```