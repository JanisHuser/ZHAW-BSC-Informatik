# Klassischer Euler (Polygonzug-Verfahren)


![[Pasted image 20221205110924.png]]

- Anfangswerte sind bei gewöhnlichen Differentialgleichungen auf eine einfache Art numerisch zu lösen.

## Algorithmus

$$
y' = f(x,y) \text{ mit } y(a) = y_0
$$
$$
x_{i+1}=x_i+h
$$
$$
y_{i+1}= y_i+h \cdot f(x_i, y_i)
$$
$$
\text{ wobei } x_0 = a,
x_i = a +ih \text{ für } i=0,..,n-1
(n \in \mathbb{N})
\text{ und } h = \frac{b-a}{n}
$$
# Mittelpunk-Verfahren

Das klassische Euler-Verfahren beruht darauf, die Steigung  $ y'(x_i) $ am Punkt $ (x_i, y_i) $ zu berechnen und der Tangente in diesem Punkt eine Schrittweite h zu folgen. Beim Mittelpunktverfahren folgt man der Tangente nut die Halbe Schrittweite $ h/2$ und berechnet beim Mittelpunkt des Intervalls $ x_{h/2} = x_i + \frac{h}{2} $ die neue Steigung $ y_{h/2} $

$$
y_{h/2} = y_i+ \frac{h}{2}
\cdot
f(x_i, y_i)
$$

## Algorithmus

$$
x_{h/2} = x_i + \frac{h}{2}
$$
$$
y_{h/2} = y_i + \frac{h}{2} \cdot f(x_i, y_i)
$$
$$
x_{i+1} = x_i + h
$$
$$
y_i+1 = y_i + h
\cdot
f(x_{h/2}, y_{h/2})
$$
$$
\text{ wobei } x_0 = a,
x_i = a +ih \text{ für } i=0,..,n-1
(n \in \mathbb{N})
\text{ und } h = \frac{b-a}{n}
$$
# Modifiziertes Euler-Verfahren

1) Führe das klassische Euler-Verfahren durch und speichere die erste Tangentensteigung in der Variable $ k_1 $:
$$
x_{i+1} = x_i + h
$$
$$
y_{i+1}^{\text{Euler}} = y_i + h
\cdot
f(x_i, y_i)
$$
$$
k_1 = f(x_i, y_i)
$$
2) Berechne die zweite Tangentensteigung am Punkt $ (x_{i+1}, y_{i+1}^{\text{Euler}}) ) $
$$
k_2 = f(x_{i+1},  y_{i+1}^{\text{Euler}})
$$
3) Bilde den Durchschnitt der beiden Steigungen $ (k_1 + k_2) / 2 $ und mache einen Schritt $ h $ ausgehend vom ursprünglichen Punkt $ (x_i, y_i) $ zur Berechnung der Näherung $ ( x_{i+1}, y_{i+1}) $
$$
x_{i+1} = x_i +h
$$
$$
y_{i+1} = y_i + h
\cdot
\frac{(k_1 + k_2)}
{2}
$$
4) Wiederhole diese Schritte ausgehend von $ x_0 = a $ für $ x_i = a+ ih $ mit $ i=0,..,n-1 (n \in \mathbb{N}) $ und $ h = \frac{b-a}{n} $