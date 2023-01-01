$$
P \cdot A
= L \cdot R
$$

Hinzufügen der Permutationsmatrix $P$

- P erhält man aus der $n$ x $n$ Einheitsmatrix $I$, indem jede Zeilenvertauschung in der Reihenfolge des Auftretens durchgeführt wird.

# Vorgehensweise
1. Löse zunächst das lineare Gleichungssystem $L \cdot y = P \cdot b$
2. Löse anschliessend das Gleichungssystem $R \cdot x = y$

# Beispiel

$$
A =
\begin{bmatrix}
0 & 0 & 2 & 1 \\
1 & 0 & 1 & -1 \\
2 & 1 & 0 & -2 \\
-2 & 1 & 0 & 0 \\
\end{bmatrix}
$$
1. Durchführen von Gauss-Algorithmus **ohne** Spaltenpivotisierung
$$
R = 
\begin{bmatrix}
1 & 0 & 1 & -1 \\
0 & 1 & -2 & 0 \\
0 & 0 & 2 & 1 \\
0 & 0 & 0 & -4 \\
\end{bmatrix}
$$
2. Bestimmung von L
- $Z_1 \leftrightarrow Z_2$
- $Z_2 \leftrightarrow Z_3$
$$
L = 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-2 & 1 & 2 & 1 \\
\end{bmatrix}
$$
3. Bestimmung von P
- Spaltenpivotisierung von L durchführen
$$
P=
\begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

**Ergebnis**:
$$
\begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\cdot
\begin{bmatrix}
0 & 0 & 2 & 1 \\
1 & 0 & 1 & -1 \\
2 & 1 & 0 & -2 \\
-2 & 1 & 0 & 0 \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 & 0 \\
2 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-2 & 1 & 2 & 1 \\
\end{bmatrix}
\cdot
\begin{bmatrix}
1 & 0 & 1 & -1 \\
0 & 1 & -2 & 0 \\
0 & 0 & 2 & 1 \\
0 & 0 & 0 & -4 \\
\end{bmatrix}
$$

