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
k(x) =

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
k(X) < 10
$$

### Schlechte Konditionierung
Wenn die Konditionszahl $k(x)$ **viel grösser als 1** ist, dann vergrössert sich der relative Fehler bei Funktionsauswertung stark.
$$
k(x) > 100
$$