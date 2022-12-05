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


# Fehlerabschätzungen

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
    [8, 5, 2],
    [5, 9, 1],
    [4, 2, 7]
],dtype='float64')

b = np.array([19, 5, 34], dtype='float64').reshape(3,1)




x = [
	np.array([1, -1, 3]).reshape(3, 1),
    np.array([ 2.25, -0.3333, 4.5714]).reshape(3,1),
    np.array([ 1.4405, -1.2024, 3.6667] ).reshape(3,1),
    np.array([2.2098, -0.6521, 4.3776] ).reshape(3,1),
]
n = 3

option = 'jacobi'
# option = 'gauss-seodel'

D = np.diagflat(np.diag(A), 0)
L = np.tril(A, k=-1)
U = np.triu(A, k=1)

D_inv = np.linalg.inv(D)
LU = L+U


if option == 'jacobi':
	B = -1 * np.matmul(D_inv, LU) 
else:
	B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(U))

B_norm = np.linalg.norm(B, np.inf)

x_norm = np.linalg.norm(x[3] - x[2], np.inf)
estimation = B_norm / (1 - B_norm) * relative_x_error

print ("D^{-1}", '\n', D_inv)
print ("B", '\n', B)
print ("B norm", B_norm)

print ("!!Aufschreiben")
print (f"{B_norm:.4f}/(1-{B_norm:.4f}) * {x_norm:.4f}={estimation:.4f}")
log({B_norm:.4f})= {n:.4f}={n}")
```

### Geschätze Iterationen

$$

\frac{
log
\frac{1- ||B||}{|| x^1 - x^0 ||}
\cdot tol
}{
log || B ||
}

$$
```python, editable
import numpy as np

A = np.array([
	[4, -1, 1],
	[-2, 5, 1],
	[1, -2, 5]
], dtype='float64')

b = np.array([5,11,12], dtype='float64').reshape(3,1)

x = [
	 np.array([1, -1, 3]).reshape(3, 1),
	 np.array([2.25, -0.333, 4.5714]).reshape(3, 1),
     np.array([1.4405, -1.2024, 3.6667]).reshape(3, 1),
     np.array([2.2098, 0.6521, 4.3776]).reshape(3, 1),
    ] # <- Fill x in here

tolerance = 1E-4

option = 'jacobi'
# option = 'gauss-seodel'

D = np.diagflat(np.diag(A), 0)
L = np.tril(A, k=-1)
U = np.triu(A, k=1)

D_inv = np.linalg.inv(D)
LU = L+U


if option == 'jacobi':
	B = -1 * np.matmul(D_inv, LU) 
else:
	B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(U))

B_norm = np.linalg.norm(B, np.inf)

x_norm = np.linalg.norm(x[1] - x[0], np.inf)

n = np.log(((1 - B_norm) / x_norm) * tolerance) / np.log(B_norm)

print ("!!Aufschreiben")
print (f"log(((1-{B_norm:.4f})/{x_norm:.4f}) * {tolerance:.4f} / log({B_norm:.4f})={n}")

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
    [8, 5, 2],
    [5, 9, 1],
    [4, 2, 7]
],dtype='float64')

b = np.array([19, 5, 34], dtype='float64').reshape(3,1)




x = [
	np.array([1, -1, 3]).reshape(3, 1),
    np.array([ 2.25, -0.3333, 4.5714]).reshape(3,1),
    np.array([ 1.4405, -1.2024, 3.6667] ).reshape(3,1),
    np.array([2.2098, -0.6521, 4.3776] ).reshape(3,1),
]
n = 3

# option = 'jacobi'
option = 'gauss-seodel'

D = np.diagflat(np.diag(A), 0)
L = np.tril(A, k=-1)
U = np.triu(A, k=1)

D_inv = np.linalg.inv(D)
LU = L+U


if option == 'jacobi':
	B = -1 * np.matmul(D_inv, LU) 
else:
	B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(U))

B_norm = np.linalg.norm(B, np.inf)

x_norm = np.linalg.norm(x[3] - x[2], np.inf)
estimation = (B_norm / (1 - B_norm)) * x_norm

print ("D^{-1}", '\n', D_inv)
print ("B", '\n', B)
print ("B norm", B_norm)

print ("!!Aufschreiben")
print (f"{B_norm:.4f}/(1-{B_norm:.4f}) * {x_norm:.4f}={estimation:.4f}")

```
