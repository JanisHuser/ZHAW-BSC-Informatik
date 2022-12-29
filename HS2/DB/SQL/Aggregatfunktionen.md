# Aggregatfuntionen ohne Gruppierung

| SQL-Keyword | Beschreibung |
|--|--|
| COUNT | Zählt die Anzahl der Element |
| MAX | Maximaler Wert der Elemente |
| MIN | Minimaler Wert der Elemente |
| SUM | Summe aller Elemente |
| AVG | Durschnitt der Werte der Elemente |

## Count


COUNT(<AttributName>) zählt nur diejenigen Tupel, bei denen der Wert des Attributs nicht NULL ist.

COUNT(*) zählt alle Tupel, es gibt kein Tupel, bei dem alle Attribute gleichzeigit NULL sein können.

COUNT(**DISTINCT**}NAME): zählt die Anzahl verschiedener Namen

## Bestellumsatz pro Kunde, unabhängig von der einzelnen Bestellung

```sql
SELECT kdNR, SUM(menge * preis) AS UMSATZ
FROM Bestellposition JOIN Kaufhistorei ON bestNr = bNr
GROUP BY kdNr;
```

## Grösster Bestellumsatz

```sql
SELECT MAX(Umsatz) AS GroessterUmsatz
FROM (SELECT kdNR, SUM(menge * preis) AS UMSATZ
FROM Bestellposition JOIN Kaufhistorei ON bestNr = bNr
GROUP BY kdNr) AS x;
```

# Aggregatsfunktionen mit Gruppierung

## Reihenfolge der SQL Abfragen}

1. FROM
2. WHERE
3. GORUP BY
4. HAVING
5. SELECT
6. ORDER BY

## Having

Alle Sätze, wo alle numerischen Werte grösser als 2 sind:
```sql
HAVING COUNT(*) > 2
```