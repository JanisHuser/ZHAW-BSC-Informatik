# Binominalverteilung

- Wird angewendet bei: Erfolg und Nicht-Erfolgsexperimenten (Treffer / Kein Treffer)
- Verteilung mit Zurücklegen

Wiederholtes Anwenden der Bernouilli Verteilung

$$
P(X = k)
=
\begin{pmatrix}
n \\
k
\end{pmatrix}
\cdot
p^k
\cdot
(1-p)^{n-k}
$$

$$
H
\tilde
B(n,p)
$$

| Symbol | Beschreibung |
|--|--|
| n | Grösse der Stichprobe |
| $ \pmatrix{begin} n \\ k \end{pmatrix}$ | Binomalkoeffizient |
| p | Erfolgswahrscheinlichkeit des Ereignises |
| k | Anzahl der Erfolge im Zufallsexperiment |


## Binomialkoeffizienten

$$

\begin{pmatrix}
n \\
k
\end{pmatrix}

=

\frac{
	n!
}{
	k!
	\cdot
	(n-k)!
}
$$

## Beispiel

Höchstens zwei Treffer

$$
P(X \leq 2)
=
P(X=0) +
P(X=1) +
P(X=2)
$$

## Verteilungsfunktion
$$
F(x) =
\sum_{k=0}^m
\begin{pmatrix}
n \\
k
\end{pmatrix}

\cdot

p^k
\cdot
(1-p)^{n-k}
$$

