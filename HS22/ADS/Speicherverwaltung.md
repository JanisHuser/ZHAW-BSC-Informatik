
## Fork / Join
1. Definiere ein ForkJoinPool-Objekt
2. Definiere ein Task-Objetk das von der Klasse RecursiveTask erbt
3. Instanziere den ForkJoinPool
4. Instanziiere (Root)Task-Objekt und rufe invoke() auf
5. In der Compute() methode Code mit der Aufteilung des Problems
5. 1. Löse das Problem direkt falls klein/einfach genug
5. 2. Sonst: Teile Problem auf: Rufe: Invokeall(tasks)


# Garbage Collection
- Is called when an object reference explicitly is set to null
- If the object goes out of scope


## Mark-Sweep-GC
- Speicher wird nicht sofort freigegeben, sondern est bei "Bedarf"
- Suche nach Blöcken die nicht benutzt sind, und markiert diese. Alle markierten Objekte werden sekentiell gelöscht.

### Probleme
- Aufwand
- Das Programm muss während Mark-Sweep-Phase gestoppt werden.
- Memory-Fragmentierung


## Mark-Compact
Nutzt Mark-Sweep-GC, verschiebt aber markierte Objekte werden an den Anfang des Heaps geschoben, was das Problem des Memory-Fragments löst.

### Probleme
- Schlehcte Performace

## Generational GC

![[Pasted image 20230105124202.jpg]]
