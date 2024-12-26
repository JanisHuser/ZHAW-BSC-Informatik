# Cache

![](media/Cache/Address.png)

- Blocks sind in diesem Beispiel 4 Byte lang, können aber auch grösser, bzwh. kleiner sein.

## Aufbau im Memory

![](media/Cache/blocks.png)

- Gruppen von Blocks werden im Memory hintereinander gebilted.
- Die CPU kopiert gewisse Blocks mit deren ID in den Cache.


| Bezeichnung | Symbol |
|-------------|--------|
| Anzahl Bits für die Adressierung | t + i + o |
| Anzahl Bits für Offset | o |
| Anzahl Bits für Index | i |
| Anzahl Bits für Tag | t |


- **Grösse des RAM in Bytes (Memory Size)**: 2^(t+i+o)
- **Anzahl Zeilen im Cache**: 2^i
- **Grösse einer Cache-Zeile in Bytes (nur Nutzdaten)**: 2^o
- **Grösse des Cache in Bytes (Cache Size, nur Nutzdaten)**: 2^i * 2^o

## Cache Organization

![alt text](media/image-47.png)

![alt text](media/image-43.png)


### Fully Associative
![alt text](media/image-44.png)

### Direct Mapped

![alt text](media/image-45.png)

### N-Way Set Associative

- max index corresponds to number of sets (s=m/n)

![alt text](media/image-46.png)

## Memory Hierarchy

![alt text](media/image-41.png)]

![alt text](media/image-42.png)

## Principle of locality

```c
for (i=0; i < 10000; i++) {
	a[i] = b[i];					// spatial locality
}

if (a[1234] == a[4320]) {			// temporal locality
	a[1234] = 0;
}
```