# Jacobi Verfahren

Ein Algorithmus zu näherungsweisen Lösung von linearen Gleichungssystemen.

## Beschreibung

$$

\begin{matrix}
a_{11} \cdot x_1 + \cdots + a_{1n} \cdot x_n = b_1 \\
a_{21} \cdot x_1 + \cdots + a_{2n} \cdot x_n = b_2 \\
							\vdots \\
a_{n1} \cdot x_1 + \cdots + a_{mn} \cdot x_n = b_n
\end{matrix}

$$


$$

x_i^{m+1}
:=
\frac{1}{a_{ii}}

\left(
b_i
-
\sum\limits_{j \neq i}
a_{ij}
\cdot x_j^(m)
\right)
,
i = 1,...,n
$$

## Algorithmus

Gegeben Startvektor $ x^{alt} $
für $ m=1,... $ bis Erfüllung eines Abbruchkriteriums
	$ x = b $
	fürr $ i=1 $ bis $ n $
		für $ j = 1 $ bis $ n $
			falls $ j \neq i $
				$ x_i = x_i - a_{ij} x_j^{alt};
		ende
		$ x_i = x_i / a_{ii}; $
	
	ende
	$ x^{alt} = x_i;
ende


```python
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
LU = L + U

D_inv = np.linalg.inv(D)
D_inv_LU = np.dot(D_inv, LU)
D_inv_b = D_inv.dot(b)

B = np.dot(-1, np.linalg.inv(np.add(L, R)))

print ("B")
print(B)
    
xi_1 = x0
    
np.set_printoptions(precision=4)
for i in range(3):
	xi = xi_1
	xi_1 = -1 * np.dot(D_inv_LU, xi) + D_inv_b
	print ("{i}. Schritt")
	print (xi_1, "\n")
        
print ("L+U = LU", L, U, LU, "\n")
print ("D^-1 * LU = ", D_inv, D_inv_LU, "\n")

```

## Konvergenz

Die Matrix konvergiert, wenn diese echt kleiner als 1 ist.

$$ D^{-1} (L+U) $$

### Beispiel

$$
\begin{pmatrix}
0 & 0.625 & 0.25 \\
0.55 & 0 & 0.11 \\
0.571 & 0.286 & 0
\end{pmatrix}

= max\{0, 0.11, 0.25, 0.286, 0.55, 0.571, 0.625 \} = 0.625

$$

## Fixpunktiteration


$$
Dx^{(k+1)} = - (L+)x^{(k)} + b
$$

$$
x^{(k+1)} = - D^{-1}(L+U)x^{(k)} + D^{-1}b
$$
## Herleitung

$$
Ax = b
$$
$$
(L + U + R)x = b
$$
$$
(L+U)x + Dx = b
$$
$$
Dx = -(L+U)x + b
$$
$$
x = -D^{-1}(L+U)x+D^{-1}b \equiv F(x) 
$$
### Beispiel

$$
A =
\begin{pmatrix}
4 & -1 & 1 \\
-2 & 5 & 1 \\
1 & -2 & 5
\end{pmatrix};

b =
\begin{pmatrix}
5 \\
11 \\
12
\end{pmatrix}
$$

$$
L =
\begin{pmatrix}
0 & 0 & 0 \\
-2 & 0 & 0 \\
1 & -2 & 0
\end{pmatrix}
,

D =
\begin{pmatrix}
4 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 5
\end{pmatrix}
,

U =
\begin{pmatrix}
0 & -1 & 1 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{pmatrix}
,
$$

$$
x^{n+1}
=
- D^{-1}((L+U)x^{(n)} - b)
$$
$$
=
\begin{pmatrix}
0.25 & 0 & 0 \\
0 & 0.2 & 0 \\
0 & 0 & 0.2
\end{pmatrix}

\left(
\begin{pmatrix}
0.25 & 0 & 0 \\
0 & 0.2 & 0 \\
0 & 0 & 0.2
\end{pmatrix}
x^{(n)}

\begin{pmatrix}
5 \\
11 \\
12
\end{pmatrix}
\right)
$$
$$
\begin{pmatrix}
0 & 0.25 & -0.25 \\
0.4 & 0 & -0.2 \\
-0.2 & 0.4 & 0
\end{pmatrix}

x^{(n)}
+
\begin{pmatrix}
1.25 \\
2.2 \\
2.4
\end{pmatrix}
$$
![[Pasted image 20221204181527.jpg]]
## Fehlerrechnung

