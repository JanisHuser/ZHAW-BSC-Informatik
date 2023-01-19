# O-Notation
Komplexität in Zeit und Speicher
- Nicht absolute Zahlen, sondern als Funktion von Grösse oder Anzahl Werten *n*.
| O            | Beschreibung                   |
| ------------ | ------------------------------ |
| O(1)         | konstanter Aufwand             |
| O(log n)     | logarithmischer Aufwand        |
| O(n)         | linearer Aufwand               |
| O(n • log n) | linear-logarithmischer Aufwand |
|              |                                |

# Singly Linked List
- Hat ein Ende
- Jedes Element kennt das nächste
- Ende ist **NULL**

| Aktion    | Aufwand | Begründung                   |
| --------- | ------- | ---------------------------- |
| Erweitern | O(n)    | Iterieren über gesamte Liste |                             |
| Entfernen | O(n)    | Iterieren über gesamte Liste |                             |
| Suchen    | O(n)    | Iterieren über gesamte Liste | 

# Doubly Linked List
- Hat ein Ende und ein Anfang
- Jedes Element hat einen Zeiger auf das vorherige und nächste
- Ende und Anfang sind **NULL**

| Aktion    | Aufwand | Begründung                      |
| --------- | ------- | ------------------------------- |
| Erweitern | O(1)    | Zeiger können verschoben werden |
| Entfernen | O(1)    | Zeiger können verschoben werden |
| Suchen    | O(n)    | Iterieren über gesamte Liste    | 
