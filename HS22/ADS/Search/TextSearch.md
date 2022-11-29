# Text Search

Searching through a text, larger than $^2^{31}-1 $ characters

| Methode | Aufwand |
|--|--|
| IndexOf Java | O(m * n) |



## Java

### IndexOf

Gibt die Position an der das Zeichen resp. Pattern beginnt zurück. Falls nicht gefunden -1.
```java
int indexOf (int ch) //ch: Unicode des gesuchten Zeichens
int indexOf (String str) //str: Gesuchter Substring
int indexOf (String str, int from) //from: Index ab welchem das Zeichen/Substring gesucht wird
```


## Brute Force (I)
Jedes Zeichen nacheinander suchen

```java
static int indexOf(String str, String pattern) {
	int k;
	for (int i=0; i < str.len() - pattern.len() + 1; i++) {

		// Suche den ersten übereinstimmenden Buchstaben
		while (i < str.len() && str.charAt(i) != pattern.charAt(0)) i++;

		// Pruefe, ob der Rest des Strings stimmt
		for (k=0; k < pattern.len() && str.charAt(i + k) == pattern.charAt(k); k++);

		if (k == pattern.len()) return i;
	}
	return -1;
}
```

## Brute-Force (II)
Es wird vor dem Ausführen der 2. Schleife, der erste Buchstabe gesucht.

```java
static int indexOf(String str, String pattern) {
	int k;
	for (int i=0; i < str.len() - pattern.len() + 1; i++) {
		// Suche den ersten übereinstimmenden Buchstaben
		while (i < str.len() && str.charAt(i) != pattern.charAt(0)) i++;

		if (i + pattern.len() <= str.len()) {
			for (k=0; k < pattern.len() && str.charAt(i + k) == pattern.charAt(k); k++);

			if (k == pattern.len()) return i;
		}
	}
	return -1;
}
```

## Brute Force (III)
Nachdem der Patternvergleich erfolglos war, *i* nicht nur um eins, sondern um die Länge des abgescuhten Strings erhöhen
```java
static int indexOf(String str, String pattern) {
	int k;
	for (int i=0; i < str.len() - pattern.len() + 1; i++) {
		// Suche den ersten übereinstimmenden Buchstaben
		while (i < str.len() && str.charAt(i) != pattern.charAt(0)) i++;

		if (i + pattern.len() <= str.len()) {
			for (k=0; k < pattern.len() && str.charAt(i + k) == pattern.charAt(k); k++);

			if (k == pattern.len()) return i;
		}
		i = i +k
	}
	return -1;
}
```

Sich wiederholende Teile im Pattern führen zu Probleme, mit dem Knuth-Morris-Pratt-Algorithmus intelligent verschieben.
