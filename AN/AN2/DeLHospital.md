# De l'Hospital
Wird verwendet um Grenzwerte der Form zu berechnen

$$ \frac{f(x)}{x}$$

$$

f,g: (a,b) \rightarrow \R
(- \infin \leq a \leq b \leq \infin)
$$

$$
g'(x) \neq 0 \forall x
$$

$$

\lim \limits_{x \to b}{
    \frac{f'(x)}{g'(x)}
}
=: c \in R
$$

## 1. Regel (Oberer Intervalstrecke)

Aus 
$$
\lim \limits_{x \to b}{f(x)}
=
\lim \limits_{x \to b}{g(x)} = 0
$$
oder
$$
\lim \limits_{x \to b}{f(x)}
=
\lim \limits_{x \to b}{g(x)} = \pm \infin
$$

folgt
$$
\lim \limits_{x \to b}{
    \frac{
        f(x)
    }
    {g(x)}
}
=c
$$

## 2. Regel (Untere Intevalstrecke)

Aus 
$$
\lim \limits_{x \to a}{f'(x)}
=
\lim \limits_{x \to a}{g'(x)} = 0
$$
oder
$$
\lim \limits_{x \to a}{f'(x)}
=
\lim \limits_{x \to a}{g'(x)} = \pm \infin
$$

folgt
$$
\lim \limits_{x \to a}{
    \frac{
        f'(x)
    }
    {g(x)}
}
=c
$$
