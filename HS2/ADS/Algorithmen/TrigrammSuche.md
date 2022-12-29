# Trigramm Suche

- Fehlertolerante Suche (auch Wortverdreher z.B. Vor- und Nachname)
- Effizient für grosse Datenbestände


- Index -> Wort in 3er Buchstaben Gruppen unterteilt.
- Das zu suchende Wort wird ebenfalls in 3-er Gruppen zerlegt.
Das gesuchte Wort mit am meisten übereinstimmungen wirrd genommen.

## Bespiel

PETER: **PET**, ETE, **TER**

PETTER: **PET**, ETT, TTE, **TER**


## Beispiel

Beispiel an PETER und LISA, PETRA
1. Basiswörter zertrennen:
    1. PETER wird zu PET, ETE, TER
    2. LISA zu LIS, ISA
    3. PETRA zu PET, ETR, TRA.
2. Wörter sortieren
    - PET: 1, 3
	- ETE: 1
	- TER: 1
	- LIS: 2
	- ISA: 2
	- **PET (bereits vorhanden in 1)**
	- ETR: 3
	- TRA: 3
3. Zu suchendes Wort **PETTER** aufteilen
    - PET, ETT, TTE, TER
4. Wörter matchen
    - PET: 1, 3
	- ETT: -
	- TTE: -
	- TER: 1
5. Anzahl Index wiederholungen zählen
    - 1: PET & TER -> 2
	- 3: PET -> 1
6. Index mit maximaler wiederholung suchen -> 1
7. **PETTER ähnelt PETRA mehr als PETRA.**

