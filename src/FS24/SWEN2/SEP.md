# SWEN2 Prüfungszusammenfassung

## Tidy First? (Buch von Kent Beck)
### Wichtigste Ideen und Konzepte:
- **Ordnung vor Funktionalität:** Die Grundidee ist, dass es einfacher ist, Änderungen in sauberem Code vorzunehmen.
- **Kontinuierliches Aufräumen:** Code sollte regelmäßig aufgeräumt werden, um technische Schulden zu vermeiden.
- **Empirisches Softwaredesign:** Entscheidungen sollten auf Grundlage von Erfahrungen und Experimenten getroffen werden.

## Einführung Softwareentwicklung
### SWEBOK:
- **Definition:** Software Engineering Body of Knowledge.
- **Inhalt:** Umfasst grundlegende Prinzipien, Praktiken und Techniken des Software Engineerings.

### Plangetriebene Methoden:
- **Vorteile:** Vorhersagbarkeit, klare Struktur und Dokumentation, gut für große, komplexe Projekte.
- **Nachteile:** Weniger Flexibilität, schwierig bei sich ändernden Anforderungen.
- **Einsatzgebiete:** Große, stabile Projekte mit klaren Anforderungen (z.B. Regierungsprojekte).

## Gesetze der Softwareentwicklung
### Drei Hauptgesetze:
- **Lehman's Laws:** Software altert und muss kontinuierlich weiterentwickelt werden.

### Weitere Gesetze:
- **Conway’s Law:** Systemdesign spiegelt die Kommunikationsstruktur der Organisation wider.
- **Brooks’s Law:** Hinzufügen von mehr Personal zu einem verspäteten Projekt verzögert es weiter.
- **Parkinson’s Law:** Arbeit dehnt sich aus, um die verfügbare Zeit zu füllen.
- **Pareto’s Fallacy:** 80% der Effekte kommen von 20% der Ursachen.
- **Sturgeon’s Revelation:** 90% von allem sind Schrott.
- **The Iceberg Fallacy:** Der größte Teil eines Problems ist unsichtbar.
- **The Peter Principle:** In einer Hierarchie steigt jeder bis zu seiner Inkompetenz auf.
- **Eagleson’s Law:** Jeder Programmierer verdoppelt den Speicherbedarf des Programms.
- **Greenspun’s 10th Rule:** Jede komplexe Software enthält ein schlechtes, in sich verborgenes Lisp.

## Agile Manifesto
### Values:
- **Individuen und Interaktionen über Prozesse und Werkzeuge.**
- **Funktionierende Software über umfassende Dokumentation.**
- **Zusammenarbeit mit dem Kunden über Vertragsverhandlungen.**
- **Reagieren auf Veränderung über das Befolgen eines Plans.**

### 12 Principles:
1. **Frühe und kontinuierliche Auslieferung wertvoller Software.**
2. **Begrüßen von sich ändernden Anforderungen.**
3. **Lieferung funktionierender Software häufig.**
4. **Tägliche Zusammenarbeit zwischen Geschäftsleuten und Entwicklern.**
5. **Projekte um motivierte Individuen herum aufgebaut.**
6. **Effektive Kommunikation von Angesicht zu Angesicht.**
7. **Funktionierende Software als wichtigstes Fortschrittsmaß.**
8. **Nachhaltige Entwicklung.**
9. **Technische Exzellenz und gutes Design fördern Agilität.**
10. **Einfachheit.**
11. **Selbstorganisierte Teams.**
12. **Regelmäßige Reflexion und Anpassung.**

## Agile
### Begriffe:
- **Risk:** Potenzielle Probleme, die den Projekterfolg beeinträchtigen könnten.
- **Cost of Change:** Der Aufwand, der nötig ist, um Änderungen am Projekt vorzunehmen.
- **Iron Triangle:** Die drei Variablen Scope, Time, und Cost beeinflussen sich gegenseitig.

## eXtreme Programming (XP)
### Core Values:
- Kommunikation, Einfachheit, Feedback, Mut, Respekt.

### Principles:
- Menschliche Werte, Wirtschaftlichkeit, gegenseitiger Nutzen, Selbstähnlichkeit, kontinuierliche Verbesserung.

### Practices:
- Planungsspiel, kleine Releases, Metapher, einfaches Design, Tests, Refactoring, Pair Programming, kollektive Code-Eigentümerschaft, kontinuierliche Integration, 40-Stunden-Woche, Vor-Ort-Kunde, Coding-Standards, TDD, Slack, Spike, inkrementelles Design, selbstorganisiertes Team.

## Software Craft
### Notwendigkeit und Prinzipien:
- **Notwendigkeit:** Reaktion auf mangelhafte Softwarequalität und -praktiken.
- **Formate:** Coding Dojo, Code Katas zur Übung und Verbesserung der Programmierfähigkeiten.
- **Community-Prinzipien:** Kontinuierliches Lernen und Teilen von Wissen.

## Pyramid of Agile Competencies
### Drei Ebenen:
- **Technische Praktiken:** Grundlagen wie Testen und Refactoring.
- **Team Praktiken:** Zusammenarbeit und Kommunikation.
- **Business Praktiken:** Kundenorientierung und Wertschöpfung.

