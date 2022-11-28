# Common Table expressions

analog wie eine abgeleitete Tabelle oder eine Sicht - ein tempöräres Resultat einer Abfrage auf das in einer Tabelle


```sql
WITH cte_name (column_list) AS
(
	CTE_query_defiition
)
<query>;
```

```sql
WITH DSPpS AS (
	SELECT Strasse, AVG(Suppenpreis) AS DurchscnittsPreis
	FROM Restaurant
	GROUP BY STRASSE
)
SELECT Name, Suppenpreis, Durchschnittspreis
FROM Restaurant
JOIN DSPpS
ON Restaurant.Strasse = DSPpS.Strasse;
```

## Vorteile

- Grosse Queries besser stukturieren

- Abfragen besser lesbar, da die einzelnen Teilabfragen einen eigenen Namen haben,

- Mehr oder menschlichen Denkweise

- unterstützen rekursive Abfragen