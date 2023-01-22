![[Pasted image 20230101105818.png]]

## Absolute und relative Häufigkeitsfunktionen
Sei $(x_1, \cdots, x_n)$ eine Stichprobe eines metrischen Merkmals.

**Empirische absolute Häufigkeitsfunktion**
$h: \mathbb{R} \rightarrow \mathbb{R}, h(x) =$ Anzahl der  $\le i \le n$ mit $x_i = x$ 

**Empirische relative Häufigkeitsfunktion (PMF / PDF)**
$f: \mathbb{R} \rightarrow [0, 1], f(x) = \frac{h(x)}{n}$

## Absolute und relative Summenhäufigkeit

### Für nichtklassierte Stichproben

Sei $(x_1, \cdots, x_n)$ eine Stichprobe eines metrischen Merkmals mit der absoluten Häufigkeitsfunktion $h(x)$ und der PMF $f(x)$.

#### Empirische absolute Summenhäufigkeit
$H: \mathbb{R} -> \mathbb{R}, H(x) =$ Summe aller $h(y)$ mit $y \le x$

#### Empirische relative Summenhäufigkeit / Kummulative Verteilungsfunktion (CDF)
$F: \mathbb{R} \rightarrow [0,1], F(x) =$ Summe aller PMF Werte $f(y)$ mit $y \le x$.

<div style="page-break-after: always;"></div>

## Eigenschaften der PMF und CDF

### Nichtklassierten Stichproben
- $0 \le f(x) \le 1$ und $0 \le F(x) \le 1$ für alle $x \in \mathbb{R}$
- $\sum\limits_{x=-\infty}^{\infty} f(x) = 1$ und $F(z) = \sum\limits_{x=-\infty}^{z} f(x)$
- Die DCF F(x) ist eine rechtsseitig stetige Treppenfunktion
- Monotinie: Aus $x \le y$ folg $F(x) \le F(y)$
- Es gibt reele Zahlen $a,b$ mit $F(a)=0$ und $F(b) = 1$
- Der Anteil aller Stichprobenwerte $x_i$ mit $x_i \le b$ ist $F(b)$
- Der Anteil aller Stichprobenwerte $x_i$ mit $a \lt x_i \le b$ ist $F(b) - F(a)$ 
- Der Anteil aller Stichprobenwerte $x_i$ mit $x_i > b$ ist $1 - F(b)$

## Klassierte Stichproben

**Klassenbreite:** $b_i$
**Relative Häufigkeiten:** $f_i = \frac{h_i}{n}$
**relative Häufigkeitsfunktion:** $g(x) = f_i$
**Empirische Dichtefunktion (PDF):** $f(x) = \frac{g(x)}{b_i}$
**Kumulative Verteilungsfunktion:** $F(X) = \sum\limits_{i=1}^{x} f(i)$
$$
b_i = \frac{F(i)-F(i-1)}{PDF}
$$
$$
a \lt x \le b \Rightarrow F(b) - F(a)
$$
$$
\frac{
F(x) - F(a_i)
}
{
x -a_i
}
=
\frac{
F(a_{i+1})- F(a_i)
}{
a_{i+1} - a_i
}
$$
$$
f(x) = \frac{f_i}{n \cdot d_i}
$$
<div style="page-break-after: always;"></div>

# Kenngrössen

## Quantille, Perzentille, Quartille, Median
**q-Quantil:** Wenn der Anteil der Stichprobenwerte $\lt R$ mindestens $q$ und der Anteil der Stichprobenwerte $\gt R$ mindestens $1-q$ ist.
**Perzentil: $p$** $100/p Quantil$

### Wenn $z = n \cdot q$ eine ganze Zahl

$$
R_q = \frac{1}{2} (x_z + x_{z+1})
$$

### Wenn $z = n \cdot q$ keine ganze Zahl ($z$ ist die nächstgrössere Zahl) 

$$
R_q = x_{z}
$$

## In einer Klasse
**Quantil:** $q$
**Wert bei q**: $R_q$
**Endwert der unteren Klasse:** $a$
**Endwert der oberen Klasse:** $b$

$$
\frac{
F(b) - F(a)
}
{
b-a
}
=
\frac{q-F(a)}
{R_q -a}
$$
$$
R_q =
a +
\frac{(b-a)}
{F(b) \cdot F(a)}
\cdot
(q - F(a))
$$
$$
q = \frac{(F(b) - F(a)) \cdot (R_q -a)}
{b -a} + F(a)
$$

## Boxplot

**Quartilsabstand**: $Q_3 - Q_1$
**Untere Antenne:** $\le Q_1 - 1.5 (Q_3 - Q_1)$
**Obere Antenne:** $\ge + 1.5(Q_3 - Q_1)$

![[Pasted image 20230101165432.png|500]]

<div style="page-break-after: always;"></div>

## Stichprobenmittelwert

**Klassenmitten:** $M_i = \frac{a_{i+1} + a_i}{2}$
**Stichprobenmittelwert:** $\overline{x} = \sum\limits_{i=1}^{m} M_i \cdot f_i$
**(Stichproben-)Varianz:** $\tilde{s}^2 = \sum\limits_{i=1}^{n} (M_i - \overline{x})^2 \cdot f_i$
**Korrigierte (Stichproben-)Varianz:** $s^2 = \frac{n}{n-1} \cdot \tilde{s}^2$
**(Stichproben-)Standardabweichung:** $\tilde{s} = \sqrt{\tilde{s}^2}$
**Korrigierte (Stichproben-)Standardabewichung:** $s = \sqrt{s^2}$

## Eigenschaften der Kenngrössen
**Linearität:** $\overline{x + y} = \overline{x} + \overline{y}$
**Verschiebungssatz für die Varianz:** $\tilde{s}^2 = \overline{x^2} - \overline{x}^2$
**Zusammenhang zwischen korrigieter und nichtkorrigierter Varianz:** $s^2 = \frac{n}{n-1}\tilde{s}^2$


