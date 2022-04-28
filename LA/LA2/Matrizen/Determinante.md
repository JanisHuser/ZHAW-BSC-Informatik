# Determinante

Eine determinante kann anzeigen, ob eine Matrix invertierbar ist.

## Berechnung der Determinante


## Definition Determinante 2x2 Matrix

$$
A =
\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}

$$

$$
\det (A) = \mid A \mid = a * d - b *c
$$

## Definition Determinante 3x3 Matrix

$$

A=
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

$$
\det (A) = \mid A \mid \\
= 
a_{11} \cdot a_{22} \cdot a_{33} +
a_{12} \cdot a_{23} \cdot a_{31} +
a_{13} \cdot a_{21} \cdot a_{32} \\

- a_{13} \cdot a_{22} \cdot a_{31}
- a_{11} \cdot a_{23} \cdot a_{32}
- a_{12} \cdot a_{21} \cdot a_{33}
$$

### Geometrische Interpretation

$$

\mid
\begin{pmatrix}
a_{1} \\
a_{2} \\
0
\end{pmatrix}

\times

\begin{pmatrix}
b_{1} \\
b_{2} \\
0
\end{pmatrix}

\mid

=
\mid
\begin{pmatrix}
0 \\
0 \\
a_{1} \cdot b_{2} - a_{2} \cdot b_{1}
\end{pmatrix}
\mid

=

\mid
a_{1} \cdot b_{2} - a_{2} \cdot b_{1}
\mid

$$

$$
\det{(A \cdot B)} = \det{(A)} \cdot \det{(B)}
$$

$$
\det{(A^{-1})} = \frac{1}{\det{(A)}}
$$

$$
\det{(\lambda \cdot A)} = \lambda^n \cdot \det{(A)}
$$

$$
\det{(E)}=1
$$