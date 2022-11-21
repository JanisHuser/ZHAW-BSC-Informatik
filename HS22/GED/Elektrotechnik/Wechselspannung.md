# Wechselspannung


| Beschreibung | Symbol | Einheit |
|---|--|--|
| Amplitude | $ U_0 $ | V |
| Freqzenz | $ v $ | Hz |
| Phasenversschiebung | $ \phi_0 $ | Grad / Rad |
| Kreisfreqzenz | $ \omega $ | Hz |


$$
U(t) = U_0 \sin{ ( 2 \pi v t + \phi_0) }
$$

```python,editable
import numpy as np

# Amplitude
U0 = 230

# Frequenz 
v = 50

# Phasenverschiebung [Grad]
phi0 = 0

# Zeit [s]
t = 0


print (U0 * np.sin(2*pi*v*t + phi0))
```


# Nennspannung

$$

U_{Nenn} = \frac{U_0}{\sqrt{2}}

$$


```python,editable
import numpy as np

# Amplitude 
U0 = 230

# Nennspannung
print (U0 / np.sqrt(2))

```