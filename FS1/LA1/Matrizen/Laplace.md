# Laplace

$$
(-1)^{i+j} \\
a_{ij}
$$

$$
A =
\begin{pmatrix}
1 & 2 & 4 \\
3 & 5 & 1 \\
7 & 2 & 5
\end{pmatrix}


=
\begin{pmatrix}
\stackrel{+}{a_{11}} & \stackrel{-}{a_{12}} & \stackrel{+}{a_{13}} \\

\stackrel{-}{a_{21}} & \stackrel{+}{a_{22}} & \stackrel{-}{a_{23}} \\

\stackrel{+}{a_{31}} & \stackrel{-}{a_{32}} & \stackrel{+}{a_{33}} \\
\end{pmatrix}

$$


# Zeile / Spalte auswählen
Die mit den meisten Nullen
$$

\begin{pmatrix}
\color{red}1 & \color{red}2 & \color{red}4 \\
3 & 5 & 1 \\
7 & 2 & 5
\end{pmatrix}

$$

## Nächster Schritt

Spalte wegstreichen (Beispiel bei 1. Zeile / 1. Zahl)

$$

\begin{pmatrix}
\color{red}\sout{1} & \color{red}\sout{2} & \color{red}\sout{4} \\
\sout{3} & 5 & 1 \\
\sout{7} & 2 & 5
\end{pmatrix}

$$

## Nach Hauptachse multiplizieren

$$
1 \cdot
\begin{vmatrix}
\color{blue}5 & \color{red}1 \\
\color{red}2 & \color{blue}5 \\
\end{vmatrix}

=

\color{red}+5 \cdot 5 \color{blue}- 2 * 1

$$

$$

\det A
=
+1 
\begin{vmatrix}
5 & 1 \\
2 & 5 \\
\end{vmatrix}

-2 
\begin{vmatrix}
3 & 5 \\
7 & 2 \\
\end{vmatrix}
+4

$$

## Bei grösseren Matrizen

$$
\begin{pmatrix}
1 & 2 & 4 & \color{red}4 \\
3 & 4 & 1 & \color{red}2 \\
5 & 7 & 1 & \color{red}2 \\
1 & 1 & 5 & \color{red}7 \\
\end{pmatrix}
$$



$$
-4 / +2 / -2 / +7
$$

$$

-4 
\begin{pmatrix}
3 & 4 & 1 \\
5 & 7 & 1 \\
1 & 1 & 5 \\
\end{pmatrix}

+2
\begin{pmatrix}
1 & 2 & 4 \\
5 & 7 & 1 \\
1 & 1 & 5 \\
\end{pmatrix}

-2
\begin{pmatrix}
1 & 2 & 4 \\
3 & 4 & 1 \\
1 & 1 & 5 \\
\end{pmatrix}

+7
\begin{pmatrix}
1 & 2 & 4\\
3 & 4 & 1 \\
5 & 7 & 1 \\
\end{pmatrix}
$$