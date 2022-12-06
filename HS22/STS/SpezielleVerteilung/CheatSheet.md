# Verteilungen - Cheatsheet

$$
\begin{pmatrix}
M \\
x
\end{pmatrix}

= M \text{ nCr } x
$$

## Hypergeometrische Verteilung
- Wahrscheinlichkeit für mehrere unterschiedliche Elemente berechnen.
$$
X
\sim
H(N, M, n)
$$
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
\mu = E(X) = n \cdot
\frac{M}{N}
$$
$$
\sigma^2=
V(X) = n \cdot
\frac{M}{N}
\cdot
(1-\frac{M}{N})
\cdot
\frac{N-n}{N-1}
$$
$$
\sigma = S(X) = \sqrt{V(X))}
$$
**N**: Anzahl Möglichkeiten
**M**: Anzahl an Richtigen Möglichkeiten
**n**: Anzahl Ziehungen
**x**: Wie viele Ziehungen müssen richtig sein

**MINDESTENS 1**: $ 1 - P(0) $

## Bernoulli Verteilung
Wenn sie nur zwei verschiedene Werte annehmen kann.

$$
P(X=0) = 1 -p
$$
$$
E(X) = E(X^2)=p
$$
$$
V(X)=p \cdot (1-p)
$$

## Binomialverteilung
X zählt wie oft bei der n-fachen Wiederholung eines Bernoulli-Experiments das Ergebnis 1 eintritt.
$$
x
\sim
B(n;p)
$$
$$
P(X=x)
=
\begin{pmatrix}
n \\
x
\end{pmatrix}
\cdot p^x
\cdot
(1-p)^{n-x}
$$
$$
\mu
=
E(X)
=np
$$
$$
\sigma^2 = V(X) = npq
$$
$$
\sigma
= S(X) = \sqrt{npq}
$$

## Poisson Verteilung
Durchschnittliche Anzahl Ereignisse pro betrachtetes Zeitintervall.
$$
X
\sim
Poi(\lambda)
$$
$$
P(X = x)
=
e^{-\lambda \cdot \frac{\lambda^x}{x!}}
$$
$$
\mu = E(X) = \lambda
$$
$$
\sigma^2
= V(X)
=
\lambda
$$
$$
\sigma
=
S(X)
= \sqrt{\lambda}
$$

## Gauss'sche Normalverteilung
