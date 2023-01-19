# Fibonacci
The fibonacci Series is a steadily increasing series of numbers, where each number is the sum of the preceding two numbers.

	0, 1, 1, 2, 3, 5, 8, 13, 21, ...

$$
F_n = F_{n-1}+F_{n-2}
$$

## Bedingungen
- $F_0 =0$ 
- $F_1 = 1$

# Fakultät
$$
n! = 
1 \cdot 2 \cdot 3 \cdot ... \cdot n
=
\prod\limits_{k=1}^nk
$$
## Rekursiv definiert
$$
n! =
\begin{cases}
1, &n=0 \\
n\cdot (n-1)!, &n>0\end{cases}
$$

# Hanoi
![](https://media.geeksforgeeks.org/wp-content/uploads/tower-of-hanoi.png)

## Idea
- Shift *red* disk from 'A' to 'C'
- Shift *white* disk from 'A' to 'B'
- Shift *red* disk from 'C' to 'B'
- Shift *green* disk from 'A' to 'C'
$\begin{pmatrix}R&& \\W&& \\G&&\end{pmatrix}$$\rightarrow$ $\begin{pmatrix}&& \\W&& \\G&&R\end{pmatrix}$$\rightarrow$ $\begin{pmatrix}&& \\&& \\G&W&R\end{pmatrix}$ $\rightarrow$ $\begin{pmatrix}&& \\&R& \\G&W&\end{pmatrix}$ $\rightarrow$ $\begin{pmatrix}&& \\W&& \\G&&R\end{pmatrix}$$\rightarrow$$\begin{pmatrix}&& \\&R& \\&W&G\end{pmatrix}$ 

