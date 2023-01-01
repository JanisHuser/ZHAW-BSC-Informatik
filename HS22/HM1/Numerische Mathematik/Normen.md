# Vektornorm

## 1-Norm / Summennorm
$$
\left|
\left|
x
\right|
\right|_1

=
|x_1| + \cdots + |x_n|
$$
## 2-Norm / Euklidische Norm
$$
\left|
\left|
x
\right|
\right|_2

=
\sqrt{x_1^2 + \cdots + x_n^2}
$$
## $\infty$-Norm / Maximumnorm
$$
\left|
\left|
x
\right|
\right|_{\infty}

=
max
\{
\left|
x_1
\right|
,
\cdots
,
\left|
x_1
\right|
\}
$$

# Matrixnorm

## 1-Norm / Spaltensummennorm
$$
\left|
\left|
A
\right|
\right|
_1

=

max
\{
|a_{11}| + \cdots + |a_{n1}|
,
\cdots
,
|a_{1n}| + \cdots + |a_{nn}|
\}
$$
## 2-Norm / Spektralnorm
$$
\left|
\left|
A
\right|
\right|
_2

=

max
\{
\sqrt{
\lambda
| \lambda
\text{ ist Eigenwert von }
A^T \cdot A
}

\}
$$
## $\infty$-Norm / Zeilensummennorm
$$
\left|
\left|
A
\right|
\right|
_{\infty}

=

max
\{
|a_{11}| + \cdots + |a_{1n}|
,
\cdots
,
|a_{n1}| + \cdots + |a_{nn}|
\}
$$

````python
import numpy as np

A = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
])

# Unendlichkeitsnorm
norm = np.linalg.norm(A, np.inf)

print(f"inf-Norm der Matrix A: {norm}")
```