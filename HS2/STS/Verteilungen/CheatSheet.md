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

**MINDESTENS 1**: $1 - P(0)$

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
q = 1 - p
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
### Stetigkeitskorrektur
Wenn $a < x$:
- $a+0.5$
- $b+0.5$

Wenn $a \leq x$:
- $a - 0.5$
- $b + 0.5$

$P(77 \leq X < 87) \approx P(76.5 < Y \leq 77.5)$



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
$$
X
\sim
N( \mu; \sigma)
$$
$$

\rho_{\mu, \sigma}(x)
=
\frac{1}{
\sqrt{2 \pi \cdot \sigma}
}
\cdot
e^{
- \frac{1}{2}
(
\frac{x - \mu}
{ \sigma }
)^2
}
$$


## Kummulative Verteilungsfunktion (CDF)

$$
\Phi_{\mu, \sigma}(x)
=
P(X \leq x)
=
\int_{-\infty}^{x}
\rho_{\mu, \sigma}(t) dt
=
\frac{1}
{\sqrt{2 \pi \cdot \sigma}}
\cdot

\int_{- \infty}^{x}
e^{
-\frac{1}{2}
(
\frac{x - \mu}{
\sigma
}
)^2
}
dt
$$

### Standardnormalverteilung

$\mu = 0$ und $\sigma = 1$
$$

\rho (x)
=
\frac{1}{
\sqrt{2 \pi}
}

\cdot

e^{
-
\frac{1}{2}
x^2
}

$$

### Intervall

**P(U > u)**: $1 - \Phi(u)$

## Tabelle

### Normalverteilt
$$
U = \frac{X - \mu}{\sigma}
$$
$$
P(U \leq \frac{x - \mu}{\sigma})
$$

### Intervall bestimmen

$$
[
\mu - u
\cdot \sigma
;
\mu + u
\cdot \sigma
]
$$

# Zentraler Grenzwertsatz
**Bedingung**: $n > 30$

**Arithmetisches Mittel**: $\overline{X}_n = \frac{S_n}{n}$

**Summe**: $\S_n \sum_{i=1}^n X_i$

**Erwartungswert**: $\mu$

**Varianz**: $\sigma^2$



# Symbole

| Symbol | Bezeichnung | Formel | Beispiel |
|--|--|--|--|
| $\mu$ | Erwartungswert | $\frac{a+b}{2}$ | $[1;2] = 1.5$|
| $\sigma^2$ | Varianz |$\int_{a}^{b}(x - \mu)^2 \cdot f(x) dx$|






$$

$$