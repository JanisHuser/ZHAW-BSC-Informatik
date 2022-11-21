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

**Residium / Defekt**: $ \Delta b $
**Fehler der Näherungslösung**: $ \Delta x = \tilde{x} - x $