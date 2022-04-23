# Gauss-Jordan Verfahren

1. Wir bestimmen die am weitesten links stehende Spalte mit Elementen ≠ 0- Wir nennen diese Spalte die **Pivot-Spalte**.
2. Ist die oberste Zahl in der Pivot-Spalte = 0, dann vertauschen wir die erste Zeile mit der obersten Zeile, in der Pivot-Spalte ein Element ≠ 0 hat.
3. Die oberste Zahl in der Pivot-Spalte ist nun eine Zahl a ≠ 0. Wir dividieren die erste Zeile durch a. So erhalten wir die **führende Eins**.
4. Nun wollen wir unterhalbt der führenden Eins lauter Nullen erzeugen. Dazu addieren wir passende Vielfache der ersten Zeile zu den übrigen Zeilen.
5. Wir lassen nun die erste Zeile aussen vor und wenden die ersten vier Schritte auf den verbleibenden Teil der Matrix an. Dieses Verfahren wiederholen wir so oft, bis die erweiterte Koeffizientenmatrix **Zeilenstufenform** hat.
6. Nun arbeiten wir von unten nach oben und addieren jeweils geeignete Vielfache jeder Zeile zu den darüber liegenden Zeilen, um über den führenden Einsen Nullen zu erzeugen.

## Beispiel
$$
\begin{rcases}
& & x_3 &+ 2x_4 &=3 \\
2x_1 &-4x_2 &+6x_3 &- 4x_4 &= -6 \\
-3x_1 &+ 6x_2 & & + x4 &= -10 \\
4x_1 &-8x_2 &+ x_3 & &=15
\end{rcases}
$$

$$

\left(
  \begin{matrix}
    0 & 0 & 1 & 2 \\
    2 & -4 & 6 & -4 \\
    -3 & 6 & 0 & 1 \\
    4 & -8 & 1 & 0 \\
  \end{matrix}
\left|
  \begin{matrix}
    3\\
    -6\\
    -10 \\
    15 \\
  \end{matrix}
\right)\right.
$$


1. Pivot ≠ 0

$$

\left(
  \begin{matrix}
    2 & -4 & 6 & -4 \\
    0 & 0 & 1 & 2 \\
    -3 & 6 & 0 & 1 \\
    4 & -8 & 1 & 0 \\
  \end{matrix}
\left|
  \begin{matrix}
    -6\\
    3\\
    -10 \\
    15 \\
  \end{matrix}
\right)\right.
$$

2. Zeile 1 (dividieren durch 2)

$$

\left(
  \begin{matrix}
    1 & - 2 & 3 & -2 \\
    0 & 0 & 1 & 2 \\
    -3 & 6 & 0 & 1 \\
    4 & -8 & 1 & 0 \\
  \end{matrix}
\left|
  \begin{matrix}
    -3\\
    3\\
    -10 \\
    15 \\
  \end{matrix}
\right)\right.
$$

3. Zeile (III) = 3*(I)+(III); (IV) = 4*(I)+(IV)


<span style='color:red;'>Freie Unbekante</span>
$$

\left(
  \begin{matrix}
    \color{lime}2 & \color{red}-2 & 3 & -2 \\
    \color{lime}0 & 0 & 1 & 2 \\
    \color{lime}0 & 0 & 9 & 5 \\
    \color{lime}0 & 0 & -11 & 8 \\
  \end{matrix}
\left|
  \begin{matrix}
    -3\\
    3\\
    -19 \\
    27 \\
  \end{matrix}
\right)\right.
$$

Auflösen bis folgende Matrix

$$

\left(
  \begin{matrix}
    1 & -2 & 3 & -2 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 \\
  \end{matrix}
\left|
  \begin{matrix}
    -3\\
    3\\
    2 \\
    0 \\
  \end{matrix}
\right)\right.
$$

### Resultierdends LSG
$$
x_1 -2x_3+3x_3 - 2x_4 = 3 \Leftrightarrow
x_1 = 3 + 2x_3 - 3x_3+ 2x_4 \\
x_3 + 2x_4 = 3 \\
x_4 = 2 \\

$$