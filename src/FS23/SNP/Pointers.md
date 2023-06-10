Pointers zeigen auf eine Adresse im Speicher.

```c
int *p; // Pointer auf ein Objekt vom typ int

char *c[20]; // Array von 20 Pointern auf Objekte vom typ char

double (*d)[20]; // Ist ein Pointer, der af ein Array mit 20 Elementen zeigt

char **ppc; // Zeigt auf ein Objekt vom Typ Pointer
			// das auf ein Objekt vom Typ char zeigt

int * p, q; // p ist pointer
			// q ist KEIN pointer
```

**Sizeof**: Systemarchitektur abhängig (32 bit = 32/8 -> 4 byte)


## Operatoren
```c
int i;

int *p;
int *op;

p = &i;  // p zeigt auf die Adresse von i

*p = 4; // modifiziert den Wert von i

// Zeigt auf die gleiche Adresse wie p zum ZEITPUNKT des setzens.
op = p;
*op += 5; // modifiziert Objket i

```

Pointer müssen immer auf etwas zeigen, sonst wird **IRGENDEIN** Speicher modifizert.

## Der geilste Pointer

```c
double d = 1.0;

// Void pointer, zeigt auf alles mögliche
void *vp = &d;

// Zuerst auf double pointer casten
// dann wert von double auslesen
printf("%f", * (double*)vp);
```

## Konstante Pointers
Konstant = nicht mehr modifizierbar
```c
int i = 15;
int * const p = &i;

// i kann modifizert werden
i = 16;
printf("%d", *p);

// p aber nicht mehr
p++; // DAS GEHT NICHT!!!
```

## NULL Pointer
Hat die Adresse 0
```c
#include <stdio.h>

int *p1 = 0; //blöde idee, vorallem nicht lesbar
int *p2 = NULL; // perfekt

```

## Für strukturen
```c

typedef struct {
  int studNr;
  char name[30];
  char vorname[30];
} Student;

Student notPointer;
Student *pointer;


notPointer.studNr = 4;
strcpy(notPointer.name, "Mueller");

// Hey, ich zeige auf den notPointer
pointer = &notPointer;

printf("%s", (*pointer).name); // Mueller

```

# Pointer Arithmetik

```c
int a[5] = {2, 4, 6, 8, 10};
int *p = a;


// alle folgenden Zeilen sind identisch
a[3]     = 1; // vom Compiler intern als *(a + 3) = 1 generiert
*(a + 3) = 1; // a steht für die Start Adresse von a
*(p + 3) = 1; // p ist auf die Start Adresse von a gesetzt
p[3]     = 1; // vom Compiler intern als *(p + 3) = 1 generiert
```

## Iterator

```c
int a[5];

// a+5 ist die Adresse *hinter* das
// letzte Element des Arrays: C++ Stil

for(int *it = a; it != a+5; ++it) {
	*it = 0;
}

```

oder
```c
int array[5];

int *it = &array[0]; // zeigt auf das erste Element von a
int *end = &array[5]; // zeigt auf das letze Element von a
    
for(it; it != end; ++it) {
	*it = 0;
}

```

# String Literale
```c

char * str = "I am a literal";

printf("%s", str);

printf("%c", str[0]);
```

## Jagged Arrays
Eindimensionale Arrays von pointern.

```c
char *jagged[] = {
	"January",
	"February",
	"March",
	"April",
	"Mai",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December" };


if (jagged[3][2] == ‘r') {
...
}
// jagged[3] is “April”
// jagged[3][2] is the third character of April
```