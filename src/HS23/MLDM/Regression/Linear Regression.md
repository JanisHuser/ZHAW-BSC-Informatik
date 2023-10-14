# Linear Regression

## Closed Form 

Funktioniert nur mit univarianten Daten. Beruht auf der Ableitung von Varianzen.


### Normal Equation

Lässt sich für alle Probleme anwenden.

$$
\theta
=
(X^T X)^{-1}
X^T y

$$

### Runtime

![](images/Linear%20Regression/IMG_0260.jpeg)

- Mehr als 15'000 Features sind nicht möglich.

Matrix X ist: $X \in \mathbb{R}^{M \times N}$

Umgewandlet, bedeutet dass: $X^T X \in \mathbb{R}^{N \times N}$, wobei N die Features sind. Die Matrix wird dadurch riesig.

## Cost function

A cost function s a a measure, of how well a machine learning model performs by quantifiying the difference between predicted and actual outputs.

$$
J(\theta_0, \theta_1) =
\frac{1}{2M}
\sum\limits_{m=1}^{M}
(y_m - \hat{y}_m)^2
$$


Die Werte werden quadriert, um:

- Die Werte zu normieren
- Grosse Fehler werden verstärkt

### Optimaler Wert der Cost-Function

- Die Cost-Function ist genau dann 0, wenn alle Punkte **genau** auf einer Gerade sind.

- Der Fehler der Kostenfunktion soll so klein sein wie möglich, der Wert wird dabei einfach minimiert.

Mit der Normal Equation können wir die optimalen Theta Werte bestimmen.

## Hypothesis

$$
\theta_0(x)
$$
