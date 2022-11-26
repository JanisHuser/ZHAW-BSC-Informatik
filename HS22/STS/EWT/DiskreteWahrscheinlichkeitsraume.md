# Diskrete Wahrscheinlichkeitsräume $ (\Omega, P) $

## Ergebnisraum $ \Omega $
Menge aller möglichen Ergebnisse des betrachteten Zufallexperiments

## Zähldichte


Die Zähldichte ist eine Funktion 
$ \rho \rightarrow [0,1] $
, die jedem Ergebinis seine Wahrscheinlichkeit zuordnet.

Es gilt
$
1 = \sum\limits_{\omega \in \Omega} \rho( \omega)
$

## Ereignis

Eine Teilmenge von $ \Omega $

## Ereignisraum $ 2^{\Omega} $

Die Menge aller Teilmengen von $ \Omega $


## Wichtige Eigenschaften

### Unmögliches Ereignise
$$ P({}) = 0 $$

### Sicheres Ereignis

$$

P(\Omega) = 1

$$

### Komplementäres Ereignis

$$
P(\Omega \\ A) = 1 - P(A)
$$

### Vereinigung

$$

P(A \cup B) =
P(A) + P(B) - P(A \cap B)
$$

### Sigma-Additivität

Falls die Ereignisse paarweise disjunkt sind
$$
P(A_1 \cup A_2 \cup A_3 \cup ...)
=
P(A_1) + P(A_2) + P(A_3) + ....
$$