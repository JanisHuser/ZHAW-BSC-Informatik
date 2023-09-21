# Javascript

**Beschreibung**
- Dynamisches Typenkonzept
- Objektorientierter und funktionaler Stil möglich


**positiv**

- Mächtige unde moderne Sprachkonzepte
- Leistungsfähige Laufzeitumgebungen

**negativ**

- Design Mängel aus den Anfangstagen
- Grundlegende Änderungen nicht möglich, da nur Erweiterungen möglich sind

## Standards

- ECMAScript
- versionen
	- ES3: 2000 - 2010 (verbreitete Version)
	- ES4: Übung 2008 abgebrochen
	- ES5: 2009, kleineres Update
	- ES6: 2015, umfangreiche Neuerungen
	- ES7, Javascript 2016
	- Nun jährliche Updates
- Transpiler: Babel


## Console

### Formatiertes ausgeben

```javascript
let x = 30;
console.log("the value of x is ", x);
// -> the value of x is 30

console.log("my %s has %d ears", 'cat' 2);
// -> my cat has 2 ears
```


### Konsole löschen

```javascript
console.clear()
```

### Stack trace ausgeben

Wird bei Fehlern oft automatisch ausgegeben.

```javascript
console.trace()
```

### Zeit messen

```javascript
console.time()
console.log("Welcome to Programiz!");
console.timeEnd()
// default: 3.572ms
```

### Fehler ausgeben

```javascript
console.error()
```

## Zahlen

- Zahlentyp in JavaScript: **Number**
- 64 Bit Floating Point entsprechend IEEE 754 (double in Java)
- Enthält alle 32 Bit Ganzzahlen
- Konsequenz alle Java int auch in JavaScript exakt dargestellt
- Weitere Konsequenz: oft Rechnunggenauigkeit mit Zahlen mit Nachkommastellen

## Zahlenliterale

| Typ | Beispiel |
| Ganzzahlliteral | 17 |
| Dezimalstellen | 3.14 |
| Dezimalpunktverschiebung (*10^x) | 2.998e8 |

**Nicht exakte Zahlen**

0.1 = 0x3FB999999999999A, entspricht nicht exakt 0.1
0.25 // hexadezimal 3FD0000000000000, entspricht exakt 0.25

## Ausdrücke

- Rechenoperationen wie in Java
- Spezielle Zahlen: Infinity, -Infinity, NaN

```javascript
100 + 4 * 11 		// 114
(100 + 4) * 11 		// 1144
314 % 100 			// 14

1/0					// Infinity
Infinity + 1		// Infinity
0/0					// NaN (Not a Number)
```

## BIGINT

- Mit ES2020 eingeführt
- Lieterale mit angehängem n
- Keine automatische Typumwandlung von/zu Number

```javascript
1n + 2n				// 3n
2n ** 128n			// 340282366920938463463374607431768211456n

BitInt(1)			// 1n
Number(1n)			// 1

1n + 1				// Cannot mix BigInt and other types
```

## Typeof

- Operator, der TypString seines Operanden liefert

```javascript
typeof(12)			// 'number'
typeof(2n)			// 'bigint'
typeof(Infinity)	// 'number'
typeof(NaN)			// 'number'
typeof('number')	// 'string'
```

## Strings

- Sequenz von 16-Bit-Unicode-Zeichen
- Kein spezieller char-Typ
- Strings mit "..." und '...' verhalten sich gleich

### String-Verkettung

```javascript
`con` + "cat" + 'enate' // 'concatenate'
```

### Escape Sequencen

| Sequenz | Bedeutung |
|--|--|
| \\\\ | Backslash |
| \\n | newline |
| \\r | carriage return |
| \\v | vertical tab |
| \\b | backspace |
| \\f | form feed |
| \\uXXXX (4 Hexziffern) | UTF-16 code unit |
| \\xXX (2 Hexziffern) | ISO-8859-1 character |
| \\XXX (1-3 Oktalziffern) | ISO-8859-1 character | 

### Template Strings

- \\ wird als \\ interpretiert (Ausnahme vor `, $ und Leerzeichen)
- Kann Zeilenwechsel enthalten
- String-Interpolation: Werte in String einfügen

```javascript 
`half of 100 is ${100 / 2}`		// half of 100 is 50
`erste Zeile
zweite Zeie`					// 'erste Zeile\nzweite Zeil'
```


## Logische Ausdrücke

- Typ boolean mit Werten: true / false
- Vergleiche liefern Ergebnis vom Typ boolean
- Logische Operatoren entsprechen denen in C und Java
- Strings sind Werte: Vergleich mit == ist kein Problem

```javascript
typeof(true)				// 'boolean'
3 > 4						// false
1 < 2 && 2 < 3				// true
4 >= 5 || !(1 == 2)			// true
"ab" == "a" + "b"			// true
```