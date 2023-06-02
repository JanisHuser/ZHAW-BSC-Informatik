Das Domänenmodell dient als Überblick der gesamten Anwendung. Dabei werden die Teile des Systems in unterschiedliche Blöcke getrennt. Diese Blöcke besitzen Attribute, die **IMMER** einen Bezug zur Welt des Anwenders besitzen, also keine ids, etc.

Die Verbindungen zwischen diesen Blöcken sind beschreibend, also Verben. Das Modell wird als **UML Klassendiagramm in einer vereinfachten Form** gezeichnet.

![[Pasted image 20230602162156.png]]

# Beziehungen

## Komposition
Ein Objekt kann ohne das andere (Parent) nicht existieren. Wird das Parent gelöscht, so stirbt auch das Kind. Ein Parent kann mehrere Kinder besitzen. (1 -> \*)

![[Pasted image 20230602162417.png]]

## Aggregation
Es besteht eine **hat** Beziehung. Ein Parent kann mehrere Kinder besitzen (1 -> \*) 
![[Pasted image 20230602162701.png]]

## Generalisierung / Spezialisierung
Eine Zusammenhang wird genauer definiert. Somit hat ein Typ nur noch die Funktionen, die **NUR** ihm zugeordnet werden können. Die **isA** Regel, sowie die **100%** Regel darf nicht verletzt werden.

isA: Ist ein
100%: Eine Spezialisierung darf nicht etwas anderes können, als die Kasse selber es könnte.

![[Pasted image 20230602162807.png]]

# Vorgehen
Die Vorgehensweise eines Kartografens wird angewendet, also zuerst das Grobe bestimmen / identifizieren und danach mit weiteren Details ausschmücken. Zudem wird unwichtiges weggelassen. Es wird **NUR** vorhandenes hinzugefügt.
1. Konzepte identifizieren
2. Konzepte mit Attributen versehen
3. Konzepte in Verbindung zueinander setzen

# Attribute

## Datentypen
Die meisten Attributtypen sind einfach (primitiv)
- Integer, float, boolean
- Werden im DB **normalerweise nicht angegeben**

## Konzepte
Sind in einer Klasse Attribute vorhanden, die normalerweise zu einem eigenen Typen gehören, oder sind diese mehrfach verwendet, so werden diese in Konzepte ausgelagert.

**Anwendung**:
- Der Type besteht aus mehreren Abschnitten (Adresse)
- Operationen darauf möglich sind, z.B. Validierung einer Kreditkartennummer
- Der Typ selber noch Attribute hat, z.B. ein Verkaufspreis der ein Anfangs- und Enddatum hat
- Der Typ mit einer Einheit verknüpft ist, z.B. ein Preis mit einer Währung

## Anti-Pattern
- Assoziationen anstelle von Attributen verwenden um Konzepte in Beziehung zueinander zu setzen.
- Keine Software Klassen im Domänenmodell, die es nicht in der Fachdomäne gibt. z.B. print(), toString(), …

## Beschreibungsklasse
Attribute, die für alle Artikel eines Typs gleich sind, werden in eine eigene Klasse herausgezogen.
