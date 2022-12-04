# Konvergenz

- B ist eine n x n Matrix

$$
x^{(n+1)}
=
Bx^{(n)}
+c
=:
F(x^{(n)})
$$
## Anziehend

$$
|| B || \lt 1
$$

## Abstossend

$$
|| B || \gt 1
$$


# Abschätzungen

$$
x^{(n+1)}
=
Bx^{(n)}
+c
=:
F(x^{(n)})
$$
### Jacobi
$$
B = -D ^{-1}(L+U)
$$ 
### Gauss-Seidel
$$
B = -(D+L)^{-1}U
$$


## A-priori Abschätzung

$$
||
x^{(n)} - \overline{x}
||

\leq
\frac{
||B ||^n
}{
1 - ||B ||
}

||
x^{(1)} - x^{(0)}
||
$$

### Implementierung

```python, editable
import numpy as np

A = np.array([
	[4, -1, 1],
	[-2, 5, 1],
	[1, -2, 5]
], dtype='float64')

b = np.array([5,11,12], dtype='float64').reshape(3,1)

x = [np.array([
		[1,2,3],
		[4,5,6],
		[7,8,9]]),
    np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
    ] # <- Fill x in here


option = 'jacobi'
# option = 'gauss-seodel'

D = np.diagflat(np.diag(A), 0)
L = np.tril(A)
U = np.triu(A)

D_inv = np.linalg.inv(D)
LU = L+U


if option == 'jacobi':
	B = -1 * np.matmul(D_inv, LU) 
else:
	B = -1 * np.matmul(np.linalg.inv(D + L), U)

B_norm = np.linalg.norm(B, np.inf)

relative_x_error = np.linalg.norm(x[1] - x[0], np.inf)
estimation = B_norm / (1 - B_norm) * relative_x_error

print ("D^{-1}", '\n', D_inv)
print ("B", '\n', B)
print (" A-Priori Estimation", estimation)
print ("estimation >= ||x_n - x_ ||")
```
## A-Posteriori Abschätzung

$$
||
x^{(n)} - \overline{x}
||

\leq
\frac{
||B ||
}{
1 - ||B ||
}

||
x^{(n)} - x^{(n-1)}
||
$$

```python, editable
import numpy as np

A = np.array([
	[4, -1, 1],
	[-2, 5, 1],
	[1, -2, 5]
], dtype='float64')

b = np.array([5,11,12], dtype='float64').reshape(3,1)

x = [np.array([
		[1,2,3],
		[4,5,6],
		[7,8,9]]),
    np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])
    ] # <- Fill x in here
n = 1

option = 'jacobi'
# option = 'gauss-seodel'

D = np.diagflat(np.diag(A), 0)
L = np.tril(A)
U = np.triu(A)

D_inv = np.linalg.inv(D)
LU = L+U


if option == 'jacobi':
	B = -1 * np.matmul(D_inv, LU) 
else:
	B = -1 * np.matmul(np.linalg.inv(D + L), U)

B_norm = np.linalg.norm(B, np.inf)

relative_x_error = np.linalg.norm(x[n] - x[n-1], np.inf)
estimation = B_norm / (1 - B_norm) * relative_x_error

print ("D^{-1}", '\n', D_inv)
print ("B", '\n', B)
print (" A-Posteriori Estimation", estimation)
print ("estimation >= ||x_n - x_ ||")
```