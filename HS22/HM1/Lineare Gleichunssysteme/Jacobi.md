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

Gegeben Startvektor $x^{alt}$
für $m=1,...$ bis Erfüllung eines Abbruchkriteriums
	$x = b$
	fürr $i=1$ bis $n$
		für $j = 1$ bis $n$
			falls $j \neq i$
				$x_i = x_i - a_{ij} x_j^{alt}$;
		ende
		$x_i = x_i / a_{ii};$
 	 ende
	 $x^{alt} = x_i$;
ende


```python
from Scripts.Iteration.Jacobi import Jacobi
import numpy as np
import math

n = 6
c = 4
x0 = np.zeros(n).reshape(n,1)
tolerance = 10**(-3)

jacobi = Jacobi(
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

