# Aufteilung
## Variation (mit Reihenfolge)
- Wesentliche Reihenfolge
### Mit Wiederholung
$$
n^k
$$

### Ohne Wiederholung
$$
\frac{
n!
}{
(n-k)!
}
$$

## Kombination (ohne Reihenfolge)
-  Keine wesentliche Reihenfolge
### Mit Wiederholung
$$
\begin{pmatrix}
n + k -1 \\
k
\end{pmatrix}
$$

### Ohne Wiederholung
$$
\frac{
n!
}{
(n-k)!k!
}
=
\begin{pmatrix}
n \\
k
\end{pmatrix}
$$


# Binominalkoeffizienten

## Leere Menge
$$
\begin{pmatrix}
n \\
0
\end{pmatrix} = 1
$$
## Symmetrie.
$$
\begin{pmatrix}
n \\
k
\end{pmatrix}

=
\begin{pmatrix}
n \\
k + 1
\end{pmatrix}
$$

## Pascal'sches Dreieck - Rekursion

$$
\begin{pmatrix}
n +1\\
k+1
\end{pmatrix}

=
\begin{pmatrix}
n\\
k
\end{pmatrix}
+
\begin{pmatrix}
n\\
k+1
\end{pmatrix}
$$

## Binomischer Lehrsatz
$$
(a+b)^n
=
\begin{pmatrix}
n \\
0
\end{pmatrix}
a^0 b^n
+
\begin{pmatrix}
n\\
1
\end{pmatrix}
a
b^{n-1}
+
\begin{pmatrix}
n\\
2
\end{pmatrix}
a^2
b^{n-2}
+
\cdots
+
\begin{pmatrix}
n\\
n-1
\end{pmatrix}
a^{n-1}
b
+
\begin{pmatrix}
n\\
n
\end{pmatrix}
a^n
b^0
=

\sum\limits_{k=0}^{n}
\begin{pmatrix}
n \\
k
\end{pmatrix}
a^k
b^{n-k}
$$
### Binominalkoeffizient
$$
\begin{pmatrix}
n \\
k
\end{pmatrix}
=
\frac{
n!
}{
(n-k)! \cdot k!
}
$$TR: $n$ "ncR" $k$

### Auswahl ohne zurücklegen
**Anzahl Möglichkeiten:** $n$
**Anzahl die zu ziehen sind:** $k$
$$
M
=
\begin{pmatrix}
n \\
k
\end{pmatrix}
=
\frac{
n!
}{
(n-k)! \cdot k!
}
$$
### Anzahl totale Möglichkeiten
**Anzahl zur Auswahl:** $n$
$$
M = n!
$$

