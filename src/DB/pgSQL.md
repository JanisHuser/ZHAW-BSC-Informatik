# PGSQL (Programmieren in SQL)

## Grundaufbau

### DECLARE
- Dklarationsblock für Variablen, Konstanten
- Der DECLARE Abschnitt ist Optional

### BEGIN
- Ausführungsteil

### EXCEPTION
- Ausnahmeverarbeitung
- Der *EXCEPTION* Abschnitt ist optional

END;

## Beispiel (Hallo Welt)
```sql
CREATE OR REPLACE FUNCTION HalloWelt() RETURNS void AS
$body$
BEGIN
	RAISE NOTICE 'Hallo Welt';
END;
$body$
LANGUAGE plpgsql;

-- Funktion ausführen
SELECT HalloWelt();

-- Funktion löschen
DROP FUNCTION HalloWelt();

```

## Variablen

```sql
DECLARE
	KNR INTEGER;
	ProdNr INTEGER := 0;         -- Initialisierung zu 0
	UserID Users.UserID%TYPE;    -- Typ von UserID kopieren
	Zeile users%ROWTYPE;         -- Ganze Zeile einer Tabelle kopieren
	name RECORD;                 -- untypisierte Zeile
```

## Eingebaute Funktionen

- **Konfigurationsfunktionen**: Geben Auskunft über den Zustand des Systems
- **Datum- und Zeitfunktionen**: Funktionen zur Bearbeitung von Daten und Zahlen
- **Mathematische Funktionen**: *sum()*, *avg()*
- **Metadaten-Funktionen**: *has_any_column_privilege(user, table, privilege)*
- **Zeichenfolgefunktionen**: *length(string)*, *lower(string*
- **Konversions- /Datenttypprüffunktionen**: *cast('100' as integer)*
- **Rangfolgefunktionen**: *rank()*

## Konstrollstrukturen

```sql
IF Boolean_expression
	{ sql_statement }
[ ELSE
	{sql_statement}
]
```

```sql
CASE
	WHEN Boolean_expression THEN { sql_statement }
	WHEN Boolean_expression THEN { sql_statement }
	ELSE -- DEFAULT
END
```

```sql
LOOP

EXIT WHEN Boolean_expression;
{ sql_statement }
END LOOP
```

```sql
WHILE Boolean_expression
BEGIN
	{ sql_statement }
END;
```

```sql
FOR counter in initial_value .. final_value LOOP
	{ sql_statement }
END LOOP;
```

## Cursor
- Ein Cursor erlaubt uns nicht das gesamte Ergebnis einer Query auf einmal zu verarbeiten, sondern Zeile um Zeile.
- Den jeweils aktuellen Datensatz kann man für bestimmte Operationen verwenden. So eignet sich ein Cursor dazu, eine bestimmte Aktion in gleicher Art und Weise uaf mehrere Zeilen hintereinander anzuwenden.


```sql
DECLARE cursor_name CURSOR
FOR {select statement}
[FOR UPDATE];
```


### Verwenden des Cursors

```sql
OPEN cursor_name; -- Cursor muss vor dem verwenden geöffnet werden

FETCH cursor_name
	INTO @variable1, @variable2, ...; -- Lesen der Daten in Variablen

CLOSE cursor_name; -- Cursor muss geschlossen werden
```

### Beispiel

```sql
CREATE OR REPLACE FUNCTION Show_AleBesuchernamen()
RETURNS VOID AS $$
DECLARE
	rec_Besucher record;
	c_Namen FOR SELECT Name, Vorname FROM Besucher;

BEGIN
	OPEN c_Namen;
	LOOP
		FETCH c_Namen INTO rec_Besucher;
		EXIT WHEN NOT FOUND;
		RAISE NOTICE 'Name % Vorname % ', rec_besucher.Name, rec_besucher.Vorname;
	END LOOP;
	CLOSEc_Namem;
END; $$
LANGUAGE pspgsql;
```

## Trigger

**Prinzip**: ECA
- **E**vent - **C**ondition - **A**ction

### Auslösung

- **BEFORE**: vor der DML-Operation
- **AFTER**: nach der DML-Operation
- **INSTEAD OF**: Anstelle der DML-Operation

### Einsatz
Sinnvoll, wenn
- Überprüfung / Funktion oft ausgefüht wird.
- SQL-Constraints nicht ausreichen
- Logik von der DB und nicht von den Anwendungsprogrammen durchgeführt weden soll.
- Lösung dadurch stark vereinfacht wird.

### Probleme
- Fehlerbehandlung
- Testen, Debuggen
- Gefahr der Unübersichtlichkeit
- Ergebnis von Triggeroperationen evtl abhängig vonder Aufrufreihenfolge
- Terminierung vone geschachtelten Triggeraufrufen

### Beispiel

```sql

-- Funktion für Trigger erzeugen
CREATE OR REPLACE FUNCTION log_Strasse()
RETURNS TRIGGER LANGUAGE PLPGSQL AS $$

BEGIN
	IF NEW.Strasse <> OLD.Strasse THEN INSERT INTO
		Adressänderung(Name, Vorname, StrasseAlt, StrasseNeu, Geändert_am)
		VALUES(OLD.Name, OLD.Vorname, OLD.Strasse, NEW.Strasse, now());
	END IF;
	RETURN NEW;
END; 

-- Trigger erzeugen

CREATE TRIGGER Strassenänderung
BEFORE UPDATE
ON Besucher
FOR EACH ROW
	EXECUTE PROCEDURE log_Strasse();

```


## Vergleich


#### Aufruf
|  Stored procedures / Functions | Trigger |
|--|--|
| Durch Benutzer oder Anwendungsprogramm | Durch DBMS, in Abhängigkeit von Datenänderungen |
| Transaktionskontrolle | Keine Transaktionskontrolle |

#### Einsatzbereiche
|  Stored procedures / Functions | Trigger |
|--|--|
| Kapselung von "business reules" | Konsistenzsicherung |
| Optimierung von Abfragen, Reduktion des Netzwerkverkehrs -> Batch Processing | Logging |
| Erhöhte Sicherheit benötigt | Nachführen von Tabellen |

#### Probleme
|  Stored procedures / Functions | Trigger |
|--|--|
| Fehlerbehandlung | Kompliziert zu testen |
| | Aufrufreihenfolge nicht determiniert |