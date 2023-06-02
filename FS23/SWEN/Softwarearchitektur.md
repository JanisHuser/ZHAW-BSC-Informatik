# Logische Architektur
Auftrennung in Module

## ISO 25010
Diese ISO Norm beschreibt, wie eine Software zu analysieren ist.
**Functional Suitability**
- Appropriateness
- Accuracy
- Compliance

**Reliability**
- Availability
- Fault tolerance
- Recoverability
- Compliance

**Performance efficiency**
- Timebehaviour
- Resourceutilisation
- Compliance

**Operation (Useability)**
- Appropriatenessrecogniseability
- Leranability
- Ease-of-use
- Helpfulness
- Attractiveness
- Technicalaccessibility
- Compliance

**Security**
- Confidentiality
- Integrity
- Non-repudiation
- Accountability
- Authenticity
- Compliance

**Maintainability**
- Modularity
- Reusability
- Analyzability
- Changeability
- Modification stability
- Testability
- Compliance

**Transferability**
- Portability
- Adaptability
- Installability
- Compliance

## Schnittstellen (Interfaces)

### Exportierte Schnittstellen
- Definieren angebotene Funktionalität
- Sind im Sinne eines Vertrags garantiert
- Definieren wie ein Modul verwendet werden muss
- Modul kann intern beliebig verändert werden, solange Schnittstellen gleich bleiben

### Importierte Schnittstellen
- Verwendet ein Modul andere Module, so importiert sie deren Schnittstellen
- Einzige Kopplung zwischen Modulen


### Kapselung und Austaschbarkeit
- Der Bausteil kapselt die Implementierung dieser Schnittstellen ab. Somit ist die Implementation unsichtbar für die Aussenwelt
- Daher kann dieser durch andere Bausteine **problemlos** ersetzt werden

## Güte einer Modularisierung

### Kohäsion
- Ein Mass für die Stärke des inneren Zusamenhangs
- Je höher die Kohäsion innerhalb eines Moduls, desto besser die Modularisierung
	- schlecht: zufällig, zeitlich
	- gut: funktional, objektbezogen

### Kopplung
- Ein Mass für die Abhängigket zwischen Modulen
- Je geringer die wechselseitige Kopplung zwischen den Modulen, desto besser die Modularisierung
	- schlechte: Globale Kopplung (Globale Daten)
	- akzeptabel: Datenbereichskopplung: (Referenz auf gemeinsame Daten)
	- gut: Datenkopplung (alle Daten werden beim Aufruf der Schnittstelle übergeben)

## Clean Architecture
### Entities
Kapseln die Business Rules gültig für das gesamte Unternehmen

### Use Cases
Beinhalten die Business Rules einer Anwendung, orchestriert die Verwendung der Entities

### Interface Adapters
Adapter für die Konvertierung von Daten aus Datenbank oder web

### Frameworks and Drivers
![[Pasted image 20230602171312.png]]

## N+1 View Model

### Logical View
- Welche Funktionalität bietet das System gegen aussen an?
- Wichtige Aspekte: Schichten, Subsysteme, Pakete, Frameworks, Klassen, Interfaces
- **UML: Systemsequenzdiagramme, Interaktionsdiagramme, Klassendiagramm, Zustandsdiagramme**

### Process View
- Welche Prozesse laufen wo und wie ab im System?
- Wichtige Aspekte: Prozesse, Threads, Wie werden Anforderungen wie Performance und Stabilität erreicht?
- **UML: Klassendiagramme, Interaktionsdiagramme, Aktivitätsdiagramme**

### Development View (Implementation View):
- Wie wurde die logische Struktur (Layer, Schichten, Komponenten) umgesetzt?
- Wichtige Aspekte: Source Code, Executables, Artefakte
- **UML: Paketdiagramme, Komponentendiagramme**

### Physical View (Deployment View):
- Auf welcher Infrastruktur wird ein System ausgeliefert/betrieben?
- Wichtige Aspekte: Prozessknoten, Netzwerke, Protokolle
- **UML: Deployment Diagram**

### Scenarios (Use Cases)
- Welches sind die wichtigsten Use-Cases und ihre nichtfunktionalen Anforderungen? Wie wurden sie umgesetzt?
- Wichtige Aspekte: Architektonisch wichtige Ucs, deren nichtfunktionale Anforderungen und deren Implementation
- **UML: UC-Diagramm, Systemsequenzdiagramme, UC- Realisierungen**

![[Pasted image 20230602171531.png]]



## Paketdiagramme
![[Pasted image 20230602170946.png]]
