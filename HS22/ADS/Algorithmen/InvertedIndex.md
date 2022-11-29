# Invertierter Index

"... ein invertierter Index ist eine Indexdatenstruktur, die eine Abbildung vom Inhalt, wie. z.B. Wörter oder Zahlen, auf seine Positionen ...in einem Dokument oder eienr Gruppe von Dokumenten speichert"(Wikipedia)

T[0] = "it is what it is"

T[1] = "what is it"

T[2] = "it is a banana"

	a		{ (2, 2) }
	banana	{ (2, 3) }
	is		{ (0, 1), (0, 4), (1, 1), (2, 1) }
	it		{ (0, 0), (0, 3), (1, 2), (2, 0) }
	what	{ (0, 2), (1, 0) }


## Anwendungen
Suchmaschinen verwenden häufig invertierte Indexe
### WebRboter / Spider / Crawler
- Durchsuchen regelmässig das Web nach neuen Informationen

### Indexierung
- Aufbereitung von Dokumenten
- Speicherung im Index / in der Datenbank der Suchmaschine

### Retrievalsystem
- Suche im Index
- Sortierung nach Relevant
    - Wo kommen die Suchbegriffe vor?
	- Wie oft kommen die Begriffe vor?
	- In welcher Reihenfolge?
	- Wie lang ist der Text?
	- Wie viele Links verweisen auf das Dokument?
	- ...

## Verbesserungen

- Wörter sortieren und binär suchen: O(log(n))
- Wörter in einen balancierten Baum O(log(n))
- Hashing, allenfalls verteilte Hashtabellen über mehrere Systeme O(1)
- Nur relevante Wörter, Stopwords enfernen, z.B. den, dem, die, ...
- Wörter normalisieren:
	Wortstamm bilden (wohn: wohnen, bewohnen, wohnlich, Wohnzimmer)