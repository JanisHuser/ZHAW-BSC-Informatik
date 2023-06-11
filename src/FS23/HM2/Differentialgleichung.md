# Differentialgleichung

## Transformation in DGL System 1. Ordnung

1. DGL 2. Ordnung gegeben

$$
y'' + 2y + x = 0
$$

2. Ersatzvariablen einführen
$ y_1 = y $ und $y_2 = y'$

3. Ersatzvariablen in DGL einsetzen. Somit ist die DGL 2. Ordnung jetzt 1. Ordnung.

$$
y_2' + 2 y_1 + x = 0
$$

3. In System umbauen

$$
y_1 = y \to y_2 = y' = y_1'
$$

$$
y_1' = y_2
$$

4. Umstellen der DGL 1. Ordnung (Schritt 2)

$$
y_2 = -2y_1 - x
$$

5. In Matrixschreibweise schreiben

$$
\begin{pmatrix}
y_1' \\
y_2'
\end{pmatrix}
=
\begin{pmatrix}
0 & 1 \\
-2 & 0
\end{pmatrix}

\begin{pmatrix}
y_1 \\
y_2
\end{pmatrix}
+

\begin{pmatrix}
0 \\
-x
\end{pmatrix}
$$

