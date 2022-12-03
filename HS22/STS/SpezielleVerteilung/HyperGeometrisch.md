# Hypergeometrische Verteilung


- Wird angewendet Zufallsexperimenten mit nur zwei möglichen Ergebnissen, Erfolg oder Nicht-Erfolg.

- Experimente ohne zurücklegen

$$

P (X = x) =
\frac{
	\begin{pmatrix}
	M \\
	x
	\end{pmatrix}

	\cdot

	\begin{pmatrix}
	N - M \\
	n - x
	\end{pmatrix}
}
{
	\begin{pmatrix}
	N \\
	n
	\end{pmatrix}
}

$$

$$

X
\tilde
HG(N,M,n)
$$

| Symbol | Beschreibung |
|--|--|
| N | Anzahl aller Elemente. |
| M | Anzahl derjenigen Element an, die als Erfolg gesehen werden. |
| n | Anzahl an Elementen die für das Zufallsexperiment gezogen werden |

## Varianz

$$

V(X) = n
\cdot
\frac{M}{N}
(1 - \frac{M}{N})
\frac{
	N - n
}{
	N -1
}

$$

## Verteilungsfunktion

$$
F(X) = 
P(X \leq x)
=

\sum_{k=1}^x f(k)
$$

## Erwartungswert

$$

E(X) = n
\cdot
\frac{M}{N}

$$