Für Zahlen $x\geq 0$ gilt in der Mathematik immer $(\sqrt{x})^2 =x$. Auf Rechnern gilt dies meistens nicht.

# Ganze Zahlen
$$ n \geq 0 $$
$$
1+2+ ... + n-1 +n = n+ n-1 + ... + 2 + 1 = \frac{n \cdot (n+1)}{2}
$$
# Maschinenzahlen
Auf einem rechner können nur endlich viele relle Zahlen $\mathbb{R}$ abgespeichert werden. Sie heissen Maschinenzahlen $\mathbb{M}$.
Um eine Maschinenzahl zu speichern, muss diese meistens **gerundet** werden. Es entstehen **Rundungsfehler**.

## Stellenwertsystem
Zu jeder Basis B =2,34,... gibt es ein Stellenwertsystem
- Dezimalsystem: B = 10, Ziffern 0-9
- Binärsystem: Basis = 2, Ziffern 0, 1

## Fixpunktzahlen

Ganzer Teil: 123.
Gebrochener Teil .45

## Normierte Gleitpunktzahlen
$$ 0.12345 \cdot 10^3$$Mantisse: 0.12345
Basis: 10
Exponent 3

$$
x = (\pm 0.m_1 m_2 m_3 m_n)_B \cdot B^{(\pm e_1 e_2 e_3 3_n)_B}
$$
**Mantisse**: $m=(\pm 0.m_1 m_2 m_3 m_n)_B$
**Exponent**: $e =(\pm e_1 e_2 e_3 3_n)_B$

## Norm IEEE 754

**Float64**: $x=(-1=^S \cdot (1+m) \cdot 2^{e-b}$

S: aus $\{0,1\}$
m: $(0.m_1 m_2 m_3 ... m_{52})_2$ mit $m_1, m_2, m_3,..., m_{52}$ aus $\{0, 1\}$
e: $(e_1,e_2,e_{11})_2$ mit $e_1, e_2, ..., e_{11}$ aus $\{0,1\}$ 
b: $(11'1111'1111)_2
![[Pasted image 20221229155820.png]]

### Normierung
Addition von 1

### Darstellung von negativen Zahlen
Es wird eine Zahl b (Bias) subtrahiert

### Null und subnormale Zahlen
Wenn alle Bits 0 sind.

### Unendlich
Alle Exponentbits 1 und alle Mantissebits 0

### Not a Number
Die 64 Bitfolgen mit Exponentenbits alle 1 und mindestens einem Mantissebit verschieden von 0