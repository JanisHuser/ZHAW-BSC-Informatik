# Stochastische Unabhängigkeit

Sei $ (\Omega, P) $ ein diskreter Wahrscheinlichkeitsbaum

## Definition

$$

P(A \cap B)
=
P(A) \cdot
P(B)
$$

# Stochastische Unabhängigkeit bei Zufallsvariablen 

## Definition

Zwei Zufallsvariablen
$ X: \Omega \rightarrow \mathbb{R} $
und
$ Y: \Omega \rightarrow \mathbb{R} $
heissen stochastisch unabhängig, falls gilt:

$$
P(X = x, Y=y) = P(X =x)
\cdot
P(Y=y)

\text{für alle}
x,y \in \mathbb{R}
$$

# Gemeinsame Verteilung

$$

f(x,y) = P(X = x, Y=y)

$$

Verbundverteilung von $ X $ und $ Y $.

## Satz

- Folgende Eigenshachften sind äquivalent.

(i). $ A $ und $ B $ sind stochastisch unabhängig
(ii). $ A $ und $ \Omega \\ B $ sind stochastisch unabhängig
(iii). $ \Omega \\ A $ und $ \Omega \\ B $ sind stochastisch unabhängig.

- Wenn $ A $ und $ B $ stochastisch unabhängig sind, beeinflusst das Eintreten des einen Ereignisses das Eintreten des anderen Ereignisses nicht

$$ P(B) \neq 0 $, so gilt $ P(A|B) = P(A) $$

$$ P(A) \neq 0 $, so gilt $ P(B|A) = P(B) $$

- Für stochastisch unabhängige Zufallsvariablen $ X $ und $ Y $ gilt:

$

E(X \cdot Y)
=
D(X)
\cdot
E(Y)

$

und

$
V(X + Y)
=
V(X)
+
V(Y)
$