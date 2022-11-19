# Integrationsregeln


|Ableitung|Ausgangsfunktion|Stammfunktion|
|---------|-----|---|
|$$f'(x)\\[|\\]f(x)\\[|\\]\int f(x)dx\\]
|$$0$$|\\]c \thickspace c \in \R$$|\\]cx$$
|$$r \cdot x^{-1}$$|\\]x^r$$| \\[ \frac{x^{r+1}}{r+1}\\]
|\\[-\frac{1}{x^2}\\[| \\[ \sqrt{x} =  x ^{\frac{1}{2}}\\[| \\[ \frac{2}{3}x^{\frac{3}{2}}\\[|
|\\[ \cos{x}\\] | \\[ \sin{x} \\[| \\[- \cos{x}\\[|
| \\[- \sin{x} \\[| \\[ \cos {x} \\[| \\[ \sin{x} \\[|
| \\[1 + \tan^2{x}=\frac{1}{\cos^2{x}} \\[|$$\tan{x}\\[| \\[-\ln{\mid \cos{x \mid}}\\[|
| \\[e^x\\[| \\[e^x\\[| \\[e^x\\[|
|\\]c \cdot e^{cx} \\[| \\[e^{cx} \\[| \\[ \frac{1}{c} \cdot e^{cx} \\[|
| \\[ \ln{a} \cdot a^x\\[| \\[a^x \\[| \\[ \frac{a^x}{\ln{a}} \\[|
|\\]\frac{1}{x} \\[|\\]\ln{x}\\[| \\[x(\ln \mid x \mid -1) \\[|
| \\[ \frac{1}{\ln{a} \cdot x} \\[|\\]\log_a{\mid x \mid}\\[| \\[ \frac{x}{\ln{\mid x \mid} -1 } = x(\log_a{\mid x \mid - \log_a{e}})$$|
|\\[ \frac{1}{\sqrt{1-x^2}}\\[| \\[ \arcsin{x} \\[| \\[x \cdot \arcsin{x} + \sqrt{1-x^2}$$|
|\\[-\frac{1}{\sqrt{1-x^2}}\\[| \\[ \arccos{x} \\[| \\[x \cdot \arcsin{x} - \sqrt{1-x^2}$$|
|\\[ \frac{1}{1+x^2}\\[| \\[ \arctan{x} \\[| \\[x \cdot \arctan{x} - \frac{1}{2} \ln{(1+x^2)}$$|

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