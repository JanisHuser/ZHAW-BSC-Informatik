# Absoluter Fehler

$$
\left|
\tilde{x} - x
\right|
$$

# Relativer Fehler

$$
\left|
\frac{
\tilde{x} - x
}{x}
\right|

=
K(x_0)
\cdot
\left|
\frac{x - x_0}
{x_0}
\right|

$$

# Rundungsprinzipien

## 1. Prinzip
Eine reelle Zahl x wird auf die nächstgelegende Maschinenzahl $\tilde{x}$ gerundet (Rounding to Nearest)

## 2. Prinzip
Wenn es zwei gleich nah gelegene Maschinenzahlen gibt, wird entweder:

- Auf die betragsmässige grössere Maschinenzahl $\tilde{x}$ gerunde
- Auf diejenige Maschinenzahl $\tilde{x}$ mit gerader hinterster Stelle in der Mantisse gerundet.

```python
from Scripts.Fehlerrechnung import calc_err_rel, calc_err_abs

xr = 24700
x = 24680

print (f"absoluter Fehler: {calc_err_abs(x, xr)}")
print (f"relativer Fehler: {calc_err_rel(x, xr)}")
```

# Outputfehler

Der Fehler der beim Ausgang entsteht.

**Anwendung**: $\tilde{x}$ durch $\tilde{y}$ ersetzen, $x$ durch $y$ ersetzen

$f(x) = y$
$f(\tilde{x}) = \tilde{y}$

## Bei differnzierbarer Funktion

$$
\left|
\frac{\tilde{y}-y}{y}
\right|
\approx

\left|
\frac{f'(x) \cdot x}{f(x)}
\right|
\cdot

\left|
\frac{\tilde{x}-x}{x}
\right|

$$

# Konditionszahl
$$
K(x) =

\left|
\frac{f'(x) \cdot x}{f(x)}
\right|

$$

```python
from Scripts.Fehlerrechnung import calc_cond

f = "x**3" # Funktion
print (f"Konditionszahl k(x) = {calc_cond(f)}")
```

## Bewertung der Konditionszahl

### Gute Konditionierung
Wenn die Konditionszahl $k(x)$ **kleiner als 1** oder **nur wenig grösser als 1** ist, dann verkleinert sicht der relative Fehler bei Funktionsauswertung oder vergrössert sich nur leicht.
$$
K(X) < 10
$$

### Schlechte Konditionierung
Wenn die Konditionszahl $k(x)$ **viel grösser als 1** ist, dann vergrössert sich der relative Fehler bei Funktionsauswertung stark.
$$
K(x) > 100
$$

## Konditionszahl einer Matrix
$$
A \cdot x = b
$$
$$
A \cdot \tilde{x} = \tilde{b}
$$
$$
cond(A) =
\left|
\left|
A
\right|
\right|
\cdot
\left|
\left|
A^{-1}
\right|
\right|

$$
```python
import numpy as np

A = np.array([
    [2, 5, 0],
    [-2, 2, 6],
    [1, 0, 3]
])

print (f"Konditionszahl von A: {np.linalg.cond(A)}")
```

# Fehlerabschätzung

$$

\frac{
\left|
\left|
\tilde{x} -x
\right|
\right|
}{
\left|
\left|
x
\right|
\right|
}


\le

\frac{
cond(A)
}{
1 - cond(A)
\cdot
\frac{
\left|
\left|
\tilde{A} - A
\right|
\right|
}{
\left|
\left|
A
\right|
\right|
}
}

\cdot
\left(

\frac{
\left|
\left|
\tilde{A} - A
\right|
\right|
}{
\left|
\left|
A
\right|
\right|
}
+
\frac{
\left|
\left|
\tilde{b} - b
\right|
\right|
}{
\left|
\left|
b
\right|
\right|
}
\right)
$$

## Norm einer Matrix
