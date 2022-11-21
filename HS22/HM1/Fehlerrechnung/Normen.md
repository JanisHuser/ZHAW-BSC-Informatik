# Konditionszahl

$ \text{cond} ( A )  = ||A|| * ||A^1|| $

```python,editable
import numpy as np

A = np.array([
	[1, 2],
	[3, 4]
])

cond = np.linalg.cond(A)

print ("Konditionszahl", cond)

```

# Vektornorm

$$
	\left|
	\left|
	.
	\right|
	\right|
	:
	\mathbb{R}^n \rightarrow \mathbb{R}
$$

## Allgemein

-  $ ||.|| $ eine Norm, $ A \in \mathbb{R}^{n \times n} $ eine regüläer $ n \times n $ Matrix
- $ x, \tilde{x}, b, \tilde{b} \in \mathbb{R}^n $ mit $ Ax = b $ und $ A \tilde{x} = \tilde{b} $

**Dann gilt**:

- $ || x - \tilde{x} \leq ||A^{-1} ||
\cdot
\frac{||b- \tilde{b}||}{||b||} $
**Falls $ b \neq 0 $**: $ \frac{|| x - \tilde{x}}{||x||} \leq ||A|| \cdot ||A^{-1} ||
\cdot
\frac{||b- \tilde{b}||}{||b||} $



## Bedingungen
- $ ||x|| \geq 0 $ und $ ||x|| = 0 \Leftrightarrow x = 0 $
- $ || \lambda x || = \lambda ||x|| $
- Dreiecksgleichung: $ || x +y || \leq ||x|| + ||y|| $

## Vektornormen
Für Vektoren $ (x = x_1, x_2, ..., x_n )^T \in \mathbb{R}^n $ gibt es folgende Vektornormen:

### 1-Norm, Summenform

$
||x||_1 = \sum_{i=1}^n | x_i |
$

### 2-Norm, euklidische Norm

$$
||x||_2 = \sqrt{ \sum_{i=1}^n x_{i}^2 }
$$

### $ \infty $-Norm, Maximumnorm

$$
||A||_{\infty} = \max\limits_{i=1,…,n} |x_{i}|
$$

# Matrixnormen

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


