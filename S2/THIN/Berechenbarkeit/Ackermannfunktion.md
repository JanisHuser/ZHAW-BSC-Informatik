# Ackermannfunktion

## Definition

$$
a: \N^2 \rightarrow \N
$$

$$
a(0,m) = m + 1
$$

$$
a(n + 1, 0) = a(n,1)
$$

$$
a(n+1, m+1) = a(n, a(n+1, m))
$$

## Einige Funktionswerte

| a(x,y) | 0 | 1 | 2 | 3 | 4 | 5 |
| ------ | --|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| 2 | 3 | 5 | 7 | 9 | 11 | 13 |
| 2 | ...
| 2 | ... 
| 5 | gross | gross | gross | gross | riesig | riesig

## Satz
- Die Ackermannfunktion "wächst schneller" als jede primitiv rekursive Funktion
- Die Ackermannfunktion ist nicht LOOP berechenbar / nicht primitiv rekursiv
- Die Ackermannfunktion ist total (überall definiert)

## Beweis
Für den Beweis, dass die Ackermannfunktion nicht primitiv rekursiv ist, geht man wie folgt vor:
- Definiere zu jeder primitiv rekursiven Funktion
    $$f$$ 
    eine Funktion 

    $$
    m(n,f) = 
    \max{
        \text{\textbraceleft}
        f(\overrightarrow(x)) |
        \Sigma \overrightarrow(x) \leq n
        \text{\textbraceright}
    }
    $$

- Zeige, dass