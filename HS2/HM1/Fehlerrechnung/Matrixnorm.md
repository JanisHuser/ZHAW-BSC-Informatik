
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

Für eine $n \times n$ Matrix $A in \mathbb{R}^{n \times n }$
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
## Beispiel

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


