Wird benötigt um Aufgaben aufzutrennen, und zu  vereinfachen

## Header
Datei endet mit .h
```c
// list.h
#ifndef __LIST_H__
#define __LIST_H__

// Diese Defines sind wichtig, da sonst der Header doppelt kompiliert werden kann. Macht auch Probleme mit Defines, Konstanten, statics und Methodendeklarationen


// Methode wird im Header deklariert
// so weiss jedes andere Modul, heyy in dieser Datei finde ich die deklaration
// ausprogrammiert wird diese aber in der source (.c) datei
void list_clear(void);

// Diese Variable ist GLOBAL in ALLEN Dateien, die list.h inkludieren vorhanden
static int iAmGlobal = 0;

#endif __LIST_H__
```
Können aber auch durch folgendes ersetzt werden

```c
// list.h
#pragma once

```


# Source
```c
// list.s

#include "list.h"

// ist für jedes include separat definiert
int iAmSpecific = 3;

// ist für jedes include gleich, kann für Prozesskommunikation verwendet werden.
static int iAmProcessWide = 5;

void list_clear()
{
	// globale variable modifizieren
	iAmGlobal = 2;

	// verändert die Dateispezifische Variable
	iAmSpecific = 5;
}
```

# Makefile

Du gucken da: https://devhints.io/makefile
