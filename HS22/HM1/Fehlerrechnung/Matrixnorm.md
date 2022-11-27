
# Matrixnormen

```python,editable
import numpy as np

A = np.array([
	[1, 0],
	[0, 1]
])


order = np.Infinity
# Unendlich

norm = np.linal.norm(A, np.Infinity)
print ("Kondition von A": norm)

```

## Allgemein

$$
	\frac{||x - \tilde{x}||}{||x||}
	\leq
	\frac{
		cond(A)
	}{
		1 - cond(A) \cdot \frac{||A- \tilde{A}||}{||A||}
	}
	*
	\left(
		\frac{||b - \tilde{A}||}{||A||}
		+
		\frac{||b - \tilde{b}||}{||b||}
	\right)
$$

Für eine $ n \times n $ Matrix $ A in \mathbb{R}^{n \times n })
### 1-Norm, Spaltensummennorm


$$
||A||_1 = \max\limits_{i=1,…,n} \sum_{j=1}^n |a_{ij}|
$$

### 2-Norm, Spektralnorm

$$
||A||_2 = \sqrt{ \rho ( A^T A ) }
$$


### $ \infty $-Norm, Zeilenssummennorm

$$
||A||_{\infty} = \max\limits_{i=1,…,n} \sum_{j=1}^n |a_{ij}|
$$



## Beispiele

### Vektor
$$
\left|
\left|
\begin{pmatrix}
-1 \\
2 \\
3
\end{pmatrix}
\right|
\right|_1

= 1+2+3 = 6
$$

$$
\left|
\left|
\begin{pmatrix}
-1 \\
2 \\
3
\end{pmatrix}
\right|
\right|_2

= \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}
$$

$$
\left|
\left|
\begin{pmatrix}
-1 \\
2 \\
3
\end{pmatrix}
\right|
\right|_2

= \max \{ 1,2,3 \} = 3
$$

### Matrix

$$

\left|
\left|
\begin{pmatrix}
\textcolor{red}{1} & 2 & 3 \\
\textcolor{red}{3} & 4 & -2 \\
\textcolor{red}{7} & -3 & 5
\end{pmatrix}
\right|
\right|_1


= \max \{
	( 1+3+7 ),
	( 2+4-3 ),
	( 3-2+5 )
	\} = 11

$$

$$

\left|
\left|
\begin{pmatrix}
\textcolor{red}{1} & \textcolor{red}{2} & \textcolor{red}{3}  \\
3 & 4 & -2 \\
7 & -3 & 5
\end{pmatrix}
\right|
\right|_{ \infty }


= \max \{
	( 1+2+3 ),
	( 3+4-2 ),
	( 7-3+5 )
	\} = 11

$$


