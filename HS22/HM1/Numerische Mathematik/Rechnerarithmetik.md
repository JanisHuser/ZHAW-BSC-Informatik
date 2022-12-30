- Für Zahlen $x \geq 0$ gilt in der Mathematik immer $(\sqrt{x})^2 =x$
- Auf Rechnern dagegen gilt meistens nicht

# Stellenwertsysteme
- Zu jeder Basis B=2,3,4, ... gibt es ein Stellenwertsystem

**Dezimalsystem**: B=10, Ziffern 0-9
$$
(123.4)_{10}
=
1 \cdot 10^2
+
2 \cdot 10^1
+
3 \cdot 10^0
+
4 \cdot 10^{-1}
$$
**Binärsystem**: B=2, Ziffern: 0,1
$$
(1100.01)_2
=
1 \cdot 2^3
+
1 \cdot 2^2
+
0 \cdot 2^1
+
0 \cdot 2^0
+
0 \cdot 2^{-1}
+
1 \cdot 2^{-2}
$$

## Fixpunktzahlen
$$
123.45
$$
**Ganzer Teil**: $123$
**Gebrochener Teil: $45$

## Gleitpunktzahlen

$$
1.2345 \cdot 10^2
\text{ oder }
1234.5 \cdot 10^{-1}
$$

## Normierte Gleitpunktzahlen

$$
0.12345
\cdot
10^3
$$

**Mantisse**: $0.12345$ 
**Basis**: $10$
**Exponent**: $3$

Jede reelle Zahl $x$ ausser $0$ hat zu jeder Basis B eine normierte Gleitpunktdarstellung.

$$

x = (
\pm
0.
m_1
m_2
...
m_n
)_B

\cdot

B^{(
\pm
e_1
e_2
...
e_m
)_B}
$$

mit $m_1, m_2,m_..., m_n$ und $e_1,e_2,...,e_m$ aus $0,.., B-1$ und $m_1 \neq 0$

**Mantisse**: $m = (\pm 0. m_1 m_2 ... m_n)$
**Exponent**: $e=(\pm e_1 e_2 ... e_m)$

## Norm IEEE 754
Eine normale Maschinenzahl x von Float64 hat die Gestalt.
$$
x = (-1)^S
\cdot
(1+m) \cdot
2^{e-b}
$$

![[Pasted image 20221230092539.png]]

```python
S = 1
e = 0b10000000100
m = 2**-1 + 2**-3

le = 11 # Anzahl der Bits in e
b = 2**(le-1)-1 #

x = (-1)**S
x *= (1+m)
x *= 2**(e-b)

print(f"Resultat: {x}")
```

## Spezielle Zahlen
| Zahl                  | Signbit | Exponent | Mantisse                  |
| --------------------- | ------- | -------- | ------------------------- |
| 0                     | S       | 0 ... 0  | 0 ... 0                   |
| Subnormalle Zahlen (< 0)   | S       | 0 ... 0  | 0 ... 0 (Nicht alle 0) |
| Unendlich ($\pm inf$) | S       | 1 ... 1  | 0 ... 0                   |
| Not a Number          | S       | 1 ... 1  | $m_1$ ... $m_{52}$ (nicht alle 0)|

