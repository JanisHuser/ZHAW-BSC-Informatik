# Gauss Algorithmus


1. Matrizen in Dreiecksform bringen

## Entiwcklungssatz

Berechnen der Determinante einer grossen Matrix aus den Determinanten von mehreren kleineren Matrizen.

$$
A=
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} \\
\end{pmatrix}
$$

Nach a11 entwickelt

$$

= a_{11} \bullet

\begin{vmatrix}
a_{12} & a_{13} \\
a_{32} & a_{33} \\
\end{vmatrix}

+ 

a_{31}
\cdot
\begin{vmatrix}
a_{12} & a_{13} \\
a_{22} & a_{23} \\
\end{vmatrix}

$$
