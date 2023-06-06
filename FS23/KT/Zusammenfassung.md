# FORMELN
**Log umschreiben**
- $2^x = 8$
- $x = \log_2{(8)}$ 

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
| Bandbreite | $B$ | $\frac{bits}{s}$ | |
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

## Fehlererkennung / Fehlerkorrektur
**FER** (**F**rame **E**rror **R**atio)
**RER** (**R**esidual **E**rror **R**atio)
**BER** (**B**it **E**rror **R**atio)

## Parity
**Even Parity**: Wenn die Anzahl Bits, die 1 sind, gerade ist, dann ist der Wert: 1
**Odd Parity**: Wenn die Anzahl Bits, die 1 sind, ungerade ist, dann ist der Wert 1

# Local Area Networks (LAN)

| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Framerate | $F_R$ |$\frac{\text{Frames}}{\text{s}}$|$F_R = \frac{B}{8 \cdot (F_L + IFG) \cdot 8}$|
| Bitrate | $B$ |||
| Framelänge | $F_L$ |Bits| Data + Prä + SFD + FCS = Data + 7Bit + 1Bit + 4Byte |
| Nutzbitrate | $N$ || $N = F_R \cdot P \cdot 8$|
| Payload | $P$ |||

## Übertragungsarten
- **Unicast**: an einzelne Stationen
- **Broadcast**: an alle Stationen
- **Multicast**: an eine Gruppe von Stationen

## Leitungscode

Als **Leitungscode** wird ein Manchester eingesetzt
- 1 positive Flanke, 1 negative Flanken
- Erlaubt die Taktrückgewinnung auf einfache Weise
- Benötigt die doppelte Bandbreite des theoretischen Minimums 
![](media/Pasted%20image%2020230604142706.png)

## Kollosionen
Können durch die Überlagerungen von Signalen entstehen. Kollosionen müssen erkannt werden. 
![](media/Pasted%20image%2020230604143542.png)

### Kollosionserkennung
![](media/Pasted%20image%2020230604155515.png)



## Topologie
![](media/Pasted%20image%2020230604143612.png)

| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Nutzdaten | $N$ | Bits |
| Länge zwischen Switch und Knoten | $l$ | $m$ |
| Bandbreite | $B$ | $\frac{bits}{s}$
| Framedauer | $t_{\text{frame}}$ |s | $\frac{N + 8 \cdot (\text{Prä/SFD}) + 12 (\text{Macs}) + 2 (\text{Type} + 4 (\text{FCS})) }{B}$ |
| Transferdauer | $t_{\text{transfer}}$ | s | $\frac{l}{c_\text{Medium}}$

## Ethernet
![](media/Pasted%20image%2020230604160442.png)

## IEEE Mac Adressen
![](media/Pasted%20image%2020230604161209.png)


# Switched LAN und Ethernet Technologien
