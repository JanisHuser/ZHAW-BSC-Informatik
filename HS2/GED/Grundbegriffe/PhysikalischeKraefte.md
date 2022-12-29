# Physikalische Kräfte

## Kräfte
$$
\overrightarrow{F} = m \overrightarrow{a}
$$
| Symbol               | Beschreibung   | Einheit         |
| -------------------- | -------------- | --------------- |
| $\overrightarrow{F}$ | Kraft          | N               |
| $m$                  | Masse          | kg              |
| $\overrightarrow{a}$ | Beschleunigung | $\frac{m}{s^2}$ |

### Eigenschaften
- Kräfte sind Vektoren

### Konstante Beschleunigung
$$
v(t) = v_0 + a(t-t_0)
$$
$$
s(t) = s_0 + v_0(t-t_0)+
\frac{a}{2}(t-t_0)^2
$$
#### Speziallfall $a=0, t_0=0$
$$
v(t)=v_0
$$
$$
s(t)=v_0 t
$$

##  Bewegung aus der Ruhe
```python
import numpy as np

# Beschleunigung
a = 1

# Startzeit
t0 = 0

# Position zum Zeitpunkt t0
s0 = 0

# Geschwindigkeit zum Zeitpunkt t0
v0 = 0


def v(t):
	return v0 + a*(t - t0)

def s(t):
	return s0 + v0*(t-t0) + a/2*(t-to)**2


t = 5
print (f"Velocity at t={t}: {v(t)}")
print (f"Position at t={t}: {s(t)}")
```

