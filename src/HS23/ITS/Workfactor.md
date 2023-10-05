# Workfactor

Denotes the average number of attepts needed to guess a secret.

$$
WF(X)
=
\sum
\limits_{k=1}^{n} k p_k
$$

## Work factor in bits

$$
\frac{\log(WF)}{\log{2}}
$$

## How long does it take to break a key

$$
t =
\frac{WF}
{\text{cpu freq} \times
\text{cycles per byte}}
$$