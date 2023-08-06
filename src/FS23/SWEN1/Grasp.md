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


## Low Coupling

Kopplung = Mass für die Abhängigkeit von anderen Elementen.

- Hohe Kopplung: Element ist von vielen anderen Elementen abhängig
- Niedrige Kopplung: Element ist nur von wenigen anderen Elementen abhängig

Der Aufruf der Funktionen sollte in einer Linie geschehen. 


## High Cohesion

Mass für die Verwandtschat und Fokussierung eines Elements.

- Hohe Kohäsion: Element erledigt nur wenige Aufgaben, die **eng** miteinander verwandt sind.
- Geringe Kohäsion: Element das für viele unzusammenhängende Dinge verantwortlich ist.


Wie bei Low Coupling, sollten die Aufgaben gebündelt werden. 

## Polymorphism

Polymorphism ist das bündeln von typengleichen oder ähnlichen Verhalten.

**Tier**

Ein Hund ist auch ein Tier

## Pure Fabrication


Künstliche Hilfsklassen erzeugen um dem Domänenmodell gleich zu sein. Wird nur verwendet, um eine bessere Wiederverwendbarkeit zu realisieren.

## Indirection

Direkte Kopplung zwischen zwei oder mehreren Objekten vermeiden.

-> Vermittler 

## Protected Variants

Veränderungen im Objekt sollen **keinen** Einfluss auf andere Elemente haben.

-> Interfaces einführen

- Spekulationen sind zu vermeiden, da dies zu unnötiger Komplexität führt.