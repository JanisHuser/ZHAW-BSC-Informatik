# FORMELN
**Log umschreiben**
- $2^x = 8
- $ $x = \log_2{(8)}$ 

| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Signaldämpfung || db | $10*log(\frac{P_E}{P_A})$ |
| Signaldämpfung über Spannung | | db | $20 * log(\frac{U_E}{U_A})^2$ |
| Amplitude | $A$ | V | |
| Maximale Anzahl erkennbare Zustände | $M$ |bit/s |$1+\frac{A}{\Delta V}$ |
| Maximal erreichbare Bitrate (Hartley's Gesetz) | $R$ | bit/s | $R \le 2 \cdot B ld(M) = 2B \cdot ld(M)$
| Signalleistung | $S$ | | |
| Rauschleistung | $N$ | | |
| Kanalkapazität | $C$ | | $B \cdot ld(1 + \frac{S}{N})$ |
| Nettobitrate | | | $\text{Bruttobitrate} \cdot \frac{\text{Nutzdaten}}{\text{Nutzdaten} + \text{Header}}$ |
| Maximale Bitrate | $R$ | $\frac{\text{bit}}{\text{s}}$ | $R \leq 2B \cdot \log_2(M)$ |
| Unterscheidbare Signalzustände | $M$ | Anzahl||
| Amplitude | $A$ || $A = (M-1) \cdot \Delta V$ |
| Bandbreite | $B$ | MiB | |
| max. Symbolrate | $f_s$ | Hz | $2B$ |


# OSI Referenzmodell

**Verbindungsorientiert**
- Verbindungsaufbau nötig
- Ziel muss bereit sein

**Verbindungslos**
- Jederzeit Nachrichten schicken
- Ziel muss nicht „bereit“ sein

**Zuverlässig**
- Kein Datenverlust
- Sicherung durch Fehelr-Erkennung -/korrektur
- Text-Nachrichten

**Unzuverlässig**
- Möglicher Datenverlust
- Keine Sicherung
- Streaming

![](media/Pasted%20image%2020230604133437.png)

![](media/Pasted%20image%2020230604133513.png)

# Übertragungsmedien

**Lichtgeschwindigkeit**: $c_0 = 299‘792‘458 \frac{m}{s}$
**Ausbreitungsgeschwindigkeit**: $C_{Medium} = 200‘000 \frac{km}{s} \approx \frac{2}{3} C_0$  

## Signale
Für Übertragungsmedien ist die Dämpfung pro Distanz massgebend. Typischerweise in $dB$ pro 100m angegeben.

| Beschreibung | Signal | Spannung |
|-|-|-|
| Eingangssignal | $P_1$ | $U_1$ |
| Ausgangssignal | $P_2$ | $U_2$ |
| Signaldämpfung | $10 \cdot \log(\frac{P_1}{P_1})$ | $10 \cdot \log(\frac{U_1}{U_1})^2$ |

## Kabeltypen
- **Koaxialkabel**: Geeignet für hochfrequente Signale
- **Twinaxial-Kabel**: Hoher Schutz
- **Twisted-Pair** (TP): Häufig im Einsatz (Shielded / Unshieded)
- **Glasfaser**: Hohe Bandbreite, Geringe Dämpfung, Resistent


# Physical Layer (Bitübertragungsschicht)

## Serielle asynchrone Übertragung (ohne Synchronisations-Takt)

Zwischen Sender und Empfänger werden folgende Abmachungen gemacht
- Bitrate
- Anzahl Datenbits (Typischerweise 1 Byte)
- Anzahl Stopbits (Typischerweise 1 Bit)
![](media/Pasted%20image%2020230604135039.png)
Die *Taktrückgewinnung* ist möglich, solange regelmässig Zustandsänderungen auftreten.

## Serielle synchrone Übertragung
Bei der synchronen Übertragung arbeitet der Empfänger mit dem gleichen Takt wie der Sender
- Es werden keine Start- und Stopbits benötigt
- Der Takt muss zusätzlich übertragen werden

Die Übertragung des Takts erfolgt über ein Codierungsverfahren oder eine zusätzliche Leitung.

## Kommunikationsarten (Verkehrsbeziehung)
- **Simplex**: Ein Kanal, in eine Richtung
- **Halbduplex**: Ein Kanal, abwechslungsweise in zwei Richtungen
- **Vollduplex**: Ein Kanal pro Richtung

## Arten der Verbindungen (Kopplung)
- **Punkt-Punkt**: Direkte  Verbindung zweier Kommunikationspartner
- **Shared Medium**: Mehrere Partner verwenden das gleiche Medium

## Datenübertragungsrate
- **Baudrate**: Symbole pro Sekunde
- **Zeichenrate**: Zeichen pro Sekunde

# Data Link Layer

## Framing

### Asynchron
Keine Daten -> Nichts wird gesendet
Zu Beginn eines Frames wird ein Start-Bit gesendet

### Synchron
- Frames werden ohne Unterbruch gesendet
![](media/Pasted%20image%2020230604141236.png)