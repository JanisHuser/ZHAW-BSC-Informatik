# Entitätstypen

![](https://informatik-abitur.de/wp-content/uploads/2017/10/ERM_Grundelemente.png)

- **Entität**: individuell identifizierbares Objekt der Wirklichkeit
- **Beziehung**: Verknüpfung zwischen zwei oder mehreren Entitäten
- **Attribut**: Eigenschaft einer Entität (Spalte)

# Relationen

## 1:1
In einer „Eins-zu-Eins-Beziehung“ steht jede Entität aus einer Entitätsmenge mit höchstens einer Entität aus der anderen Entitätsmenge in Beziehung.
![](https://informatik-abitur.de/wp-content/uploads/2017/10/1_zu_1.png)
_Beschreibung_: **Eine Klasse** erhält **einen neuen Schüler**. Der **neue Schüler** kommt in **eine neue Klasse**.

# 1:m
In einer **„Eins-zu-M-Beziehung“** steht jede Entität aus der ersten Entitätsmenge mit **beliebig vielen** Entitäten aus der zweiten Entitätsmenge in Beziehung. Umgekehrt kann jede Entität aus der zweiten Entitätsmenge mit **höchstens einer Entität** aus der ersten Entitätsmenge in Beziehung stehen.

Dies ist die am häufigsten auftretende Beziehung.
![](https://informatik-abitur.de/wp-content/uploads/2017/10/1_zu_m.png)
_Beschreibung_: **Eine Klasse** erhält **mehrere neue Tablets**. **Ein Tablet** gehört zu **einer Klasse**.

# n:m
In einer **„N-zu-M-Beziehung“** steht jede Entität aus der ersten Entitätsmenge mit **beliebig vielen** Entitäten aus der zweiten Entitätsmenge in Beziehung (und umgekehrt).

![](https://informatik-abitur.de/wp-content/uploads/2017/10/n_zu_m.png)
_Beschreibung_: **Eine Klasse** erhält zum neuen Schuljahr **mehrere neue Lehrer**. **Ein Lehrer**bekommt **mehrere neue Klassen**.

### N-zu-M-Beziehung auflösen

N-zu-M-Beziehungen sind je nach Aufgabenstellungen so gut wie immer aufzulösen. Dazu erstellt man **eine zusätzliche Entität**, welche die Verknüpfungen der anderen beiden Entitäten enthält.

### Obere N-zu-M-Beziehung aufgelöst
![](https://informatik-abitur.de/wp-content/uploads/2017/10/1_zu_n_m_zu_1.png)


# ISA Beziehung
- Spezialisierung
- Vererben von Informationen
![[Pasted image 20230124181229.png]]


# ID Beziehung
![[Pasted image 20230124181521.png]]
- Ein logisches Buch hat mehrere physische Bücher.

# Schwache Entitätstypen / Zusammengesetze Entitätstypen
- Bei 1:1 Beziehungen
- Identifikation von Objekt B ist ohne Objekt A nicht möglich
![[Pasted image 20230124182515.png]]
Fotoabzug ist ohne Foto nicht möglich. 
![[Pasted image 20230124182418.png]]
