# Gauss'sche Normalverteilung


$$
X
\sim
N(\mu: \sigma)
$$

![[Pasted image 20221206121719.png]]

## Kummulative Verteilungsfunktion

$$
\Phi_{\mu, \sigma}(x)
=
P(X \leq x)
=
\int_{-\infty}^{x}
\rho_{\mu, \sigma}(t) dt
=
\frac{1}
{\sqrt{2 \pi \cdot \sigma}}
\cdot

\int_{- \infty}^{x}
e^{
-\frac{1}{2}
(
\frac{x - \mu}{
\sigma
}
)^2
}
dt
$$

## Standardnormalverteilung

$$
\rho (x)
=

\frac{1}{\sqrt{2 \pi}}
\cdot

e^{
-
\frac{1}{2}
x^2
}
$$

## Dichtefunktion

$$
\rho_{\mu, \sigma}
(x)
=

\frac{1}{
\sqrt{2 \pi \cdot \sigma}}
\cdot
e^{
-\frac{1}{2}
(
\frac{x - \mu}{
\sigma
}
)^2
}
$$

- symmetrisch bezüglich der Geraden $ x = \mu $
- Hat Wendepunkte an den Stellen $ \mu - \sigma $ und $ \mu + \sigma $
- Normiert
- Eine Änderung von $ \mu $ bewirkt eine Verschiebung in x-Richtung; je grösser $ \sigma $ ist, desto breiter und niedriger wird die Glockenkurve
- Für eine Zufallsvariable $ X \sim N(\mu; \sigma) $ gilt $ E(X) = \mu $ und $ V(X) = \sigma ^2 $