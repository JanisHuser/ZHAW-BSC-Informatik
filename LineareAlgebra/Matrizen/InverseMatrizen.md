# Inverse Matrizen


Die Inverse einer quadratischen Matrix A ist eine Matrix $$ A^-1$$
für die gitlt:
$$
A*A^1 = A^1 * A = E$$

## Beispiel

$$
\begin{pmatrix}
6 & -2 & 3\\
23 & -8 & 12 \\
-14 & 5 & 7\\
\end{pmatrix}
*
\begin{pmatrix}
4 & -1 & 0\\
7 & 0 & 3 \\
-3 & 2 & 2\\
\end{pmatrix}

=

\begin{pmatrix}
6*4 +   (-2)*7 + 3*(-3) &
6*(-1) +(-2)*0 + 3*2 &
6*0 +   (-2)*3 + 3*2 \\

23*4 + (-8)*7 + 3*(-3) &
23*(-1) + (-8*0) 

6 & -2 & 3\\
23 & -8 & 12 \\
-14 & 5 & 7\\
\end{pmatrix}

=
\begin{pmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1 \\
\end{pmatrix}
$$

## Inverse einer 2 x 2 Matrix

Eine 2x2 Matriz hat genau dann einen Kehrwert, wenn folgendes gilt:
$$
ad-bc \neq 0
$$


$$
\begin{pmatrix}
a & b\\
c & d \\
\end{pmatrix}
^-1

=

\frac{1}{ad-bc}
* 
\begin{pmatrix}
d & -b\\
-c & a
\end{pmatrix}
$$

1/8