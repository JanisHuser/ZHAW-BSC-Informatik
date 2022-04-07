## Quadratische Matrizen

## Definition
Eine Matrix A heisst quadratisch, wenn sie gleich viele Zeilen wie Spalten hat (d.h. m=n).

Die Elemente $a_{11}$, $a_{22}$, $a_{mn}$ bildden dann die sogenannte Hauptdiagonale von A.


## Hauptdiagonale
Dort wo der Spaltenindex dem Zeilenindex entspricht.

$$\begin{pmatrix}
\ a_{11} & ...  & ... \\
\ ... & a_{22}  & ... \\
\ ... & ...  & a_{33} \\
\end{pmatrix}$$


## Arten von quadratischen Matrizen

### Obere Dreiecksmatrix
Alle Elemente unter der Diagonale sind = 0

$U = Upper$

$$\begin{pmatrix}
\ \color{red}1 & \color{red}2  & \color{red}5 \\
\ 0 & \color{red}4  & \color{red}5 \\
\ 0 & 0  & \color{red}6 \\
\end{pmatrix}$$


### Untere Dreieckesmatrix
Alle Elemente über der Diagonale sind = 0

$ L = lower $

$$\begin{pmatrix}
\ \color{red}1 & 0  & 0 \\
\ \color{red}4 & \color{red}6  & 0 \\
\ \color{red}7 & \color{red}8  & \color{red}0 \\
\end{pmatrix}$$

### Symetrische Matrix

$$\begin{pmatrix}
\ \color{red}1 & \color{red}4  & \color{red}6 \\
\ \color{red}4 & \color{green}2  & \color{green}5 \\
\ \color{red}6 & \color{green}5  & 3 \\
\end{pmatrix}$$

## Multiplikation mit der Einheitsmatrix


- Ändert eine Matrix nicht
$$ A \cdot E = A $$
$$ E \cdot A = E $$

## Potenzen einer Matrix
Für eine quadratische Matrix A definieren wir Potenzen wie folgt:

$$ A^0 = E $$

$$ A^k = A \cdot A \cdot A
(k \in N_{\geq1})$$

### Beliebiger Faktor
Gilt nur bei dieser Matrix
$$ a =
\begin{pmatrix}
1 & a\\
0 & 1\\
\end{pmatrix}
$$

$$ A^k 
=
\begin{pmatrix}
1 & \color{red}k*a\\
0 & 1\\
\end{pmatrix}

$$

#### Funktioniert bei dieser nicht
$$
A=
\begin{pmatrix}
1 & 2\\
-1 & 0\\
\end{pmatrix}
$$

$$
A^2 =
\begin{pmatrix}

\end{pmatrix}
$$