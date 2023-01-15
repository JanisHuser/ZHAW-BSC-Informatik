**Zähldichte (Stabdiagram):** $\rho: \Omega \rightarrow [0,1]$

| Beschreibung            | Symbol                              |
| ----------------------- | ----------------------------------- |
| Unmögliches Ereignis    | $P(\{\})=0$                         |
| Sicheres Ereignis       | $P(\Omega)=1$                       |
| Komplementäres Ereignis | $P(\Omega \setminus A) = 1-P(A)$    |
| Vereinigung             | $P(A \cup B) = P(A) +P(B)-P(A\cap B)$ |

# Zufallsvariablen
**Dichtefunktion (PMF):** $f: \mathbb{R} \rightarrow [0,1], f(x) = P(X = x)$
**Kummulative Verteilungsfunktion (CDF):** $F: \mathbb{R} \rightarrow [0,1], F(x) = P(x \le x)$
## Wichtige Eigenschaften
- $\sum\limits_{x=-\infty}^{\infty} f(x) = 1$ und $F(z) = \sum\limits_{x=-\infty}^{\infty}$
- $\lim\limits_{x \rightarrow \infty} F(x) = 1$ und $\lim\limits_{x \rightarrow -\infty} F(x) = 0$

$P(a \lt X \le b) = F(b) - F(a)$
$P(a \lt X \lt b) = F(b) - \lim\limits_{x \rightarrow a} F(x)$
$P(X \gt b) = 1  - F(b)$
$P(X \gt b) = 1 - \lim\limits_{x \rightarrow b} F(x)$

**Erwartungswert:**
- Lagemass der Verteilung X
- Existiert nicht für jede Verteilung.
$$
E(X) = \sum\limits_{x \in \mathbb{R}}
P(X = x) \cdot x
$$
**Varianz:**
$$
V(X) = E([X - EX(X)^2)
=
\sum\limits_{x \in \mathbb{R}}
$$
**Standardabweichung:**
$$
S(X) = \sqrt{V(X)}
$$
## Bedingte Wahrscheinlichkeit
**Multiplikationssatz:**$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$
**Satz der totalen Wahrscheinlichkeit:** $P(A) = P(A|B) \cdot P(B) + P(A| \overline{B}) \cdot P(\overline{B})$
**Satz von Bayes:**$P(A|B) = \frac{P(B|A) \cdot P(B)}{P(B)}$
![[Pasted image 20230102134354.png]]

## Stochastische Unabhängigkeit
- Wenn $A$ und $B$ stochastisch unabhängig sind, beeinflusst das Eintreten des einen Ereignisses das Eintreten des des anderen Ereignisses nicht.
- 