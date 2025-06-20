# Würfe

## Waagerechter Wurf
![[WaagerechterWurf.excalidraw]]
### In X-Richtung
**Ortskoordinate**: $s_x=v_0t$
**Geschwindigkeit**: $v_x=v_0$
**Beschleunigung**:$a_x=0$

### In Y-Richtung
**Ortskoordinate**: $s_y = - \frac{gt^2}{2}+h_0$
**Geschwindigkeit**:$v_x = gt$
**Beschleunigung**:$a_y = g$

### Allgemein
**Wurfweite**: $S_w =v_0 \sqrt{\frac{2h_0}{g}}$
**Wurfdauer**: $\frac{2h_0}{g}$
**Aufprallwinkel**: $tan \beta = \frac{v_y}{v_x}$
**Bahngeschwindigkeit**: $v(t)= \sqrt{v_0^2+(gt_w)^2}$

# Schräger Wurf
![[SchraegerWurf.excalidraw]]
### In X-Richtung
**Ortskoordinate**: $v_0 \cdot cos(\alpha) \cdot t$
**Geschwindigkeit**: $v(x) = v_0 \cdot cos(\alpha)$
**Beschleunigung**: $a_x = 0$

### In Y-Richtung
**Ortskoordinate**: $s_x(t) = v_0 \sin cos(\alpha) \cdot t + 0.5 \cdot -g \cdot t^2$
**Geschwindigkeit**: $v(t) = v_0 \cdot sin(\alpha) -g t$
**Beschleunigung**: $a_y = -g$

### Allgemein
**Steigzeit**: $H=\frac{v_0^2 sin^2(\alpha)}{2g}+h$
**Steigzeit** $t_s = v_0 \cdot \frac{sin(\alpha)}{g}$
**Steighöhe**: $y_max =\frac{v_0^2 \cdot sin^2(\alpha)}{2g}$

```python
import math
# Wurfwinkel
alpha = 30

#Erdbeschleunigung
g = 9.81

# Abwurfgeschwindigkeit
v0 = 3

# Anfangshöhe
h0 = 0

print (f"Wurfhöhe {(v0**2 * math.sin(alpha)**2)/(2*g)+h0}")

print (f"Steigzeit {(v0**2 * math.sin(alpha)**2)/2*g})
```