### Software Architecture

#### Begriffe und Erklärungen

**Software-Architektur**
Die Software-Architektur beschreibt die grundlegenden Strukturen einer Softwareanwendung, einschließlich der Komponenten und deren Beziehungen zueinander. Sie umfasst die Entwurfsentscheidungen, die getroffen werden, um die funktionalen und nicht-funktionalen Anforderungen zu erfüllen.

**Software-Architekt**
Ein Software-Architekt ist verantwortlich für die Gestaltung und das Design der Software-Architektur. Dies beinhaltet die Entscheidung über die Struktur der Software, die Auswahl der Technologien und die Definition von Standards und Prinzipien, die das Entwicklungsteam befolgen soll.

**Unterschied zwischen Enterprise Architecture und Application Architecture**
- **Enterprise Architecture**: Umfasst die gesamte IT-Infrastruktur einer Organisation, einschließlich der Strategien, Prinzipien und Richtlinien, die zur Verwaltung der IT-Ressourcen verwendet werden. Sie zielt darauf ab, die IT-Umgebung mit den Geschäftszielen der Organisation in Einklang zu bringen.
- **Application Architecture**: Bezieht sich auf das Design und die Struktur einer einzelnen Softwareanwendung. Sie konzentriert sich auf die internen Komponenten der Anwendung und deren Beziehungen sowie auf die Integration mit anderen Systemen.

#### Schwierigkeiten des Software Designs

1. **Complexity (Komplexität)**:
   - Software-Systeme sind oft sehr komplex, was das Verständnis, die Entwicklung und die Wartung erschwert.

2. **Conformity (Konformität)**:
   - Software muss sich an externe Standards, Schnittstellen und Systeme anpassen, was die Flexibilität einschränkt und die Komplexität erhöht.

3. **Changeability (Änderbarkeit)**:
   - Anforderungen und Technologien ändern sich ständig, was die kontinuierliche Anpassung der Software erforderlich macht.

4. **Invisibility (Unsichtbarkeit)**:
   - Software ist immateriell und ihre Struktur ist oft schwer zu visualisieren, was die Kommunikation und das Verständnis erschwert.

#### Architectural Drivers

1. **Functional Requirements (Funktionale Anforderungen)**:
   - Beschreiben, was das System tun soll. Diese Anforderungen bestimmen die Funktionen und Features, die das System bieten muss.

2. **Non-Functional Requirements (Nicht-funktionale Anforderungen)**:
   - Beziehen sich auf die Qualitätseigenschaften des Systems, wie Leistung, Sicherheit, Zuverlässigkeit und Wartbarkeit. Diese Anforderungen beeinflussen die Architekturentscheidungen maßgeblich.

#### Begriffe und Unterschiede

**Standard**:
- Ein definierter und anerkannter Weg zur Durchführung einer Aufgabe oder zur Gestaltung eines Systems. Standards bieten Konsistenz und Interoperabilität.

**Style (Architekturstil)**:
- Ein Satz von Prinzipien, der zur Strukturierung und Organisation einer Softwarearchitektur verwendet wird. Beispiele sind Layered Architecture, Microservices und Event-Driven Architecture.

**Pattern (Architekturpattern)**:
- Wiederverwendbare Lösung für ein häufig auftretendes Problem in einem bestimmten Kontext. Beispiele sind Singleton, Factory und Observer.

**Layer vs. Tier**:
- **Layer (Schicht)**: Eine logische Trennung von Verantwortlichkeiten innerhalb einer Softwareanwendung. Beispiel: Präsentationsschicht, Geschäftsschicht, Datenschicht.
- **Tier (Ebene)**: Eine physische Trennung von Komponenten, die auf unterschiedlichen Maschinen oder Servern ausgeführt werden. Beispiel: Client-Server-Architektur, bei der der Client auf einer Maschine und der Server auf einer anderen Maschine läuft.

#### Architekturstile

