$$
Ax = \lambda x
$$
![[Eigenvektor.excalidraw]]
$$
A \in \mathbb{R}^{n x n}
$$

## Nullvektor
$$
x=0
$$

$$
A =
\begin{pmatrix}
2 & 0 & 1 \\
7 & -5 & 9 \\
6 & -6 & 9
\end{pmatrix}

=

\begin{pmatrix}
2 & 0 & 1 \\
7 & -5 & 9 \\
6 & -6 & 9
\end{pmatrix}

\begin{pmatrix}
4 \\
-1 \\
-3
\end{pmatrix}

=
1
\cdot
\begin{pmatrix}
3 \\
-1 \\
-3
\end{pmatrix}
$$

## Drehmatrix
Die Winkel zur Achse bleiben bei der Drehung gleich
![[Drehmatrix.excalidraw]]

$$
Ax - \lambda x = 0
\Leftrightarrow
(A - \lambda l_n)x = 0
$$
- x is t also die Lösung eines homogenenen linearen Gleichungssystems
- Dies hat, wie wir aus der linearen Algebra wissen, nur dann eine nicht triviale Lösung $x \neq 0$, wenn die Determinante $det (A - \lambda l_n)$ gleich Null ist.

## Eigenschaften
- Die **Determinante** der Matrix $A$ ist gerade das Produkt ihrer Eigenwerte $\lambda_1, ... \lambda_n$
- Die Summe der Eigenwerte ist gleich der Summe der Diagonalelemente von $A$. d.h. gleich der Spur von $A$.
	- $det A = \lambda_1 \cdot \lambda_2 \cdots \lambda_n$
	- $tr A = a_{11} + a_{22} + \cdots + a_{nn} = \lambda_1 + \lambda_2 + \cdots + \lambda_n$
- Ist $\lambda_i$ ein Eignewert der regulären Matrix $A$, so ist der Kehrwert $\frac{1}{\lambda_i}$ ein Eigenwert der inversen Matrix $A^{-1}$


## Eigenwerte bestimmen
![[Eigenwerte_bestimmen.excalidraw]]