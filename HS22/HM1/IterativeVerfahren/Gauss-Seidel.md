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
```python,editable
import numpy as np

# Setting some variables
A = np.array([
    [8, 5, 2],
    [5, 9, 1],
    [4, 2, 7]
],dtype='float64')

b = np.array([19, 5, 34], dtype='float64').reshape(3,1)
x0 = np.array([1, -1, 3], dtype=float).reshape(3, 1)


D = np.diagflat(np.diag(A), 0)
L = np.tril(A, k=-1)
U = np.triu(A, k=1)


D_inv = np.linalg.inv(D)
B = np.dot(-1, np.linalg.inv(np.add(D, L)).dot(U))


    
xi = [x0]
    
np.set_printoptions(precision=4)
for i in range(3):
	xi = x[i]
	xn = np.add(B.dot(xi), np.linalg.inv(np.add(D, L)).dot(b))
	print ("{i}. Schritt")
	print (xn, "\n")
	x.append(xn)


print ("B",'\n', B)
print ("B_norm", np.linalg.norm(B, np.inf))
```