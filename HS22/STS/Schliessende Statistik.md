## Schätzfunktion
$$
\Theta = g(X_1, ..., X_n)
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
![[Pasted image 20230122152745.jpg]]

<div style="page-break-after: always;"></div>

## Hypothesentests
Vorgehen bei einem Parametertest

1. **Nullhypothese $H_0$ aufstellen**
Um welchen Parameter geht es? Welchen Wert hat er angeblich? Oder werden zwei Parameter verglichen? 
2. **Alternativhypothese $H_A$
 aufstellen**
Kommt es darauf an, in welche Richtung die Abweichung geht? Ist dies der Fall, so beschreibt $H_A$ nur die relevante Alternative. 
3. **Die richtige Zeile in der Tabelle "Übersicht über die wichtigsten Parametertests" finden**
Welcher Verteilung folgt die Grundgesamtheit? Um welche Nullhypothese geht es? Welcher Fall liegt vor?
4. **Kritische Grenzen bestimmen** 
Dabei müssen wir Folgendes berücksichtigen: 
- Verteilung der Testvariablen gemäss Tabelle "Übersicht über die wichtigsten Parametertests" (letzte Kolonne)
- Signifikanzniveau $\alpha$
- Ist $H_A$ einseitig oder zweiseitig? Wenn einseitig, auf welcher Seite befindet sich der kritische Bereich?
5. **Testwert berechnen** 
gemäss Tabelle "Übersicht über die wichtigsten Parametertests" (vorletzte Kolonne). 
6. **Testentscheidung fällen**
Liegt der Testwert im Annahmebereich oder im kritischen Bereich?

<div style="page-break-after: always;"></div>

## Übersicht über die wichtisgten Parametertests
![[Pasted image 20230122152035.jpg]]![[Pasted image 20230122152103.jpg]]