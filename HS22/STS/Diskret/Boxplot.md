# Boxplot

![](images/IMG_0206.jpeg)

| Beschreibung | Formelzeichen | Berechnung |
|--|--|--|
| unterer Whisker | | $$ \text{maximal, sonst Daten } Q_1 - 1.5 \bullet I_{QR} $$ |
| oberer Whisker | | $$ \text{maximal, sonst Daten } Q_3 + 1.5 \bullet I_{QR} $$ |
| 0.25 - Quantil | $$ Q_1 $$ | |
| 0.75 - Quantil | $$ Q_3 $$ | |
| Interquartilsabstand | $$ I_{QR} $$ | $$ Q_3 - Q_1 $$ |
| Median | $$ X_{med} $$ | |
| Modulo Wert | $$ X_{mod} $$ | höchster Stichprobenwert (Spitze der Kurve) | 

## Quantil

### Wenn n*q eine ganze Zahl ist

$$

R_q = \frac{1}{2} \bullet ( X_{n\bullet q} + X_{n \bullet q + 1})

$$

### Wenn n*q keine ganze Zahl ist

$$

X_{| n \bullet q |}

\text{mit } | n \bullet q| \text{ die nächstgrössere Zahl}
$$

## Boxplot in einer Klasse

1. CDF in der Verteilung berechnen
2. Klasse auswählen für die F(a) ≤ q < F(b)

$$

\frac{F(b) - F(a)}{b-a} = \frac{q - F(a)}{R_q - a}
$$

### Nach Rq umgestellt

$$

R_q = a + \frac{b-a}{F(b)-F(a)}[q - F(a)]

$$

## Median
Der in der Mitte liegende Wert einer sortiereten Datenmenge
### Wenn n gerade

$$
x[\frac{n+1}{2}]
$$

### Wenn n ungerade

$$

\frac{1}{2} [X_{[\frac{n}{2}]} + X_{[\frac{n}{2} + 1]}]

$$