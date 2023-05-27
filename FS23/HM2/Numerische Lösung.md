## Skalarwertige Funktionen mit mehreren Variablen

- Eine Funktion mit $n$ unabhängigen Variablen $x_1, …, x_n$ und einer abhängigen Variablen $y$ versteht man eine Vorschrift, die jedem geordneten Zahlentupel ($x_1, x_2, …, x_n$) aus einer Definitionsmenge $D \in \mathbb{R}^n$ genau ein Element $y$ aus einer Wertemenge $\mathbb{W} \in \mathbb{R}$ zuordnet.
Symbolische Schreibweise:

$$
f: \mathbb{D} \in \mathbb{R}^n \rightarrow \mathbb{W} \mathbb{R}
$$
$$
(x_1,x_2,…,x_n) \mapsto y = f(x_1, x_2, …, x_n)
$$
- Da das Ergebnis $y \in \mathbb{R}$ ein Skalar (eine Zahl) ist, redet man von einer **skalarwertigen** Funktion.

## Partielle Ableitung
Für eine Funktion $f: \mathbb{R} \rightarrow \mathbb{R}$ mit einer Variablen ist die Ableitung an der Stelle $x_0$ bekanntlich definiert als:
$$
f’(x_0) = \lim\limits_{\Delta x \rightarrow 0}
\frac{
f(x_0 + \Delta x) - f(x_0)
}{
\Delta x
}
$$
Aus geometrischer Sicht entspricht dies der Steigung $m = f‘(x_0)$ der im Punkt $(x_0, f(x_0))$ angelegten Kurventangente
$$
t(x) = f(x_0) + f‘(x_0)(x- x_0)
$$

## Ableitung 1. Ordnung
