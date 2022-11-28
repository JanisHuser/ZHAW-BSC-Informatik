# Data Devinision Language

Sturktur, nicht den Inhalt
- Erzeugen, Ändern, Löschen von Datenbanken, Tabellen und Beziehungen
- SQL Befehle: CREATE, ALTER, DROP

## Constraints

- CHECK
- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY

### Unterschied Unique Key und Primary Key

Unique erlaubt NULL Werte, Primary Key nicht

## Foreign Key Triggers

```sql
FOREIGN KEY
```

### NO ACTION

Keine Aktion ausführen

```sql
NO ACTION
```

### CASCADE

In allen Tabellen den Wert löschen

### SET NULL / DEFAULT

Den Wert NULL / Standard setzen

## Tabellen erstllen

### LIKE

- Erzeugt eine neue Tabelle *Besucher2* mit den gleichen Attributen wie Besucher
```sql
CREATE TABLE Besucher2 (LIKE Besucher)
```


### Tabelle einer Query erstellen

- Speichert die Resultate der Query in einer neuen Tabelle
- Übernimmt keine Constraints / Schlüssel, etc.

```sql

CREATE TABLE <tableName> AS (<query>);

```

#### Unterschied zur View

Die View zeigt die aktuellen Daten der Tabelle an, eine Tabelle mit einer Query ist ein Screenshot eines alten Standes.

## INSERT INTO


- Einfügen ganzer Resultattabellen
- Query muss kompatibelm mit tableName sein.
```sql
INSERT INTO <tableName> ( <query> );
```

## UPDATE

```sql
UPDATE <tableName>
SET <attributeName> = <attributeValue>
{, <attributeName> = <attributeValue>}
WHERE (<query>);
```


- Aufpassen, dass Primary Keys nicht überschrieben werden. (Duplikate)

## CASCADE
