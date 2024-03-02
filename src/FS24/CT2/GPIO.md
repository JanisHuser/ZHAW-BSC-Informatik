# GPIO (General Purpose Input/Output)

- GPIOS sind allgemeine Anbindungen. Mit ihnen lassen sich digitale und analoge Signale lesen bzwh. schreiben.
- Die Pins können mit Code / Software konfiguriert werden
- Die meisten GPIO Pins haben eine alternative digitale oder analoge Funktion. Man kann also auswählen, was man braucht.

| Pin bezeichung | Beschreibung |
|----------------|--------------|
| GP | General purpose |
| PP | Push Pull |
| PU | Pull UP |
| PD | Pull Down |
| OD | Open Drain |
| AF | Alternate Function |

## Wechsel zwischen INput und OUTput

Wie bereits oben beschrieben, kann ein Pin mehrere Funktionen haben. Diese werden durch digitale Schalter konfiguriert.

| MODER\[1:\0] | Beschreibung |
|--------------|--------------|
| 00 | Input |
| 01 | General purpose output mode |
| 10 | Alternate function mode |
| 11 | Analog mode |

![alt text](media/image-3.png)

## Output Typen

### PUSH PULL

Der output kann entweder HIGH oder LOW, nichts dazwischen.

Dabei wird der Output, wenn dieser näher bei HIGH liegt, nach oben gezogen, also auf das HIGH Signal (x). Alternativ, wird dieses nach unten (in den meisten fällen auf das GND ) gezogen.


![alt text](media/image-4.png)

### Open Drain

Das Signal wird auf ein anderes Signal, in den meisten Fällen, auf GND gezogen. Und **NUR** auf das eine Signal.

## Port Geschwindigkeiten

| OSPEEDR\[1:0\] | Beschreibung |
|----------------|--------------|
| 00 | Low Speed |
| 01 | Medium Speed |
| 10 | High Speed |
| 11 | Very high speed |