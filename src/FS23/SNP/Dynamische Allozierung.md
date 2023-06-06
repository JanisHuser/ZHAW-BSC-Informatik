## Heap
Zur Laufzeit dynamisch Speicher vom Heap anfordern

```c
// aus stdlib.h
// alloziert "size" Bytes vom Heap und gibt die Start Adresse zurück
void *malloc(size_t size);
// alloziert "nitems" mal "size" Bytes, setzt sie auf 0, und gibt die Adresse zurück void *calloc(size_t nitems, size_t size);
// vergrössert (oder verkleinert) einen vorgängig angeforderten Speicherbereich
void *realloc(void *ptr, size_t size);
// gibt einen oben angeforderten Speicherbereich frei
void free(void *ptr);

```

## Beispiel
```c
#include <stdlib.h>

typedef struct {
	char firstName[30];
	char lastName[30];
} Person;

Person* pointerToPerson = (Person*)malloc(sizeof(Person));

if (pointerToPerson == NULL) {
	// Etwas ist schief gelaufen. Pointer kann NICHT verwendet werden!!
	return;
}

// Wandlung in Person, dann firstname setzen
strcpy((*pointerToPerson).firstName, "firstname");

// Direkter Speicherzugriff
strcpy(pointerToPerson->lastName, "lastName");


printf("%s", pointerToPerson->firstName);

printf("%s", (*pointerToPerson).lastName);

//GANNZ WICHTIG
free(pointerToPerson); // Speicherplatz wieder frei geben

```

## Probleme

### Buffer Overflow
- z.B. Schreiben von 21 Zeichen langem String in 20 Zeichen langen Array,

