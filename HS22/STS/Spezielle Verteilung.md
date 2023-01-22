![[Pasted image 20230103114102.jpg]]


## Hypergeometrische Verteilung
**Anzal Ziehungen ohne Zurücklegen:** $n$
**Gesamtzahl aller Objete:** $N$
**Gesamtzahl aller Merkmalsträger:** $M$
$$
H \sim H(N, M, n)
$$
$$
P(X = x) =
\frac{
\begin{pmatrix}
M \\
x
\end{pmatrix}
\cdot
\begin{pmatrix}
N-M \\
n-x
\end{pmatrix}
}
{
\begin{pmatrix}
N \\
n
\end{pmatrix}
}
$$
$\mu = E(X) = n \cdot \frac{M}{N}$
$\sigma^2 = V(X) = n \cdot \frac{M}{N} \cdot \left(1 - \frac{M}{N}\right) \cdot \frac{N-n}{N-1}$
$\sigma = S(X) = \sqrt{V(X)}$
## Bernouilli Verteilung
$E(X) = E(X^2) = p$
$V(X) = p \cdot (1-p)$

## Binomialverteilung
**Anzahl Wiederholungen:** $n$
**Wahrscheinlichkeit für ein Ergebnis 1:** $p$
$$
X \sim B(n;p)
$$
$$
P(X = x)
=
\begin{pmatrix}
n \\
x
\end{pmatrix}
\cdot 
p^x
\cdot
(1-p)^{n-x}
$$
$q=1-p$
$\mu = E(X) = np$
$\sigma^2 = V(X) = npq$
$\sigma = S(X) = \sqrt{nqp}$
Wenn $n \le \frac{N}{20}$ : $H(N,M,n) \approx B(n, \frac{M}{N})$

## Poisson Verteilung
**Durchschnittliche Anzahl Ereignisse pro betrachtetets Zeitintervall:** $\lambda$
$$
X
\sim
Poi(\lambda)
$$
$$
P(X =x)
=
e^{-\lambda}
\cdot
\frac{\lambda^x}{x!}
$$
$\mu = E(X) = \lambda$
$\sigma^2 = V(X) = \lambda$
$\sigma = S(X) = \sqrt{\lambda}$
Wenn $n \ge 50$ und $p \le 0.1$: $B(n,p) \approx Poi(n \cdot p)$

## Gauss'sche Normalverteilung
$$
X \sim
N(\mu, \sigma)$$
**PDF:** $\varphi_{\mu, \sigma}(X) = \frac{1}{\sqrt{2 \pi} \cdot \sigma} \cdot e^{-\frac{1}{2}\left( \frac{x - \mu}{\sigma}\right)^2}$
![[Pasted image 20230103144839.png]]
**CDF:** $\phi_{\mu, \sigma}(x) =P(X \le x) = \int\limits_{-\infty}^{x} e^{-\frac{1}{2}\left( \frac{t-\mu}{\sigma} \right)^2}$ 
![[Pasted image 20230103150206.png]]
**Standardnormalverteilung:**$\mu=0$ und $\sigma =1$
$X \sim N(0; 1)$
$\varphi(x) = \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{1}{2} x^2}$

## Zentraller Grenzwertsatz
Alle unabhängigen Zufallsvariablen haben denselben Erwartungswert $\mu$ und dieselbe Varianz $\sigma^2$
**Summe:**$S_n= \sum\limits_{i=1}^{n}X_i = N(n \cdot \mu, \sqrt{2} \cdot \sigma)$
**Arithmetisches Mittel:** $\overline{X}_n = \frac{S_n}{n} = N(n \cdot \mu, \frac{\sigma}{\sqrt{n}})$
**Zufallsvariable:** $U_n = \frac{S_n - n \mu}{\frac{n} \cdot |sigma} = \frac{\overline{X}_n - \mu}{\frac{\sigma}{\sqrt{n}}}$

$E(S_n) = n \cdot \mu$
$V(S_n) = n \cdot \sigma^2$
$E(\overline{X_n}) = \mu$
$V(\overline{X_n}) = \frac{\sigma^2}{n}$