**Layered Architecture**
- **Vorteile**: Einfach zu verstehen, gut strukturiert, ermöglicht die Trennung von Verantwortlichkeiten.
- **Nachteile**: Kann zu Leistungseinbußen führen, schwer zu ändern, wenn Schichten stark gekoppelt sind.

**Microservices Architecture**
- **Vorteile**: Skalierbarkeit, Flexibilität, Unabhängigkeit der Dienste, einfache Wartbarkeit.
- **Nachteile**: Komplexität der Verwaltung, erhöhtes Risiko der Netzwerkkommunikation, Datenkonsistenzprobleme.

**Event-Driven Architecture**
- **Vorteile**: Entkopplung von Komponenten, Skalierbarkeit, Echtzeitverarbeitung.
- **Nachteile**: Komplexität der Ereignisverwaltung, schwierige Fehlerbehandlung, Potenzial für inkonsistente Datenzustände.

**Monolithic Architecture**
- **Vorteile**: Einfacher zu entwickeln und bereitzustellen, weniger Überkopfkosten durch weniger Netzwerkkommunikation.
- **Nachteile**: Schwer skalierbar, schwierig zu warten und zu erweitern, potenziell längere Entwicklungszeiten bei Änderungen.

#### Drei große Patterns

1. **Transaction Script**:
   - **Einsatzgebiet**: Einfachere Anwendungen, bei denen Geschäftslogik direkt in Prozeduren oder Skripten implementiert wird.
   - **Vorteile**: Einfachheit, schnelle Entwicklung.
   - **Nachteile**: Schwer wartbar und erweiterbar bei wachsender Komplexität.

2. **Domain Model**:
   - **Einsatzgebiet**: Komplexere Anwendungen mit umfangreicher Geschäftslogik.
   - **Vorteile**: Bessere Wartbarkeit, Flexibilität, gute Abbildung von Geschäftsregeln.
   - **Nachteile**: Höhere Komplexität und Lernkurve.

3. **Table Module**:
   - **Einsatzgebiet**: Anwendungen, bei denen die Geschäftslogik eng mit der Datenbankstruktur verbunden ist.
   - **Vorteile**: Strukturierte Abbildung der Geschäftslogik auf Tabellenebene.
   - **Nachteile**: Kann zu einer engen Kopplung zwischen Geschäftslogik und Datenbank führen.

#### C4-Modell

Das C4-Modell bietet eine einfache Möglichkeit, Softwarearchitekturen auf vier Ebenen zu visualisieren:

1. **Context**:
   - Überblick über das System und seine Umgebung.
2. **Container**:
   - Darstellung der verschiedenen Container (Applikationen, Datenbanken, etc.) im System.
3. **Component**:
   - Details der Hauptkomponenten innerhalb eines Containers.
4. **Code**:
   - Details auf der Code-Ebene (Klassen, Methoden).

#### Architecture Canvas

**Vorteile**:
- Ermöglicht eine strukturierte Visualisierung und Planung von Architekturentscheidungen.
- Fördert die Zusammenarbeit und Kommunikation zwischen Teams.
- Bietet eine klare Übersicht über die wichtigsten Architekturkomponenten und -abhängigkeiten.

**Nachteile**:
- Kann bei großen Systemen unübersichtlich werden.
- Erfordert regelmäßige Aktualisierung und Pflege.

**Einsatz**:
- Wird verwendet, um die Architektur eines Systems zu planen, zu dokumentieren und zu kommunizieren.

### Zusammenfassung

Software-Architektur umfasst die grundlegenden Strukturen und Prinzipien, die zur Gestaltung und Verwaltung von Softwareanwendungen verwendet werden. Verschiedene Architekturstile und Patterns bieten spezifische Vorteile und Herausforderungen, die je nach Anwendungskontext berücksichtigt werden müssen. Das C4-Modell und das Architecture Canvas sind wertvolle Werkzeuge zur Visualisierung und Kommunikation von Architekturentscheidungen.