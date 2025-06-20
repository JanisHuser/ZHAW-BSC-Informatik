# View

Eine View beinhaltet ein Screenshot, der immer aktuell ist, einer Tabelle mit einer Query.

## Vorteile
- Verbergen von Komplexität
- Logische Datenunabhängigkeit
- Vereinfachung
- Sicherheit

## Nachteile

### Performance
Die Sicht wird bei jeder Verwendung neu berechnet.

### Keine Sortierung
Sichen können nicht sortiert werden (d.h. es ist keine ORDER-BY-Klausel in Sichten erlaubt)

### Wildwuchs
In der Praxis ensteht oft ein Wildwuchs an Sichten, d.h. es brauch eine disziplinierte Organisation und Verwaltung der Sichten

## Update

Die Daten in einer View können nicht angepasst werden. Die Daten müssen in der Referenzierten Tabelle angepasst werden.

## Simple Views
Sind updatebar

Folgende Bedingungen müssen **alle** eintreffen:

- EXAKT ein Element im FROM Teil, welches entweder 
eine normale Tabelle oder ein updateable view sein muss

- Die View Definition darf nicht WITH, DISTINCT, GROUP BY, HAVING, LIMIT oder OFFSET im Hauptteil enthalten.

-  Die View Definition darf nicht Mengen Operationen (UNION, INTERSECT oder EXCEPT) im HAuptteil enthalten.

- Der SELECT Teil darf keine Aggregate, Fenster Funktionen oder Funktionen enthalten die Mengen ergeben.

## SELECT ALL

SELECT * erlaubt es alle Felder anzuzeigen.



### Update
Wird in der Basistabelle eine Spalte hinzugefügt oder entfernt, dann wird diese in der zuvor generierten View nicht angepasst.