# Probleme


## Auswahl im Select, wo ColumnName mit ColumnName direkt verglichen wird
```sql
SELECT *
FROM Besucher
WHERE EXISTS (SELECT 1
  FROM Besucher
  WHERE Vorname=Vorname AND
  NOT (Name=Name));
```

## Subqueries (in WHERE) mit EXISTS

```sql
SELECT *
FROM Besucher AS x
WHERE EXISTS (SELECT 1
  FROM Besucher AS y
  WHERE x.Vorname=y.Vorname AND
  NOT (x.Name=y.Name));
```

Kreuzprodukt + Selektionsprädikat für gemeinsame Attrivute + autom. Umbenennung/Projektion von Attributen.

