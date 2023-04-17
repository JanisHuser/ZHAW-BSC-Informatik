# Ethernet

## Klasse bestimmen
| Klasse | Addressbereich | Netzmaske |
|--|--|--|
| A | 0.0.0.0 - 127.255.255.255 | 255.X.0.0 |
| B | 128.0.0.0 - 191.255.255.255 | 255.255.X.0 |
| C | 192.0.0.0 - 223.255.255.255 | 255.255.255.X |

## Subnetzmaske berechnen
**Anzahl Clients**: $n$

**Anzahl Clients**: $b = n + 2$ Bits aus Tabelle lesen

**Maske**: $/(32 - b)$

| Bits  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Dezimal | 1 | 2 | 4 | 8 | 16| 32| 64|128|256|


| Wert | Alternative Schreibweise | Anzahl adressierbare Interfaces |
|--|--|--|
| 255 | /24 | 255 -2 |
| 254 | /23 | 512 - 2 |
| 252 | /22 | 1024 - 2 |
| 248 | /21 | 2048 -2 |
| 240 | /20 | 4096 -2 |
| 224 | /19 | 8192 -2 |
| 192 | /18 | 16384 -2 |
| 128 | /17 | 32768 - 2 |
| 0 | / 16 | 65536 -2 |

Wenn alternative Schreibweise nicht gegeben ist, dann wird anstelle von X 0 verwendet.