# General Responsibility Assignment Software Patterns (GRASP)

Entwurfsmuster, mit denene die Zuständigkeit bestimmter Klassen objektorientierter Systeme festgelegt werden.

## Information Expert

Ein allgemeines Prinzip des Objektentwurfs und der Zuweisung von Verantwortlichkeiten.

- Eine Klasse sollte nur die Aufgaben ausführen, die ihr Name auch beschreibt.

## Creator

Soll eine Instanz einer Klasse erstellt werden, wird ein Creator Pattern verwendet.

Anwenden wenn mindestens etwas zutrifft:

- A eine Aggregation oder ein Kompositum von B ist
- A registriert oder erfasst B-Objekte
- A arbeitet eng mit B-Objekten zusammen oder hat eine enge Kopplung
- A verfügt über Initialisierungsdaten für B

## Controller

Ein Controller koordiniert / empfängt als erstes Objekte jenseits der UI-Schicht als Systemoperation.


- Variante 1: _Fassaden Controller_ (repräsentiert das System bzw. übergeordnetes System)
- Variante 2: _Use Case Controller_ (pro Use case eine künstliche Klasse)

**Controller macht selber nur wenig und delegiert fast alles**


**LE06**


## Low Coupling


## High Cohesion


## Polymorphism

## Pure Fabrication

## Indirection

## Protected Variants