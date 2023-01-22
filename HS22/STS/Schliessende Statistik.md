## Schätzfunktion
$$
\Theta = g(X_1, ..., X_n
$$
**Grundgesamtheit:** $\theta$ 
**Erwartungsgetreu:** $E(\Theta) = \theta$
**Konstistent:** $E(\Theta) \rightarrow \theta$ und $V(\Theta) \rightarrow 0$

|                    | Schätzfunktion                                                         | Schätzwert                                                                                                                                                                  |
| ------------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Erwartungswert     | $\overline{X} = \frac{1}{n} \cdot \sum\limits_{i=1}^n X_i$             | $\mu = \overline{x} = \frac{1}{n} \cdot \sum\limits_{i=1}^{n}x_i$ <br/> $\hat{p} = \overline{x} = \frac{1}{n} \cdot \sum\limits_{i=1}^{n}x_i = \frac{\text{Anzahl 1en}}{n}$ |
| Varianz            | $S^2 = \frac{1}{n-1} \cdot \sum\limits_{i=1}{n}(X_i - \overline{X})^2$ | $\sigma^2 = s^2 = \frac{n}{n-1} \cdot \sum\limits_{i=1}^n (x_i - \overline{x})^2$                                                                                           |
| Standardabweichung | $S= \sqrt{S^2}$                                                        | $\hat{\sigma} = s = \sqrt{\frac{n}{n-1} \cdot \sum\limits_{i=1}^{n}(x_i-\overline{x})^2}$                                                                                                                                                                            |

## Vertrauensintervalle

|     | (1) Verteilung der Grundgesamtheit                                                                               | (2) zu schätzender Parameter | (3) Schätzfunktion                                                                                                                        | (4) zugehörige Standardisierte Zufallsvariable    | (5) Verteilung und benötigte Quantile                                                                                                                                   | (6) Zufallsvariablen für Intervallgrenzen                                                                                 |
| --- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1   | Normalverteilung (Varianz $\sigma^2$ bekannt)                                                                    | $\mu$                        | $\overline{X} = \frac{1}{n} \cdot \sum\limits_{i=1}^{n}X_i$                                                                               | $U = \frac{\overline{X}- \mu}{\sigma / \sqrt{n}}$ | Standardnormalverteilung <br/> (Tabelle 2) <br/> $c = u_p$ mit $p=\frac{1+\gamma}{2}$                                                                                   | $\Theta_u = \overline{X}-c \cdot \frac{\sigma}{\sqrt{n}}$ <br/> $\Theta_0 = \overline{X}+c \cdot \frac{\sigma}{\sqrt{n}}$ |
| 2   | Normalverteilung (Varianz $\sigma^2$ unbekannt und $n \le 30$; sonst Fall 1 mit $s$ als Schätzwert für $\sigma$) | $\mu$                        | $\overline{X} = \frac{1}{n} \cdot \sum\limits_{i=1}^{n}X_i$      <br/> $S^2= \frac{1}{n-1}\cdot \sum\limits_{i=1}^n(X_i- \overline{X})^2$ | $T=\frac{\overline{X}-\mu}{S/ \sqrt{n}}$          | $t$-Verteilung (Tabelle 4) mit $f = n-1$ <br/> $c=t_{(p;f)}$ mit $p = \frac{1+\gamma}{2}$                                                                               | $\Theta_u = \overline{X}- c \cdot \frac{S}{\sqrt{N}}$  <br/> $\Theta_o = \overline{X}+ c\cdot  \frac{S}{\sqrt{n}}$        |
| 3   | Normalverteilung                                                                                                 | $\sigma^2$                   | $\overline{X} = \frac{1}{n} \cdot \sum\limits_{i=1}^n X_i$ <br/> $S^2 = \frac{1}{n-1} \cdot \sum\limits_{i=1}^{n}(X_i - \overline{X})^2$  | $Z= (n-1)\frac{S^2}{\sigma^2}$                    | **Chi-Quadrat-Verteilung** (Tabelle 3) mit $f =n-1$ <br/> $c_1 = z_{(p_1;f)}$ mit $p_1 = \frac{1-\gamma}{2}$  <br/> $c_2 = z_{(p_2; f)}$ mit $p_2 = \frac{1+\gamma}{2}$ | $\Theta_u = \frac{(n-1) \cdot S^2}{c_2}$ <br/> $\Theta_o = \frac{(n-1) \cdot S^2}{c_1}$                                   |
| 4   | Bernoulli-Verteilung mit $n\hat{p}(1-\hat{p}) > 9$                                                               | $p$                          | $\overline{X} = \frac{1}{n} \cdot \sum\limits_{i=1}^{n}X_i$ <br/> $X_i$ 0/1-wertig mit $P(X_i= 1)=p$                                                                                                                                         |  $U = \frac{\overline{X}-p}{\sqrt{p(1-p)/n}}$                                                 |  **Standardnormalverteilung** näherungsweise (Tabelle 2) <br/> $c=u_q$ mit $q = \frac{1+\gamma}{2}$                                                                                                                                                                       |$\Theta_u = \overline{X}-c \cdot \sqrt{\frac{\overline{X} \cdot (1- \overline{X})}{n}}$ <br/> $\Theta_o = \overline{X} + c \cdot \sqrt{\frac{\overline{X} \cdot (1-\overline{X})}{n}}$                                                                                                                           |
| 5    | beliebig mit $n > 30$                                                                                                                  |   $\mu, \sigma^2$                           |    Wie im Fall 1 (gegebenenfalls mit $s$ als Schätzwert für $\sigma$) bzw. wie im Fall 3                                                                                                                           |

## Hypothesentests
Vorgehen bei einem Parametertest

1. Nullhypothese $H_0$ aufstellen
Um welchen Parameter geht es? Welchen Wert hat er angeblich? Oder werden zwei Parameter verglichen? 
2. Alternativhypothese $H_A$
 aufstellen
Kommt es darauf an, in welche Richtung die Abweichung geht? Ist dies der Fall, so beschreibt $H_A$ nur die relevante Alternative. 
3. Die richtige Zeile in der Tabelle "Übersicht über die wichtigsten Parametertests" finden
Welcher Verteilung folgt die Grundgesamtheit? Um welche Nullhypothese geht es? Welcher Fall liegt vor?
4. Kritische Grenzen bestimmen 
Dabei müssen wir Folgendes berücksichtigen: 
- Verteilung der Testvariablen gemäss Tabelle "Übersicht über die wichtigsten Parametertests" (letzte Kolonne)
- Signifikanzniveau $\alpha$
- Ist $H_A$ einseitig oder zweiseitig? Wenn einseitig, auf welcher Seite befindet sich der kritische Bereich?
5. Testwert berechnen 
gemäss Tabelle "Übersicht über die wichtigsten Parametertests" (vorletzte Kolonne). 
6. Testentscheidung fällen
Liegt der Testwert im Annahmebereich oder im kritischen Bereich?

## Übersicht über die wichtisgten Parametertests
![[Pasted image 20230122152035.jpg]]![[Pasted image 20230122152103.jpg]]