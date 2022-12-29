# Zufallsvariablen

Jede Funktion $ X: \Omega \rightarrow \mathbb{R} $, welche auf dem Ergebnisraum definiert ist und reelle Werte hat, heisst Zufallsvariable.

## Wahrscheinlichkeitsdichte (PMF)

$$

f: \mathbb{R} \rightarrow [0,1],
f(x) = P(X = x)
$$


## Kumulative Verteilungsfunktion (CDF)

$$

F: \mathbb{R} \rightarrow [0,1],
F(x) = P(X \leq x)

$$

## Wichtige Eigenschaften

$$
\sum\limits_{x=-\infty}^{\infty} f(x) = 1
$$

$$
F(z) = \sum\limits_{x=-\infty}^{z} = f(x)
$$

$$
\lim\limits{x \rightarrow \infty} F(x) = 1
$$

$$
\lim\limits{x \rightarrow -\infty} F(x) = 0
$$

### Montonie

Aus $ x\leq y$ folgt $ F(X) \leq F(y) $

$$
f(x) = F(X) - \lim\limits_{y \rightarrow \overline{x}} F(y)
$$


### Grenzbereich
$$
P(a \lt X \leq b) = F(b) - F(a)
$$

$$
P(a \leq X \leq b) = F(b) - \lim\limits_{x \rightarrow \overline{a}} F(x)
$$

### Grösser als
$$
P(X \gt b) = 1 - F(b)
$$

$$
P(X \gzt b) = 1 - \lim\limits_{x \rightarrow \overline{b}} F(x)
$$

