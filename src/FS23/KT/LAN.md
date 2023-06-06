# Local Area Networks (LAN)

| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Framerate | $F_R$ |$\frac{\text{Frames}}{\text{s}}$|$F_R = \frac{B}{8 \cdot (F_L + IFG) \cdot 8}$|
| Bitrate | $B$ | | |
| Framelänge | $F_L$ |Bits| Data + Prä + SFD + FCS = Data + 7Bit + 1Bit + 4Byte |
| Nutzbitrate | $N$ | | $N = F_R \cdot P \cdot 8$|
| Payload | $P$ | | |

## Übertragungsarten

- **Unicast**: an einzelne Stationen
- **Broadcast**: an alle Stationen
- **Multicast**: an eine Gruppe von Stationen

## Leitungscode

Als **Leitungscode** wird ein Manchester eingesetzt

- 1 positive Flanke, 1 negative Flanken
- Erlaubt die Taktrückgewinnung auf einfache Weise
- Benötigt die doppelte Bandbreite des theoretischen Minimums 

<img src="media/LAN_voltage_chart.png" width="300" />

## Kollosionen
Können durch die Überlagerungen von Signalen entstehen. Kollosionen müssen erkannt werden. 

<img src="media/Pasted%20image%2020230604143542.png" width="300"  />

### Kollosionserkennung

<img src="media/Pasted%20image%2020230604155515.png" width="300" />


## Topologie

<img src="media/Pasted%20image%2020230604143612.png" width="300" />

| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Nutzdaten | $N$ | Bits |
| Länge zwischen Switch und Knoten | $l$ | $m$ |
| Bandbreite | $B$ | $\frac{bits}{s}$
| Framedauer | $t_{\text{frame}}$ |s | $\frac{N + 8 \cdot (\text{Prä/SFD}) + 12 (\text{Macs}) + 2 (\text{Type} + 4 (\text{FCS})) }{B}$ |
| Transferdauer | $t_{\text{transfer}}$ | s | $\frac{l}{c_\text{Medium}}$

## Ethernet

<img src="media/EthernetData.png" width="300" />

## IEEE Mac Adressen

<img src="media/Pasted%20image%2020230604161209.png" width="300" />