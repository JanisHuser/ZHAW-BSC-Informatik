# Geometrische Interpretation

Eine Multiplikation mit der Einheitmatrix ändert die Matrix nicht.

$$
A \cdot E = A \\
E \cdot A = A
$$

Die Reihenfolge der Berechnungen muss beachtet werden.

$$
A \cdot B \neq B \cdot A
$$

## Beispiel


$$
A-X \cdot B = 3 \cdot X \\

X \cdot B + 3 \cdot X = A \\

X \cdot B + 3 \cdot \color{red}E \color{black}\cdot X = A \\

X \cdot B + X \cdot 3 \cdot E = A \\

X (B + 3E) = A \\

X (B+3E) \cdot (B+3E)^{-1} = A \cdot (B+3E)^{-1} \\

X = A \cdot (B+3E)^{-1} \\

$$