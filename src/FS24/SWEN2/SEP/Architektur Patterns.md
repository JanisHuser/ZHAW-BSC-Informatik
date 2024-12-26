### Architektur Patterns

#### CQRS (Command Query Responsibility Segregation)
CQRS ist ein Architekturpattern, das die Lese- und Schreiboperationen eines Systems trennt. Dies bedeutet, dass es unterschiedliche Modelle für Abfragen (Queries) und Befehle (Commands) gibt. 

- **Vorteile**:
  - Optimierte Lese- und Schreibmodelle.
  - Bessere Skalierbarkeit und Leistung.
  - Erleichtert die Implementierung von Event Sourcing.

- **Nachteile**:
  - Komplexität der Implementierung.
  - Dateninkonsistenz zwischen Lese- und Schreibmodell möglich.

#### Event Sourcing
Event Sourcing ist ein Architekturpattern, bei dem der Zustand eines Systems durch eine Abfolge von Ereignissen (Events) gespeichert wird, anstatt den aktuellen Zustand direkt zu speichern.

- **Vorteile**:
  - Volle Nachvollziehbarkeit und Reproduzierbarkeit von Änderungen.
  - Unterstützung für Audit- und Wiederherstellungsprozesse.
  - Erleichtert die Implementierung von CQRS.

- **Nachteile**:
  - Komplexität der Event-Nachverfolgung und -Wartung.
  - Erfordert robuste Event-Handling-Mechanismen.

#### Strangler Pattern
Das Strangler Pattern ist eine Methode zur schrittweisen Migration von Altsystemen zu neuen Systemen. Neue Funktionen werden in ein neues System geschrieben, während das alte System schrittweise zurückgebaut wird.

- **Vorteile**:
  - Minimierung der Risiken bei der Migration.
  - Kontinuierliche Verbesserungen und Refactoring möglich.
  - Keine Downtime erforderlich.

- **Nachteile**:
  - Komplexität der Koexistenz von Altsystem und neuem System.
  - Zusätzlicher Integrationsaufwand.

#### Online-Migration
Online-Migration ist der Prozess der Datenmigration, bei dem das System während der Migration online und verfügbar bleibt.

- **Vorteile**:
  - Minimale Ausfallzeiten.
  - Bessere Benutzererfahrung durch kontinuierliche Verfügbarkeit.

- **Nachteile**:
  - Erhöhte Komplexität und Risiko der Dateninkonsistenz.
  - Erfordert sorgfältige Planung und Testing.

#### Circuit Breaker
Das Circuit Breaker Pattern schützt eine Anwendung vor Kaskadeneffekten von Fehlern und Überlastungen in abhängigen Diensten. Es unterbricht Aufrufe zu fehlerhaften Diensten und stellt nach einer bestimmten Zeitspanne Verbindungen wieder her.

- **Vorteile**:
  - Verbesserung der Systemstabilität und Fehlertoleranz.
  - Verhindert Ressourcenerschöpfung durch wiederholte Fehlversuche.

- **Nachteile**:
  - Komplexität der Implementierung und Konfiguration.
  - Mögliche Verzögerungen durch falsche Auslösungen.

#### Bulkhead (Schottwand)
Das Bulkhead Pattern teilt ein System in unabhängige Bereiche (Bulkheads), um den Einfluss eines Fehlers zu begrenzen und die Gesamtsystemstabilität zu erhöhen.

- **Vorteile**:
  - Verbesserung der Fehlertoleranz und Isolation.
  - Reduzierung der Auswirkungen eines Teilausfalls.

- **Nachteile**:
  - Zusätzlicher Verwaltungsaufwand für die Konfiguration und Wartung.
  - Mögliche Ressourcenunterauslastung.

#### Retry
Das Retry Pattern wiederholt fehlgeschlagene Operationen nach einer definierten Anzahl von Versuchen und Zeitintervallen, um vorübergehende Fehler zu überwinden.

- **Vorteile**:
  - Erhöhung der Erfolgsrate von Operationen.
  - Vermeidung unnötiger Fehlermeldungen durch vorübergehende Probleme.

- **Nachteile**:
  - Erhöhung der Latenzzeit bei wiederholten Versuchen.
  - Risiko von Überlastungen durch wiederholte Versuche.

#### Serverless
Serverless ist ein Architekturmuster, bei dem Anwendungen auf verwalteten Cloud-Diensten laufen, die automatisch skalieren und Ressourcen basierend auf der tatsächlichen Nutzung bereitstellen.

- **Vorteile**:
  - Keine Serververwaltung erforderlich.
  - Automatische Skalierung und hohe Verfügbarkeit.
  - Bezahlung nach Nutzung.

- **Nachteile**:
  - Begrenzte Kontrolle über die Infrastruktur.
  - Potenzielle Abhängigkeit von Cloud-Anbietern.

#### Microservices
Microservices ist ein Architekturmuster, bei dem eine Anwendung aus einer Sammlung kleiner, unabhängiger Dienste besteht, die jeweils einen spezifischen Geschäftsfähigkeitsbereich abdecken.

- **Vorteile**:
  - Unabhängige Entwicklung, Bereitstellung und Skalierung von Diensten.
  - Erhöhte Flexibilität und Agilität.
  - Bessere Fehlertoleranz und Isolation.

- **Nachteile**:
  - Komplexität des Service-Managements und der Kommunikation.
  - Herausforderungen bei der Datenkonsistenz und -integration.

#### Self-contained Systems
Self-contained Systems (SCS) ist ein Architekturansatz, bei dem eine Anwendung in unabhängige Systeme unterteilt wird, die jeweils eine spezifische Domäne abdecken und sowohl Frontend- als auch Backend-Funktionen enthalten.

- **Vorteile**:
  - Unabhängige Entwicklung und Bereitstellung.
  - Reduzierung der Abhängigkeiten zwischen Teams und Systemen.
  - Bessere Skalierbarkeit und Wartbarkeit.

- **Nachteile**:
  - Erhöhte Komplexität der Systemintegration.
  - Herausforderungen bei der Konsistenz und gemeinsamen Nutzung von Daten.

#### Monolith (Modulith)
Ein Monolith ist eine traditionelle Architekturmuster, bei dem eine Anwendung als eine einzige, zusammenhängende Einheit entwickelt und bereitgestellt wird. Ein Modulith ist ein gut strukturierter Monolith, der in gut definierte Module unterteilt ist.

- **Vorteile**:
  - Einfache Entwicklung und Bereitstellung.
  - Keine Netzwerk-Latenz zwischen Modulen.
  - Einfacheres Debugging und Testing.

- **Nachteile**:
  - Schwierigkeiten bei der Skalierung und Wartung großer Codebasen.
  - Abhängigkeiten zwischen Modulen können Änderungen erschweren.
  - Begrenzte Flexibilität und Agilität.

### Zusammenfassung

Architekturpatterns bieten verschiedene Ansätze zur Strukturierung und Verwaltung von Softwareanwendungen, um spezifische Probleme und Herausforderungen zu lösen. Die Wahl des richtigen Patterns hängt von den spezifischen Anforderungen, Zielen und Kontexten der Anwendung ab.