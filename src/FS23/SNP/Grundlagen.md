
# Motivation

## Effizient
- C erlaubt es, sehr effizienten Code zu schreiben.
- Der verbraucht Arbeitsspeicher (Memory Footprint) ist sehr leicht.
- Die Ausführungsgeschwindigkeit ist hoch, weil Optimierungen zur Compilezeit ausgeführt werden.

## Verbreitet
- C/C++ ist mit grossem Abstand die wichtigste System- und systemnahe Sprache

## Systemverständnis
- C fördert und bedingt das Verständnis für das unterliegende System

# Hauptprgrogramm

```c
#include <stdio.h>    //printf
#include <stdlih.h>

int main (void)
{
	printf("Hello world in C\n"); // Newline ist wichtig
	return EXIT_STATUS;
}
```


# Datentypen

| Datentyp | Bytes | Wertbereich |
|-|-|-|
| signed char | 1 | -128 bis 127 |
| unsigned char | 1 | 0 bis 255 |
| \[signed\] short \[int\] | 2 | -32768 bis 32767 |
| unsigned short \[int\] | 2 | 0 bis 65636 |
| \[signed\] int | 4 | -2^31 bis 2^31-1 |
| unsigned \[int\] | 4 | 0 bis 2^32-1 |
| \[signed\] long \[int\] | 8 | -2^63 bis 2^63-1 |
| unsigned long \[int\] | 8 | 0 bis 2^64-1 |
| \[signed\] long long \[int\] | 8 | -2^63 bis 2^63-1 |
| unsigned long \[int\] | 8 | -2^63 bis 2^64-1 |
| long double | 19 | 1.2 \* 10^4932 bis 1.2 \* 10^4932 |

# Standard  Typen

## Integer

```c
#include <stdint.h>

int8_t signedValue;
uint8_t unsignedValue;

int16_t signedValue;
uint16_t unsignedValue;

int32_t signedValue;
uint32_t unsignedValue;

int64_t signedValue;
uint64_t unsignedValue;
```

## Bool

```c
#include <stdbool.h>

bool trueValue = true;
bool falseValue = false;
```

# Literalle / Konstanten

- Im Code eingefügte, unveränderliche Werte
- Ist die Zahlt zu gross für int, wird diese als long interpretiert.

```c

int decimal = 3987; // beginnt mit 1 - 9

unsigned int octal = 037;  // starts with 0

unsigned int hexadecimal = 0x23; // starts with 0X or 0x

char asciiCode = 'A'; // single ascii code 

double decimalPoint = 1.23;

double exponent = 1.6e3;

```

## Explizite Angabe

```c

int interpretedAsLong = 134L;

int interpretedAsLongLong = 134LL;

// U kann alleine, oder zusätzlich zu L / LL hinzufgefügt werden.
int interpretedAsUnsigned = 134U;

float interpretedAsFloat = 1.23F; // f geht auch

double interpretedAsDouble = 1.23L; // Long float

```


## Zeichenliterale

| Zeichen | Beschreibung |
|-|-|
| \\n | new line |
| \\t | horizontal tab |
| \\ | backslash |
| \\' | Single quote |
|  \\" | double quote |
| \\0 | Ascii Code 0 |

## Ascii Tabelle
![](media/Pasted%20image%2020230527113117.png)

## Strings
Durch Anführungszeichen eingeschlossene Zeichenfolgen werden als strings interpretiert.

```c
char[] iAmString = "Hello World!";
```


## Symbolische Konstanten

Symbolische Konstanten werden Textmässig ersetzt.

```c
#define MAX_LENGTH 1000
```

**Anwendung**

```c
#define MAX_LENGTH 1000

int length = MAX_LENGTH; // MAX_LENGTH wird durch den Wert im define ersetzt
```

# Definitionen 

- Sind Variablen ausserhalb von Funktionen definiert, sind diese lokal in der Source (.c) Datei.


## Variablen
Eine Variable sollte immer auf einen Wert initialisiert werden, da es keine Standardwerte gibt.

```c

double hoehe;
int laenge, breite; // mach das nicht
double r,
	radius = 15.0;  // Besser so, dann ist es klar, dass nur radius auf 15.0 ist
```

## Konstanten
Konstanten sind nicht veränderlich.
```c
const double pi = 3.14159;
```

## Typ Alias
Erlaubt es eigene Typen zu definieren, oder auch Synonyme.
```c
typedef int Index; // sagt, dass Index von typ int ist.

Index index = 0; // Index kann jetzt als Typ verwendet werden
```

```c
typedef struct position
{
	int x;
	int y;
} Position;

Position position;
position.x = 1;
position.y = 2;
```

