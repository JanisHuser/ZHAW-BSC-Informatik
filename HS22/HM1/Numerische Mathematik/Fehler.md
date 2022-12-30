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

