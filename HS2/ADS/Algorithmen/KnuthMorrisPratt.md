# Knuth-Morris-Pratt Algorithmus (KMP)

Der Knuth-Morris-Pratt Algorithmus wird verwendet, um sich wiederholende Patterns intelligent zu verschieben.

## Ablauf

1. Am Anfang wird im Pattern nach sich wiederholenden SubPattern gesucht. Diese werden in der **Next-Tabelle** gespeichert.

1. Text gemäss der Next-Tabelle durchsuchen

## Next-Tabelle (I)

1. Es werden mögliche Präfixe mit der Länge 1 bis n-1 gebildet.

Pattern: **BARBARA**

| Subpattern | Pattern |
|--|--|
| B | *B*arbara |
| BA | *BA*rbara |
| BAR | *BAR*bara |
| BARB | *BARB*ara |
| BARBA | *BARBA*ra |
| BARBAR | *BARBAR*a |

2. Danach wird jedes Subpattern von ganz links nach rechts verschoben, bis alle überlappenden Zeichen übereinstimmen, oder keine Überlappung gefunden wurde. Bei Übereinstummungen haben wir einen identischen Präfix und Suffix.

![](7AB9FE95-3326-4EFF-B72A-26649A1DEC50.jpeg)

**next[j]**: Um wieviel darf ich das Pattern nach links verschoben ansetzen und die Suche fortsetzen, falls Buchstabe j + 1 abweicht. Oder anders ausgedrückt, wie lange ist der gemeinsame Präfix und Suffix für das Subpattern der Länge j. 

## Next-Tabelle (II)

Es wird auch Suffix und Präfix verglichen

Aufwand O(m), m = Länge des Pattern

Dazu werden zwei Pointer eingeführt.
- Der Pointer p=posToCompare wandert von der Position 1 Schritt um Schritt bis zum Ende des Patterns.
- Der Pointer l=lenOfSubpattern zeigt, an welcher Position der Präfix aktuell verglichen wird (startet an der Position 0).

![](657E5B2F-4D34-448C-ABE8-2EE910D67BB3.jpeg)

### Ansatz

Beispiel "Ananas"
| Position | Buchstabe | Wert                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                             |
| -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0        | a         | -1                                                                                                                                                                                                                                                             | Sonderfall: Markiert den Anfang es Suchmusters. Hiermit muss verglichen werden!                                                                                                                                                                             |
| 1        | n         | 0                                                                                                                                                                                                                                                              | Wen der Buchstabe aus dem Text nicht übereinstimmt, so müssen wir den im Text gefundenen Buchstaben mit dem Suchmuster bei Position 0 vergleichen                                                                                                           |
| 2        | a         | 0                                                                                                                                                                                                                                                              | Ein 'a' findet sich an Position 0 im Suchmuster, damit ist das Präfix 'a' 1+0 Zeichen lang. Wenn der im Text gefundene Buchstabe nicht übereinstimmt, so findet sich das vorhergehende 'a', welches kein Präfix vor sich hat an Position 0 des Suchmusters. |
| 3        | n         | 1 | Das 'n' findet sich an Position 1 des Suchmusters, damit ist das Präfix 'an' 1+1 Zeichen lang. Wenn der im Text gefundene Buchstabe nicht übereinstimmt, so findet sich das vorhergehende 'n', welches ein 'a' vor sich hat an Position 1 des Suchmusters. |                                                                                                                                                                                                                                                             |
| 4        | a         | 2                                                                                                                                                                                                                                                              | Das 'a' findet sich an der Position 2 des Suchmusters, damit ist das Präfix 'ana' 1+2 Zeichen lang. Wenn der Buchstabe nicht übereinstimmt, so findet sich das vorhergende 'a', welches ein 'an' vor sich hat an Position 2 des Suchmusters.                |
| 5        | s         | 0                                                                                                                                                                                                                                                              | Das 's' findet sich **nicht** an der Position 3 des Suchmusters, damit ist 'anas' **kein** Präfix. Wenn der Buchstabe nicht übereinstimmt, so findet sich kein vorhergehendes 's' , welches ein 'ana' vor sich hat. Wir müssen das Suchmuster neu anlegen   |

## Implementierung

```java
public static int[] buildNextTab(String pattern) {
	int lenOfPattern = pattern.length();
	int lenOfSubPattern = 0;
	int posToCompare = 1;
	int[] next = new int[lenOfPattern - 1];

	while (posToCompare < lenOfPattern -1) {
		if (pattern.charAt(posToCompare) == pattern.charAt(lenOfSubPattern)) {
			lenOfSubPattern ++;
			next[ posToCompare ] = lenOfSupPattern;

			posToCompare++;
		} else {
			if (lenOfSubPattern != 0) {
				lenOfSubPattern = next[lenOfSubPattern - 1]:
			} else {
				next [posToCompare] = 0;
				posToCompare++;
			}
		}
	}
}
```

```java
public static void KMP(String textToSearch, String pattern) {
	int lenOfText = textToSearch.length();
	int lenOfPattern = pattern.length();
	int[] next = buildNextTab(pattern);
	next = int posOfText = 0, posOfPattern = 0;

	while ((posOfText < lenOfText) && (posOfPattern < lenOfPattern)) {
		
		// Characters match, try to increase pattern and text
		if (textToSearch.charAt(posOfText) == pattern.charAt(posOfPattern)) {
			posOfText++;
			posOfPattern++;
		} else {
			if (posOfPattern != 0) {
				
				// start the next comparison with the supbattern according
				// to the next-table
				posOfPattern = next[posOfPattern -1];	
			} else {

				// the first character of the pattern and text are differnt -> not the beginning of the pattern.
				posOfText++;
			}
		}
	}
	if (posOfPattern == lenOfPattern) {
		println("Position: " + Integer.toString(posOfText - lenOfPattern));
	}

}
```