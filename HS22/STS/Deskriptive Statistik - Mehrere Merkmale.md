# Kovarianz und Korrelation
**Bivaariate**: $(x_1, y_1) \cdots (x_n, y_n)$
**Arithmetisches Mittel der quadrierten x-Merkmale:** $\overline{x^2} = \frac{1}{n} \sum\limits_{i=1}^{n} x_i$
**Arithmetisches Mittel der quadrierten y-Merkmale:** $\overline{y^2} = \frac{1}{n} \sum\limits_{i=1}^{n} y_i$
**Arithmetische Mittel des Produktes der x- und y-Merkmale:** $\overline{xy} = \frac{1}{n} \sum\limits_{i=1}^{n} x_i y_i$
**Varianz**: $\tilde{s_x}^2 = \overline{x^2} - \overline{x}^2$
**Standardabweichung:** $\tilde{s_x} = \sqrt{\tilde{s_x}^2}$

**(Empirische) Kovarianz:** $\tilde{s}_{xy} = \frac{1}{n} (x_i -\overline{x}) \cdot (y_i - \overline{y})$
**(Empirischer) Korrelationskoeffizient nach Pearson $\tilde{s_x} \neq 0$ und $\tilde{s_y} \neq 0$:** $r_{xy} = \frac{\tilde{s_{xy}}}{\tilde{s_x} \cdot \tilde{s_y}}$ 

## Interpretierung
| $r_{xy}$ | Bedeutung                                                        |
| -------- | ---------------------------------------------------------------- |
| $1$      | positiver Zusammenhang                                           |
| $-1$     | negativer Zusammenhang                                           |
| $\gt 0$  | Punkte liegen tendenziell um eine Gerade mit **positiver Steigung**. |
| $\lt 0$  | Punkte liegen tendenziell um eine Gerade mit **negativer Steigung**.                                                                 |


## Wichtige Eigenschaften
- $-1 \le r_{xy} \le 1$
- $\tilde{s}_{xy} = \overline{xy} = \overline{x} \cdot \overline{y}$
- $r_{xy} = \frac{\overline{xy} - \overline{x} \cdot \overline{y}}{\sqrt{\overline{x^2} - \overline{x}^2} \cdot \sqrt{\overline{y^2} - \overline{y}^2}}$

## Rangkorrelation
$rg(x_i)$: Arithmetisches Mittel der Indizes aller Stichprobenwerte $x_i$ in der ge
ordneten Stichprobe
$(6,3,4,3,3,2,6) = (2,3,3,3,4,6,6)$
$rg(2) =1$
$rg(3) = \frac{1}{3}(2+3+4)=3$

