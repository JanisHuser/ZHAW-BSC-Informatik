# Vektornorm

\\[
	\left|
	\left|
	.
	\right|
	\right|
	:
	\mathbb{R}^n \rightarrow \mathbb{R}
\\]

## Bedingungen
- \\( ||x|| \geq 0 \\) und \\( ||x|| = 0 \Leftrightarrow x = 0 \\)
- \\( || \lambda x || = \lambda ||x|| \\)
- Dreiecksgleichung: \\( || x +y || \leq ||x|| + ||y|| \\)

## Andere Normen
Für Vektoren \\( x = x_1, x_2, ..., x_n)^T \in \mathbb{R}^n \\) gibt es folgende Vektornormen:

### 1-Norm, Summenform

\\[
||x||_1 = \sum_{i=1}^n | x_i |
\\]

### 2-Norm, euklidische Norm

\\[
||x||_2 = \srqrt{
	\sum_{i=1}^n x_{i}^2
}
\\]

### \\( \infty \\)-Norm, Maximumnorm

\\[
||A||_{\infty} = \max\limits_{i=1,…,n} |x_{i}|
\\]

## Matrixnormen
Für eine \\( n \times n \\) Matrix \\( A in \mathbb{R}^{n \times n })
### 1-Norm, Spaltensummennorm


\\[
||A||_1 = \max\limits_{i=1,…,n} \sum_{j=1}^n |a_{ij}|
\\]

### 2-Norm, Spektralnorm

\\[
||A||_2 = \srqt{ \rho \( A^T A \) }
\\]


### \\( \infty \\)-Norm, Zeilenssummennorm

\\[
||A||_{\infty} = \max\limits_{i=1,…,n} \sum_{j=1}^n |a_{ij}|
\\]



