Ein Eigenwert (auch Eigenvalue genannt) ist ein Skalar, der die Veränderung einer Matrix beschreibt, wenn sie auf einen bestimmten Vektor angewendet wird. Ein Eigenraum ist die Menge aller Vektoren, die bei Anwendung der Matrix auf sie denselben Eigenwert ergeben.

Einfacher ausgedrückt: Ein Eigenwert ist ein spezieller Wert, der beschreibt, wie sich eine Matrix verändert, wenn man sie auf bestimmte Vektoren anwendet. Der Eigenraum ist die Menge aller Vektoren, die diesen Eigenwert ergeben.

$x^2+2x-3= 0$: $p=2$ und $q=3$

$$
x_{1,2} =
-
\frac{p}{2}
\pm
\sqrt{
\left(
\frac{p}{2}
\right)^2
-q
}
$$



## Charakteristische Form einer Matrix
```python
import numpy as np

# Beispielmatrix
A = np.array([
	[13, -4],
	[30, -9]
])

# Charakteristisches Polynom berechnen
p = np.poly(A)

# Polynom in erweiterte Form umwandeln
p = np.poly1d(p)

print (f"Charakteristische Form: {p}")
eigenvalues, eigenvectors = np.linalg.eig(A)

# Achtung -> Werte sind zu runden
print ("Eigenwerte", eigenvalues)
```

## Berechnen
- Nur möglich, wenn Matrix invertierbar ist.
$$
\left|
A - \lambda
\right|
=0
$$
```python
import numpy as np

# Define matrix
A = np.array([[2, 5], [-1, -2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Select eigenvector for eigenvalue of interest

def normalize_vector(vector):
    vector_length = np.linalg.norm(vector)
    normalized_vector = vector / vector_length
    return normalized_vector

for eigenvalue in eigenvalues:
    eigenvector = eigenvectors[:,0]
    normed = normalize_vector(eigenvector).T
    
    
    # Define linear combination of eigenvectors
    alpha = 2
    beta = 3
    eigenplane = alpha * eigenvector.T + beta * eigenvector.T

    print("Für den Eigenwert:", round(eigenvalue,4))
#     
    print("Eigenplane:", eigenplane)
```

## Schreibweise
**Eigenvektor**: $EV$
**Eigenraum**: $E$
**Faktor (nicht als Zahl angeben)**: $\mu$

$$
E_{\lambda_2} =
\{
x |
x =
\mu
\left(
EV
\right)
,
\mu
\in
\mathbb{R}
\}
$$

# Mises-Iteration
- Sei $A \in \mathbb{R}^{n \times n}$ eine diagonalisierbare Matrix mit den Eigenwerten $\lambda_1, ..., \lambda_n$ und dem betraggsmässig grössten Eigenwert $\lambda_1$ mit
$$
\left|
\lambda_1
\right|
\gt
\left|
\lambda_2
\right|
\ge
...
\ge
\left|
\lambda_n
\right|
$$
so konvergieren für (fast) jeden Startvektor $v^{(0)} \in \mathbb{C}^n$ mit Länge 1 die Folgen
$$
v^{(k+1)}
=
\frac{
Av^{(k)}
}
{
\left|
\left|
Av^{(k)}
\right|
\right|_2
}
$$
$$
\lambda^{(k+1)}
=
\frac{
(v^{(k)})^T
Av^{(k)}
}
{
(v^{(k)})^T
v^{(k)}
}
$$

für $k \rightarrow \infty$  gegen einen Eigenvektor $v$ zum Eigenwert $\lambda_1$ von A (also $v^{(k)} \rightarrow v$ und $\lambda^{(k)} \rightarrow \lambda_1$)

```python
import numpy as np
from Scripts.Eigen.MisesIteration import MisesIteration

# Define matrix
A = np.array([
    [1, 1, 0],
    [3, -1, 2],
    [2, -1, 3]
])

# Anfangsvektor
x = np.array([1, 0, 0])

mises_iteration = MisesIteration(A, x)

# Logging einstellen
mises_iteration.enable_log(True)

# Iteriere 4 mal
iterations = mises_iteration.iterate_n(4)

# Iteriere bis Differenz 0.01 getroffen
iterations = mises_iteration.iterate(0.01)
```