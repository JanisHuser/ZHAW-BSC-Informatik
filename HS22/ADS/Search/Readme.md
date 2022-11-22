# Fast Search

## Beispiele
- Prüfen on ein Wort in einem Text vorkommt
- Zählen wie oft ein Wort in einem Text vorkommt
- Rechtschreibung
- Suchen allgemein

## Bedingungen


<span style="color:red">**Vorbedingung**</span>: Aussage, die **vor** dem Ausführen der Programmsequenz gilt

<span style="color:lime">**Nachbedingung**</span>: Aussage, die **nach** dem Ausführen der Programmsequenz gilt

$$
\textcolor{red}{ \{x >= 0 \} }
y = sqrt(x)
\textcolor{lime}{ \{y= \sqrt{x}, x >= 0 \}}
$$

## Invariane

Aussage, die über die Ausführung hinweg gültig bleibt.

All pre- and afterconditions are described used during the runtime of the algorithm.


### Schleifeninvariante

$$
\{

\forall x_i; i < k;  \textcolor{yellow}{ x_i \neq S} \}
$$


| Algorithmus | Zeitkonstante |
|--|--|
| Search in sorted array | $ O(\log_2 n) $ |
