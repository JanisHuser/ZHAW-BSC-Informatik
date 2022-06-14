# Lineare Abbildungen

Es kommt nicht darauf an, ob wir zuerst komprimieren oder zuerst überlagern. Das Ergebnis bleibt gleich

$$
2Y' = Y''

$$

## Beispiele

$$
f(x) = x+5 \\
f(1+2) = (1+2)+5 = 8 \\
f(1) + f(2) = (1+5) + (2+5) = 13
$$

$$
f(x) = x^2 \\
f(2+3)= (2+3)^2 = 25 \\
f(2) + f(3) = 2^2 + 3^3 = 4 + 9 = 13
$$

$$
f(x) = e^x \\
f(2 \cdot 0) = e^{2 \cdot 0 } = e^0 = 1
$$

## Linear
$$
f: \R^2 \rightarrow \R^3:
\begin{pmatrix}
x_1 \\ x_2
\end{pmatrix}
\rightarrow

\begin{pmatrix}
x_1 - x_2 \\
3 x_2 \\
-4 x_1
\end{pmatrix}

$$


$$
(1): f(
    \begin{pmatrix}
    x_1 \\ x_2 \end{pmatrix}
 +
 \begin{pmatrix}
    y_1 \\ y_2
 \end{pmatrix})
$$

## Nicht linear
Sobald eine Verschiebung vorhanden ist, ist es nicht linear.
$$

f: \R^2 \rightarrow \R^3 \rightarrow

\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}

\color{red}
+
\begin{pmatrix}
-1 \\2
\end{pmatrix}
$$


## Abbildungsmatrix
- Die Bilder der Basisvektoren als Matrix werden benötigt
- f(x) = Ax, wobei A aus demn Bildern der Einheitsvektoren besteht.



### Beispiel
$$

\overrightarrow{e_1} \text{ und } \overrightarrow{e_2} \text{ sind gegeben}
$$
$$

f(\overrightarrow{x}) = f(x_1 \cdot \overrightarrow{e_1} + x_2 \cdot \overrightarrow{e_2}) \\
\text{Summe mit f kompatibel} \\

= f(x_1 \cdot \overrightarrow{e_1}) + f(x_2 \cdot \overrightarrow{e_2}) \\

\text{Skalare Multiplikation mit f kompatibel}
$$


