![[Pasted image 20230101105818.png]]

## Absolute und relative Häufigkeitsfunktionen
Sei $(x_1, \cdots, x_n)$ eine STichprobe eines metrischen Merkmals.

**Empirische absolute Häufigkeitsfunktion**
$h: \mathbb{R} \rightarrow \mathbb{R}, h(x) =$ Anzahl der  $\le i \le n$ mit $x_i = x$ 

**Empirische relative Häufigkeitsfunktion (PMF)**
$f: \mathbb{R} \rightarrow [0, 1], f(x) = \frac{h(x)}{n}$


![[Pasted image 20230101111959.png]]
![[Pasted image 20230101112012.jpg]]

## Absolute und relative Summenhäufigkeit

### Für nichtklassierte Stichproben

Sei $(x_1, \cdots, x_n)$ eine Stichprobe eines metrischen Merkmals mit der absoluten Häufigkeitsfunktion $h(x)$ und der PMF $f(x)$.

#### Empirische absolute Summenhäufigkeit
$H: \mathbb{R} -> \mathbb{R}, H(x) =$ Summe aller $h(y)$ mit $y \le x$

#### Empirische relative Summenhäufigkeit / Kummulative Verteilungsfunktion (CDF)
$F: \mathbb{R} \rightarrow [0,1], F(x) =$ Summe aller PMF Werte $f(y)$ mit $y \le x$.

![[Pasted image 20230101112022.png]]
![[Pasted image 20230101112026.png]]


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
F(a_{i+1} - F(a_i))
}{
a_{i+1} - a_i
}
$$

# Kenngrössen

## Quantille, Perzentille, Quartille, Median
**q-Quantil:** Wenn der Anteil der Stichprobenwerte $\lt R$ mindestens $q$ und der Anteil der Stichprobenwerte $\gt R$ mindestens $1-q$ ist.
**Perzentil: $p$** $100/p Quantil$

### Wenn $z = n \cdot q$ eine ganze Zahl
$$
R_q = \frac{1}{2} (x_z + x_{z+1})
$$
### Wenn $z = n \cdot q$ keine ganze Zahl
$$
R_q = x_{z}
$$
## Boxplot
**Quartilsabstand**: $Q_3 - Q_1$
**Untere Antenne:** $\ge Q_1 - 1.5 (Q_3 - Q_1)$
**Obere Antenne:** $le + 1.5(Q_3 - Q_1)$
![[Pasted image 20230101165432.png]]

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


