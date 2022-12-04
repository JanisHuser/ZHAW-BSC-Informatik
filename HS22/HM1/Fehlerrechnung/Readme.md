# Fehlerrechnung und Aufwandabschätzung

- [Vektornormen](Vektornorm.md)
- [Matrixnorm](Matrixnorm.md)

$$
	Ax = b
$$

Aufgrund von den Ursachen wird nicht die exakte Lösung $ x $, sondern eine Näherungslösung $ \tilde{x} $ berechnet.

## Ursachen
- Rundungsfehler
- Eingabe und Messfehler
- Fehler aus vorgehenden Rechnungen

## Benachbartes Gleichungssystem
Formal wird ein "benachbartes" oder "gestörtes" Gleichungssystem eingeführt.
$$
A \tilde{x} = \tilde{b} = b+ \Delta b
$$

**Residium / Defekt**: $ \Delta b $
**Fehler der Näherungslösung**: $ \Delta x = \tilde{x} - x $

## $ \varepsilon $ Rechnung 

### Relativer Fehler

Relativer Fehler der Matrix A.
Ist immer positiv
$$

\frac{
	\left|
	\left|
	A - \tilde{As}
	\right|
	\right|
	_{\infty}
}
{
	\left|
	\left|
	A
	\right|
	\right|
	_{\infty}
}

$$

```python,editable
import numpy as np


A = np.array([
	[1,2],
	[3, 4]
])


As = A + np.random.rand(100, 100) / 1E5

rel_error = np.linalg.norm(A - As, order) / np.linalg.norm(A, order)

print ("Relativer Fehler", rel_error)

```

### Relativer Fehler in einem Bereich

$$

\frac{
	\left|
	\left|
	\tilde{x} - x
	\right|
	\right|
	_{\infty}
}
{
	\left|
	\left|
	x
	\right|
	\right|
	_{\infty}
}
\leq
cond(A) \cdot
\frac{
	\left|
	\left|
	\tilde{b} - b
	\right|
	\right|
	_{\infty}
}
{
	\left|
	\left|
	b
	\right|
	\right|
	_{\infty}
}

\leq
\text{(Relativer Fehler 1\% = 0.01)}

$$


```python,edtiable
import numpy as np

A = np.array([
	[1, 0, 2],
	[0, 1, 0],
	[1E-4, 0, 1E-4]
])

# Maximaler relativer Fehler 
max_rel_error = 0.01
order = np.Infinity

cond_a = np.linalg.cond(A)
print("Konditionszahl a", cond_a)
print ("Epsilon", max_rel_error / cond_a )
```

### Tatsächlicher Fehler

$$

\frac{
	\left|
	\left|
		\tilde{x} - x
	\right|
	\right|	
	_{
		\infty
	}
}
{
	\left|
	\left|
		x
	\right|
	\right|	
	_{
		\infty
	}
}

\leq

cond(A)
\cdot
(1 - \varepsilon)

\leq
error
$$

```python,edtiable
import numpy as np

A = np.array([
	[1, 0, 2],
	[0, 1, 0],
	[1E-4, 0, 1E-4]
])

# Maximaler relativer Fehler 
max_rel_error = 0.01
order = np.Infinity

cond_a = np.linalg.cond(A)
epsilon = max_rel_error / cond_a

print ("{a} ≤ (1 - {e})".format(a=cond_a, e=epsilon))

print("Resultat: ", (1-epsilon)/cond_a)
```