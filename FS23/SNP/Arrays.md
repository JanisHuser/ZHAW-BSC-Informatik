Arrays werden als **ANEINANDERLIEGENDE** Blocks im Memory definiert.

**Länge**: Die Länge des Arrays **MUSS** zur Kompilierzeit bekannt sein.
**Index:** Beginnt bei 0

```c
const int ARRAY_LEN = 6;
int[ARRAY_LEN] array = { 0 }; // Alle Werte auf 0 setzem
```

## Modifzieren des Arrays
```c
const int ARRAY_LEN = 6;
int[ARRAY_LEN] array = { 0 }; // Alle Werte auf 0 setzem

array[2] = 6; // setzte 3. Element auf 6

// AUFPASSEN BEI DER INDEXIERUNG
// Es wird keine IndexOutOfRange Exception geworfen, wenn ausserhalbt des Blockes geschrieben wird
arrray[12] = 7;
array[-3] = 9;

```

## Initialisierung eines Arrays
```c
int array[] = { 1, 2, 3}; // alloziert einen Array der Länge 3
```

## Länge eines Arrays

### Bevorzug
```c
const size_t ARRAY_LEN = 100;

int array[ARRAY_LEN] = { 0 };

for (size_t i =0; i < ARRAY_LEN; i++) {
	array[i] = i;
}
```

### „Dynamische“ Länge
```c

int array[100] = { 0 };

// Nicht in einer Funktion möglich!!
size_t len = sizeof(array) / sizeof(array[0]);

for (size_t i =0; i < len; i++) {
	array[i] = i;
}
```

# Mehrdimensionale Arrays
Wie ein Schachbrett
```c

int array[2][3] = {
	{ 1, 2, 3 },
	{ 4, 5, 7}
};

array[0][0] = 5; // Zugriff
```

# Char Arrays und Strings

In Format: %s

String terminator: **Ein char array wird immer mit \\0 beendet, ansonsten ist es unmöglich die Länge zu bestimmen.**
-> Also Grösse immer um 1 erhöhen als gewünschte Länge
```c
char hello[] = "hello, world"; // kann modifziert werden

/*
h
e
l
l
o
,

w
o
r
l
d
\0
*/
```

Es ist aber möglich, den String-Terminator zu entfernen, indem man folgendes macht.
```c

char[12] hello = "Hello, World";
```

## String Funktionen
```c
#include <string.h>
char[] hello = "Hello world";

// String läng bestimmen
int laenge = strlen(hello);

// String vergleich
int result = stcmp(hello, "Hi");
// 0 = beide sind gleich
// > 0 wenn der erste string einen grösseren Ascii Wert hat als der zweite
// < 0 wenn der zweite string einen grösseren Ascii wert hat als der erste

```

### String kopieren

Kopiert source in dest, egal ob die Länge passt.
Rückgabewert ist ein Pointer zur destination
```c
char* strcpy(char dest[], const char source[]);
```

Kopiert source in dest, mit der maximalen Länge num
Rückgabewert ist ein Pointer zur destination
```c
char* strncpy(char dest[], const char source[], size_t num);
```

## Strings aneinanderhängen

Hängt eine Kopie von source an destination.
```c
char * strcat ( char * destination, const char * source );
```

Hängt die ersten num Zeichen von source an destination.
```c
char * strncat ( char * destination, const char * source, size_t num );
```
