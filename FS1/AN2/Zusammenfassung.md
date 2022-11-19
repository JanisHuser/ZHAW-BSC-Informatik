# Zusammenfassung

## Ableiten

|Ableitung|Ausgangsfunktion|Stammfunktion|
|---------|-----|---|
|$$f'(x)\\[|\\]f(x)\\[|\\]\int f(x)dx\\]
|$$0$$|\\]c \thickspace c \in \R$$|\\]cx$$
|$$r \cdot x^{-1}$$|\\]x^r$$| \\[\frac{x^{r+1}}{r+1}\\]
|\\[-\frac{1}{x^2}\\[| \\[\sqrt{x} =  x ^{\frac{1}{2}}\\[| \\[\frac{2}{3}x^{\frac{3}{2}}\\[|
|\\[\cos{x}\\] | \\[\sin{x} \\[| \\[- \cos{x}\\[|
| \\[- \sin{x} \\[| \\[\cos {x} \\[| \\[\sin{x} \\[|
| \\[1 + \tan^2{x}=\frac{1}{\cos^2{x}} \\[|$$\tan{x}\\[| \\[-\ln{\mid \cos{x \mid}}\\[|
| \\[e^x\\[| \\[e^x\\[| \\[e^x\\[|
|\\]c \cdot e^{cx} \\[| \\[e^{cx} \\[| \\[\frac{1}{c} \cdot e^{cx} \\[|
| \\[\ln{a} \cdot a^x\\[| \\[a^x \\[| \\[\frac{a^x}{\ln{a}} \\[|
|\\]\frac{1}{x} \\[|\\]\ln{x}\\[| \\[x(\ln \mid x \mid -1) \\[|
| \\[\frac{1}{\ln{a} \cdot x} \\[|\\]\log_a{\mid x \mid}\\[| \\[\frac{x}{\ln{\mid x \mid} -1 } = x(\log_a{\mid x \mid - \log_a{e}})$$|
|\\[\frac{1}{\sqrt{1-x^2}}\\[| \\[\arcsin{x} \\[| \\[x \cdot \arcsin{x} + \sqrt{1-x^2}$$|
|\\[-\frac{1}{\sqrt{1-x^2}}\\[| \\[\arccos{x} \\[| \\[x \cdot \arcsin{x} - \sqrt{1-x^2}$$|
|\\[\frac{1}{1+x^2}\\[| \\[\arctan{x} \\[| \\[x \cdot \arctan{x} - \frac{1}{2} \ln{(1+x^2)}$$|


## Wichtige Beispiele

$$
f \rightarrow f'
$$

$$
(\sin(2x))' = 2 \cdot \cos(2x)
$$

$$
(\sin^2{(x)}) = 2 \cdot \sin{x} \cdot \cos x
$$

## Substitutionsregel

Wenn Produkt vonrhanden links -> rechts
$$

\int_a^b
f(\varphi(x)) \cdot \varphi'(x)dx = \int_{\varphi(a)}^{\varphi(b)} f(x)dx
$$


Wenn **kein** Produkt vorhandne, rechts -> links
$$

\int_{\varphi^{-1}{b}}^{\varphi{-1}{a}}
f(\varphi{x}) \cdot \varphi'{(x)} dx

=
\int_a^b{f(x)dx}

$$

## Partielle Integration

Wenn **keine** (teilweise) Ableitung vorhanden ist

$$

\int f(x) g(x) dx = f(x) G(x) - \int f'(x) G(x) dx

$$

## Grenzwerte mit De L'Hospital
Wird verwendet um Grenzwerte der Form zu berechnen

\\[\frac{f(x)}{x}$$

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

### 1. Regel (Oberer Intervalstrecke)

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

### 2. Regel (Untere Intevalstrecke)

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

## Reihen

# Potenzreihen

<span style='color:red'>Entwicklungspunkt</span>
$$
\displaystyle\sum_{k=0}^\infty (x-\color{red}a\color{black})^k

=
a_0 (x-\color{red}a\color{black})^0 + a_1(x-\color{red}a\color{black})^1 + a_n(x-\color{red}a\color{black})^n
$$

### Taylorreihen

Eine beliebig oft differenzierbare Funktion und \\[a \in I$$

$$

f(x) = \displaystyle\sum_{k=0}^\infty (x-a)^k
\frac{f^{(k)}(a)}{k!}(x-a)^k

$$