# Elementare Wahrscheinlichkeitsrechnung


## Erwartungswert
Der Erwartungswert ist ein Lagemass der Verteilung von X. Existiert nicht für jede Verteilung.

$$
E(X) = \sum\limits_{x \in \mathbb{R}}
P(X = x) \cdot x

=

\sum\limits_{ \omega \in \Omega}
P({ \omega }) \cdot X(\omega)

$$

## Varianz

$$

V(X) = E([X - E(X)]^2)
= 
\sum\limits_{x \in \mathbb{R}}
P(X = x) \cdot [x - E(X)]^2
=

\sum\limits_{\omega \in \Omega} P({ \omega }) 
\cdot
[
	X(\omega) - E(X)
]^2

$$

## Standardabweichung

$$
S(X) = \sqrt{V(X)}
$$

## Wichtige Eigenschaften

### Linearität

$$
E(X+Y) = E(X) + E(Y) 
$$

$$
E(\alpha X) = \alpha E(X)
\text{, mit } \alpha X \in \mathbb{R}
$$


### Verschiebung für die Varianz

$$

V(X) = E(X^2) - E(X)^2
=
\left[

\sum\limits_{x \in \mathbb{R}}
P(X = x) \cdot x^2

\right]

-
E(X)^2

$$

$$

V( \alpha X + \beta) =
\alpha^2 \cdot V(X)
\text{mit}

\alpha, \beta \in \mathbb{R}

$$

## Tschebyscheff'sche Ungleichung


Im Allgemeinen gilt für die Verteilung einer Zufallsvariablen X, dass immer mindestens 75% der Werte im Bereich $ E(X) \pm 2 \cdot S(X)$ liegen

## Gauss'sche Normalverteilung
Bei iener normalverteielten Zufallsvariable liegen etwa 68% der werte im Bereich $ E(X) \pm S(X) $ und bereits etwa 95% im Bereich $ E(X) \pm 2 \cdot S(X) $.