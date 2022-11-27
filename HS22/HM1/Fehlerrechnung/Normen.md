# Konditionszahl

$ \text{cond} ( A )  = ||A|| * ||A^1|| $

```python,editable
import numpy as np

A = np.array([
	[1, 2],
	[3, 4]
])

cond = np.linalg.cond(A)

print ("Konditionszahl", cond)

```

# Vektornorm

$$
	\left|
	\left|
	.
	\right|
	\right|
	:
	\mathbb{R}^n \rightarrow \mathbb{R}
$$

## Allgemein

-  $ ||.|| $ eine Norm, $ A \in \mathbb{R}^{n \times n} $ eine regüläer $ n \times n $ Matrix
- $ x, \tilde{x}, b, \tilde{b} \in \mathbb{R}^n $ mit $ Ax = b $ und $ A \tilde{x} = \tilde{b} $

**Dann gilt**:

- $ || x - \tilde{x} \leq ||A^{-1} ||
\cdot
\frac{||b- \tilde{b}||}{||b||} $
**Falls $ b \neq 0 $**: $ \frac{|| x - \tilde{x}}{||x||} \leq ||A|| \cdot ||A^{-1} ||
\cdot
\frac{||b- \tilde{b}||}{||b||} $



## Bedingungen
- $ ||x|| \geq 0 $ und $ ||x|| = 0 \Leftrightarrow x = 0 $
- $ || \lambda x || = \lambda ||x|| $
- Dreiecksgleichung: $ || x +y || \leq ||x|| + ||y|| $

## Vektornormen
Für Vektoren $ (x = x_1, x_2, ..., x_n )^T \in \mathbb{R}^n $ gibt es folgende Vektornormen:

### 1-Norm, Summenform

$
||x||_1 = \sum_{i=1}^n | x_i |
$

### 2-Norm, euklidische Norm

$$
||x||_2 = \sqrt{ \sum_{i=1}^n x_{i}^2 }
$$

### $ \infty $-Norm, Maximumnorm

$$
||A||_{\infty} = \max\limits_{i=1,…,n} |x_{i}|
$$
