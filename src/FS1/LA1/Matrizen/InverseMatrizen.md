# Inverse Matrizen


Die Inverse einer quadratischen Matrix A ist eine Matrix $$A^-1$$
für die gitlt:
$$
A*A^1 = A^1 * A = E$$

## Beispiel

$$
\begin{pmatrix}
6 & -2 & 3\\
23 & -8 & 12 \\
-14 & 5 & 7\\
\end{pmatrix}
*
\begin{pmatrix}
4 & -1 & 0\\
7 & 0 & 3 \\
-3 & 2 & 2\\
\end{pmatrix}

=

\begin{pmatrix}
6*4 +   (-2)*7 + 3*(-3) &
6*(-1) +(-2)*0 + 3*2 &
6*0 +   (-2)*3 + 3*2 \\

23*4 + (-8)*7 + 3*(-3) &
23*(-1) + (-8*0) 

6 & -2 & 3\\
23 & -8 & 12 \\
-14 & 5 & 7\\
\end{pmatrix}

=
\begin{pmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1 \\
\end{pmatrix}
$$

## Inverse einer 2 x 2 Matrix

Eine 2x2 Matriz hat genau dann einen Kehrwert, wenn folgendes gilt:
$$
ad-bc \neq 0
$$


$$
\begin{pmatrix}
a & b\\
c & d \\
\end{pmatrix}
^-1

=

\frac{1}{ad-bc}
* 
\begin{pmatrix}
d & -b\\
-c & a
\end{pmatrix}
$$

## Satz
Gegeben ist ein LGS
$$
A \cdot \overrightarrow{x} = \overrightarrow(c)
$$
mit n x n Koeffizientenmatrix A

### 1
 A ist invertierbar

### 2
Immer lösbar
$$A \cdot \overrightarrow{x} = \overrightarrow{c}$$

### 3
$$rg(A) = n$$


# Homogenes LGS

Ein LGS ist homogen, wenn die rechte Seite =
$$\overrightarrow{0}$$
ist


## Satz
Wenn A invertierbar ist, so hat das homogen LGS 
$$
A \cdot \overrightarrow{x} = \overrightarrow{0}
$$

die eindutige Lösung ist.

## Gauss-Jordan-Verfahren zur Berechnung der Inversen


Um die Inverse einer Matrix A zu bestimmen, müssen wir die MAtrixgleichung $$A \cdot X = E $$lösen.


### Beispiel

$$

A = 
\begin{pmatrix}
4 & -1 & 0 \\
0 & 2 & 1 \\
3 & -5 & -2 \\
\end{pmatrix}


\begin{pmatrix}
4 & -1 & 0 \\
0 & 2 & 1 \\
3 & -5 & -2 \\
\end{pmatrix} 

\cdot

\begin{pmatrix}
\color{red}x_{11} & \color{green}x_{12} & \color{blue}x_{13}\\
\color{red}x_{21} & \color{green}x_{22} & \color{blue}x_{23}\\
\color{red}x_{31} & \color{green}x_{32} & \color{blue}x_{33}\\
\end{pmatrix} 


\begin{pmatrix}
\color{red}x_{1} & \color{green}x_{0} & \color{blue}x_{0}\\
\color{red}x_{0} & \color{green}x_{1} & \color{blue}x_{0}\\
\color{red}x_{0} & \color{green}x_{0} & \color{blue}x_{1}\\
\end{pmatrix} 


$$