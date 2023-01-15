# Gauss-Seidel Verfahren
$$
x^{(k+1)}=D^{-1} (b - Lx^{(k+1)} - Rx^{(k)})
$$

## Algemeine Form

$$
x_{j}^{(k+1)}
=
\frac{1}{a_{ii}}
\left(
b_i - \sum_{j=1}^{i-1}a_{ij}x_j^{(k+1)}
-
\sum_{j=i+1}^n
a_{ij}x_j^{(k)}
\right)
$$
## Fixpunktiteration


$$
(D+L)x^{(k+1)}
=
-Rx^{(k)}
+b
$$
$$
x^{(k+1)}
=
-(D+L)^{-1}Rx^{(k)}
+ (D+L)^{-1}b
$$


$$
B = -(D+L)^{-1}U
$$
```python
from Scripts.Iteration.Jacobi import Jacobi
from Scripts.Iteration.GaussSeidel import GaussSeidel
import numpy as np
import math

n = 6
c = 4
x0 = np.zeros(n).reshape(n,1)
tolerance = 10**(-3)

jacobi = GaussSeidel(
    Jacobi.create_A_diagonal(n, c),
    Jacobi.create_b_diagonal(n, c),
    x0)

print ("B")
B = jacobi.calc_B()
print (B)

print (f"Inf Norm von B: {np.linalg.norm(B, np.inf)}")
estimation = jacobi.estimate_a_priori(tolerance)
print (f"A-Priori abschätzung: {estimation}  => {round(estimation)}")

# result = jacobi.iterate(tolerance, True)
result = jacobi.iterate_n(int(math.ceil(estimation)), False)

# def calc_a_posteriori_error(self,B, x, xn) -> Number:
```