# Statisch
Statische Variablen sind prozessübergreifend. 
```c
static int value;
```

- Wenn im Header definiert, dann sind diese sobald diese inkludiert wird, verfügbar.
- Wenn in der Source Datei definiert, dann sind diese in der gleichen Datei in allen Prozessen verfügbar.

## Bit-Operatoren

![](media/Pasted%20image%2020230527114235.png)


# Vorrang und Reihenfolge

![](media/Pasted%20image%2020230527114338.png)

## Type Casts

Ein type cast wird benötigt, um ein typ **explizit** in einen anderen Typen zu wandeln

```c
int value = 5;
int divider = 3;
double result = (double) value / divider;
```

## Kontrollstrukturen

### If-Else / Else-if
```c
const int SOME_CONSTANT = 10;
int value = 5;
if (value > SOME_CONSTANT) {
	// Do something if greater than SOME_CONSTANT
} else if (value < SOME_CONSTANT) {
	// Do something if less than SOME_CONSTANT
} else {
	// Do something if equal to SOME_CONSTANT
}
```

### For-Schleife
```c
for (int i=1; i <= 5; i++) {
	// Mache etwas in der for schleif
}
```

## While
Zuerst wird die Bedingung geprüft, dann der Inhalt der Schleife ausgeführt
```c
int i=0; // Initialisierung its wichtig
while (i < 5)
{
	// Mache etwas in der for schleife
	i++; // i muss manuell verändert werden
}
```

## Do while
Im Gegensatz zur While schleife, wird in der Do-While der Inhalt der Schleife zuerst ausgeführt.
```c
int i=0; // Initialisierung its wichtig
do
{
	// Mache etwas in der for schleife
	i++; // i muss manuell verändert werden
	// WIRD MINDESTENS 1 MAL AUSGEFÜHRT
}
while (i < 5);
```

## Switch
**Es können keine Strings evaluiert werden!!**
```c
int n;
switch (n)
{
case 1:
{
	// Wenn 1
	break;
}
case 2:
case 3:
{
	// Wenn 2 oder 3
	break;
}
default:
{
	// Alles andere
	break;
}

}
```


# Input

stdout / stdin / stderr sind auf der Konsole

## Konstanten String auf StdOut ausgeben
```c

#include <stdio.h>

int result = puts("Hello world");
if (result == EOF) 
{
	// Konnte nicht geschrieben werden
}
```

### Einzelnes Zeichen auf StdOut ausgeben
```c

#include <stdio.h>

int result = putchar('A');
if (result == EOF) 
{
	// Konnte nicht geschrieben werden
}
```

### Einzelnes Zeichen von StdIn lesen

```c

#include <stdio.h>

char c = getchar();

// Das Zeichen wird in c gespeichert
```



### Formatierte Ausgabe / Eingabe
```c
#include <stdio.h>

printf(format, arg1, arg2, . . .); // für Ausgabe

scanf(format, &x, &y, &z); // Parameter (ausser string (char*)) mit & angeben

```
Der Parameter _format_ ist ein String. Jedes der zusätzlichen Argumente (arg1, arg2, …) ist in diesem Forhanden und kann folgedes bedeuten.

| Zeichenfolge | Bedeutung |
|-|-|
| %d, %i | int |
| %u | unsigned int |
| %c | char |
| %s | String (char \*) |
| %f | float |

#### Formatierung von Float

%m.df

| Symbol | Bedeutung |
|-|-|
| m | Minimale Länge des Outputs |
| d | Anzahl dezimalstellen |


```c
#include <stdio.h>
double value = 5.12345;

printf("%f", value); //5.123450 (dezimal standard=6)

printf("%.3f", value); //5.123

printf("%10.3f", value); //      5.123 (6 Leerzeichen)

```


## Enums
```c
enum Wochentage
{
	Monday,  // int wert ist 0
	Tuesday, // int wert ist 1, nachfolgende sind vortlaufend
	Wednesday,
	Thursday = 13, // int wert ist 13 
	Friday, // int wert ist 14
	Saturday,
	Sunday
};

// Direkt auf Monday zugreifen, keine Angabe des Namespaces notwendig
Wochentag tag = Monday;


int dayOfWeek = tag; // 
```

## Strukturen / Datenklassen

```c
struct Point3D
{
	double x;
	double y;
	double z;
}

struct Point3D ptA = {1.0, 3.0, 4.0}; // Standard initialisierung

ptA.x = 5.0; // Zugriff
```

**Mit Typedef**
```c
typedef struct
{
	double x;
	double y;
	double z;
} Point3D;

Point3D ptA = {1.0, 3.0, 4.0}; // Standard initialisierung

ptA.x = 5.0; // Zugriff
```
