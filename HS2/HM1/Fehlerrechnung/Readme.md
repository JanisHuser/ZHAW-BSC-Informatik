# Fehlerrechnung und Aufwandabschätzung
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

**Residium / Defekt**: $\Delta b$
**Fehler der Näherungslösung**: $\Delta x = \tilde{x} - x$

## $\varepsilon$ Rechnung 


# Absoluter Fehler

$$|\tilde{x} - x|$$

# Relativer Fehler

$$
\left|
\frac{\tilde{x}-x}{x}
\right|
$$


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
