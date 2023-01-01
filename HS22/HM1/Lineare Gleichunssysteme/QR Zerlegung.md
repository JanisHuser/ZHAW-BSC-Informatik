# Orthogonale Matrizen
Eine $n$ x $n$ Matrix $Q$ heisst **orthogonal**, wenn folgendes zutrifft, wobei $I$ die nxn-Einheitsmatrix ist.
$$
Q^T \cdot Q = I
$$

```python
import numpy as np
from Scripts.NumericHelpers import is_orthogonal

Q = np.array([
    [4/5, -3/5],
    [3/5, 4/5]
])

print(is_orthogonal(Q))
```

# QR Zerlegung
$$
A \cdot x = b
$$
$$
A = Q \cdot R
$$
$$
Q \cdot R \cdot x = b
$$
Multiplikation von links mit der immer regulären Matrix $Q^T$ ergibt das äquivalente Gleichungssystem
$$
Q^T \cdot Q \cdot R \cdot x
=
Q^T
\cdot
b
$$

## Householder-Verfahren

### Vorgehen
- Initialisiere $R=A$ und $Q =I$
- Wiederhole für $i=1, \dots, n-1:$
	- Bilde Matrix $R^{(i)}$, die durch Streichung der ersten $i-1$ Zeilen und Spalten von $R$ entsteht.
- Bilde Vektor
	- $v^{(i)} = r^{(i)} + sign(r_1^{(i)}) \cdot ||r^{(i)}|| \cdot e^{(i)}$
	- mit
		- $r^{(i)}$ = 1. Spalte von $R^{(i)}$
		- $r^{(i)}$ = 1. Komponente von $r^{(i)}$
		- $sign(x)$
			- $1$ für $x \geq 0$
			- $-1$ für $x < 0$
		- $e^{(i)}$ = Einheitsvektor mit 1.Komponente
$$
1= 
\begin{bmatrix}
1 \\
0 \\
\vdots \\
0
\end{bmatrix}
$$
- Bilde Vektor $M^{(i)} = \frac{1}{||v^{(i)}||} \cdot v^{(i)}$
- Bilde Matrix $H^{(i)} = I - 2 \cdot M^{(i)} \cdot (H^{(i)})^T$
- Bilde $nxn$-Matrix $Q$
$$
Q^{(i)}
=
\begin{bmatrix}
I & 0 \\
0 & H^{(i)}
\end{bmatrix}
$$
- Setze $R=Q^{(i)} \cdot R$ und $Q = Q \cdot (Q^{(i)})^T$


```python
import numpy as np

from Scripts.NumSolve import calc_qr

A = np.array([
    [2, 5, 0],
    [-2, 2, 6],
    [1, 0, 3]
])

Q, R = calc_qr(A)
print (f"Q:\n{Q}")
print (f"R:\n{R}")
```