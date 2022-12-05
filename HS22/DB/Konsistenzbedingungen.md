# Konsistenzbedingungen

- Verhindern, dass falsche Daten in die Datenbank gelangen können

## Massnahmen zu Sicherstellung
- **Bereichsintegrität**: Der Wert eines Attributes muss in einem bestimmten Wertebereich liegen. Sichergestellt durch Datentypen / Domänen sowie *NULL* bzwh. *NOT NULL*.
- **Entitätsintegrität**: Der *Primärschlüssel* einer Tabelle mus eindeutig und immer vorhanden (*NOT NULL*) sein. Sichergestellt wurdch das RDBMS durch Definition einer nicht-leeren Attributmenge als Primary Key.
- **Referentielle Integrität**: Der Inhalt eines Fremdschlüssels muss entweder leer sein (*NULL*), oder genau eine Tupel, mit einem solchen Schlüsslwert, muss in der referenzierten Tabelle vorhanden sein.


## Einschränkungen, Constraints
Schränken die Menge der möglichen Datenwerte ein

- **UNIQUE**: Nebst Primär- und Fremdschlüsseln können weitere Schlüssel definiert werden.
- **CHECK**: Es können Regeln definiert werden, die Aussageb über Attribute einer Tabelle (genauer eines Tupels) festlegen
```sql
CONSTRAINT ck_artikel_ekpreis_vkpreis
CHECK (ekpreis >= 0 AND vkpreis >= ekpreis);
```
- **DEFAULT**:Es können Regeln definiert werden, welche Werte als Vorgabewerte verwendet werden sollen, falls für ein Attribut kein Wert geliefert wird.
```sql
CONTSTRAINT df_auftrag_datum DEFAULT SYSDATETIME();
```

## Komplexere Geschäftsregeln / Business Rules
- Zusammenhänge *zwischen Daten verschiedener Tabellen* herstellen


## Java IDBC

### Verbindung herstellen
```java
import java.sql.*;

// Datenbankverbindung konfigurieren
String url = "jdbc:postgresql://localhost/test";
Properties props = new Properties();
props.setProperty("user", "fred");
props.setProperty("password", "secret");
props.setProperty("ssl", "true");

// Verbindung initialisieren
Connection conn = DriverManager.getConnection(url, props);
```

### Query
```java
Statement st = conn.createStatement();
ResultSet rs = st.executeQuery("SELECT * FROM myTable WHERE columnfoo ==500");
while (rs.next()) {
	System.out.print("Column 1 returned");
	System.out.println(rs.getString(1));
}

rs.close();
st.close();
```
