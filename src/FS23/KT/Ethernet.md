# Ethernet

## Klasse bestimmen

| Klasse | Addressbereich | Netzmaske |
|--|--|--|
| A | 0.0.0.0 - 127.255.255.255 | 255.X.0.0 |
| B | 128.0.0.0 - 191.255.255.255 | 255.255.X.0 |
| C | 192.0.0.0 - 223.255.255.255 | 255.255.255.X |

## Subnetzmaske berechnen
**Anzahl benötigte Ip Adressen**:  $$

**Anzahl zum Rechnen**:  $ = n + \) Bits aus Tabelle lesen

**Maske**: $/(32 - b)$

| Bits  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Dezimal | 1 | 2 | 4 | 8 | 16| 32| 64|128|256|

Es werden jeweils zwei Adressen für
- Broadcast (höchste Adresse)
- Netzadresse (tiefste Adresse)
benötigt.

| CIDR | Subnet Maske | Anzahl Adressen | Nutzbare Adressen |
|-|-|-|-|
| /32 | 255.255.255.255 | 1 | 1 |
| /31 | 255.255.255.254 | 2 | 2 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224	| 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1024 | 1022 |
| /21 | 255.255.248.0 | 2048 | 2046 |
| /20 | 255.255.240.0 | 4096 | 4096 |
| /19 | 255.255.224.0 | 8192 | 8190 |
| /18 | 255.255.192.0 | 16,384 | 16,382 |
| /17 | 255.255.128.0 | 32768 | 32766 |


**Anzahl Adressen**: $ 2^(32-CIDR) $
**Anzahl nutzbare Adressen**: $ 2^(32-CIDR) - 2 $

## VLAN

Erlaubt es ein grosses Netz in unabhängige logische Netze aufzuteilen. Jeder Port am Switch kann einem beliebigen VLAN zugeordnet werden.

<img src="media/Pasted image 20230606160751.png" width="300" />

## Spanning Tree Protokoll (STP)

- Alle Knoten werden genau einmal verbunden
- Verbindungen, die zu Schleifen führen werden deaktiviert

**Bridge Identifier:** Priorität + Mac Adresse

1. Root bestimmen mittels Bridge-Identifier 
2. Direkt angeschlossene Bridges bestätigen
3. Weitere Verbindungen abhängig von Kosten und Bridge-Identifier eintragen

## Ethernet Systeme

**Autonegotiation**: Ermittlung der besten Betriebsart durch Austausch derLeistungsmerkmale zweier Netzwerkkomponenten

**Link Pulses**

- NLP: Link Presence Detection
- FLP: Autonegotiation, Autopolarity


<img src="media/Pasted image 20230606161909.png" width="300" />