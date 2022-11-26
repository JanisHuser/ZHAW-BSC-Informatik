# Hypergeometrische Verteilung

| Symbol | Beschreibung |
|--|--|
| $ X $ | Zufallsvariable: zählt, wie oft bei der $n$-fachen Ziehung ein Merkmalsträger gezogen wird. |
| $ n $ | Anzahl Ziehungen ohne Zurücklegen |
| $ N $ | Gesamtzahl aller Objekte |
| $ M $ | Gesamtzahl aller Merkmalsträger |

Eine diskrete Zufallsvariable $ X $ heisst *hypergeometrisch verteilt* mit den Parametern $ n $, $ N $ und $ M $, wenn ihre Dichtefunktion (PMF) gegeben ist durch

$$

P(X = x) =
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
}{
\begin{pmatrix}
N \\
n
\end{pmatrix}
}

$$

Schreibweise: $ X \tilde H(N, M, n) $


## Satz

Für eine ZUfallsvariable $ X \tilde H(N, M, n) $ gilt:

(1) $ \mu = E(X) = n \cdot \frac{M}{N} $

(2) $ \sigma^2 = V(X) = n \cdot \frac{M}{N} \cdot (1 - \frac{M}{N}) \cdot \frac{N-n}{N-1} $

(3) $ \sigma = S(X) =\sqrt{V(X)} $


# Bernoulli Verteilung

Eine Zufallsvariabe $ X $ heisst *Bernoulli-verteilt*, wenn sie nur zwei verschiedene Werte annehmen kann:

- Den Wert 1 mit der Wahrscheinlichkeit $ P(X =1) = p $
- Den Wert 0 mit der Wahrscheinlichkeit $ P(X = 0) = 1 - p $

## Satz

Für Bernoulli-verteilte Zufallsvariablen $ X $ gilt:

(1) $ E(X) = E(X^2) = p $

(2) $ V(X) = p \cdot (1 - p) $

# Binomialverteilung

$ p $: Wahrscheinlichkeit für ein Ergebnis 1
Eine diskrete Zufallsvariable $X$
heisst binomialverteilt mit den Parametern $n$ und $p$, wenn ihre Dichtefunktion (PMF) gegeben ist durch

$$

P(X = x)
=
\begin{pmatrix}
n \\
x
\end{pmatrix}

\cdot 
p^x

\cdot

(1-p)^{n-x}
$$

Schreibweise: $ X \tilde B(n; p) $