## User Stories
### Ziele und Anwendung:
- **Ziele:** Verständnis der Nutzerbedürfnisse.
- **Anwendung:** Agile Planung und Priorisierung.
- **Format:** "Als [Rolle] möchte ich [Funktion], um [Nutzen]."
- **Zusammenhang:** Epics (große Stories), Themes (thematische Gruppierung), Stories (kleinere, umsetzbare Einheiten).
- **Merkmale:** Unabhängig, verhandelbar, wertvoll, schätzbar, klein, testbar.

## Estimation and Planning
### Begriffe:
- **User Stories, User Roles, Epics, Themes, Story Points, Velocity, Planning Poker, Conditions of Satisfaction, Levels of Planning, Product Backlog, Priorisierung.**
- **Schätzungstechniken:** Relativ, Planning Poker.
- **Planung für Wert:** Kosten, finanzieller Wert, Risiko, neues Wissen, Kano-Modell der Kundenzufriedenheit.

## Build Automation, CI, CD, DevOps
### Arten der Automatisierung:
- On-demand, scheduled, triggered.

### Pipeline:
- Schritte von Code-Commit bis Deployment.

## Scrum
### Charakteristika und Begriffe:
- **Scrum-Rollen:** Scrum Master, Product Owner, Team.
- **Scrum-Events:** Sprint, Daily Scrum, Review, Retrospektive.
- **Scrum-Artefakte:** Product Backlog, Sprint Backlog, Increment.
- **Scrum-Werte:** Mut, Fokus, Offenheit, Respekt, Commitment.

### Begriffe:
- **Sprint, Sprintziel, Retrospektive, Task Board, Burndown Chart, Definition of Done, Definition of Ready, Daily Scrum, Increment.**

## Architektur Patterns (Gruppenpuzzle)
### Patterns:
- **CQRS:** Trennung von Lese- und Schreiboperationen.
- **Event Sourcing:** Speicherung aller Zustandsänderungen als Ereignisse.
- **Strangler Pattern:** Schrittweise Ersetzung eines alten Systems durch ein neues.
- **Online-Migration:** Live-Migration von Daten.
- **Circuit Breaker:** Schutz vor Ausfällen durch Überlastung.
- **Bulkhead:** Isolation von Systemkomponenten.
- **Retry:** Wiederholungsmechanismen bei Fehlern.
- **Serverless:** Betrieb von Anwendungen ohne Verwaltung von Servern.
- **Microservices:** Modularisierung von Anwendungen in kleine, unabhängige Dienste.
- **Self-contained Systems:** Autonome Systeme mit eigener Datenhaltung.
- **Monolith (Modulith):** Großer, zusammenhängender Codeblock, der in Module aufgeteilt werden kann.

## Software Architecture
### Grundbegriffe:
- **Software-Architektur:** Struktur und Organisation eines Softwaresystems.
- **Software-Architekt:** Verantwortlich für das Design und die Integrität der Architektur.
- **Enterprise Architecture vs. Application Architecture:** Unternehmensweite vs. anwendungsspezifische Architektur.
- **Schwierigkeiten:** Komplexität, Konformität, Änderbarkeit, Unsichtbarkeit.

### Architectural Drivers:
- Faktoren, die die Architektur beeinflussen (Geschäftsanforderungen, technische Anforderungen).

### Standards, Stile, Patterns:
- Standardisierte Lösungen für wiederkehrende Probleme.
- Unterschiede zwischen Layer und Tier.

### Architekturstile:
- **Vor- und Nachteile von Stilen wie Monolith, Microservices.**

### Patterns:
- **Transaction Script:** Verarbeiten von Transaktionen durch einfache Skripte.
- **Domain Model:** Modellierung der Geschäftslogik.
- **Table Module:** Datenbanktabellen als zentrale Logikstrukturen.

### C4-Modell:
- Kontextsensitive Architekturmodellierung.

### Architecture Canvas:
- Werkzeug zur Visualisierung und Planung von Architekturen.

## Cynefin Framework / Codefin
### Begriffe:
- **Cynefin (Komplexitätsframework), Exaptation (Nutzung bestehender Strukturen für neue Zwecke), 4 + 1 Domains (Einfach, Kompliziert, Komplex, Chaotisch, Unordnung), Causality, Correlation, Constraint.**

### Anwendung:
- Nutzung des Cynefin-Frameworks zur Entscheidungsfindung und Problemlösung in der Softwareentwicklung.

## Kanban / Lean Software Development
### Zusammenhang und Herkunft:
- Agile, Lean, Scrum, XP und Kanban stammen aus der Lean-Philosophie.

### Kanban-Prinzipien:
- **Visualisieren des Workflows, Limitierung von WIP (Work in Progress), Management des Flusses.**

### Kanban Board:
- Werkzeug zur Visualisierung des Workflows.

### Cumulative Flow Diagram (CFD):
- Darstellung des Arbeitsflusses zur Identifikation von Engpässen.
