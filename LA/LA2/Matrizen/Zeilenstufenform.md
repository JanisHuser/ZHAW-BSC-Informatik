# Zeilenstufenform

Eine Matrix hat *Zeilenstufenform*, wenn folgende Bedingungen erfüllt sind:

- Alle Zeilen, die nur Nullen enthalten, stehen zuunterst (falls vorhanden)
- Wenn eine Zeile nicht nur aus Nullen besteht, so ist die vorderste Zahl ≠ 0 eine Eins. Sie wird als <span style="color:blue">führende Eins</span> der Zeile bezeichnet 
- Eine führende Eins, die weiter unten als eine andere führende Eins steht, steht auch weiter rechts.

### Beispiel

$$
\begin{pmatrix}
\color{blue}1 & 2 & 5 \\
0 & \color{blue}1 & 7 \\
0 & 0 & 0 \\
\end{pmatrix}
$$

## reduzierte Zeilenstufenform
Wenn die Matrix Zeilenstufenform hat und zusätzlich gilt:
- Jede Spalte, in der eine führende Eins steht, enthält sonst nur Nullen.


### Beispiel

$$
\begin{pmatrix}
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 0 \\
\end{pmatrix}
$$