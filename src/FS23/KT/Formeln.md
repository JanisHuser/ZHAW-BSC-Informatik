
# Allgemeine Formeln
| Beschreibung | Symbol |Einheit | Formel |
|--|--|--|--|
| Signaldämpfung | | db | $10*log(\frac{P_E}{P_A})$ |
| Signaldämpfung über Spannung | | db | $20 * log(\frac{U_E}{U_A})^2$ |
| Amplitude | $A$ | V | |
| Maximale Anzahl erkennbare Zustände | $M$ |bit/s |$1+\frac{A}{\Delta V}$ |
| Maximal erreichbare Bitrate (Hartley's Gesetz) | $R$ | bit/s | $R \le 2 \cdot B ld(M) = 2B \cdot ld(M)$
| Signalleistung | $S$ | | |
| Rauschleistung | $N$ | | |
| Kanalkapazität | $C$ | | $B \cdot ld(1 + \frac{S}{N})$ |
| Nettobitrate | | | $\text{Bruttobitrate} \cdot \frac{\text{Nutzdaten}}{\text{Nutzdaten} + \text{Header}}$ |
| Maximale Bitrate | $R$ | $\frac{\text{bit}}{\text{s}}$ | $R \leq 2B \cdot \log_2(M)$ |
| Unterscheidbare Signalzustände | $M$ | Anzahl||
| Amplitude | $A$ | | $A = (M-1) \cdot \Delta V$ |
| Bandbreite | $B$ | $\frac{bits}{s}$ | |
| max. Symbolrate | $f_s$ | Hz | $2B$ oder $\frac{1}{T_s}$ |
| Symboldauer | $T_s$ | s |  |

**Log Umwandeln**: $2^x = 8$ => $x = \log_2 8$

**dB umwandeln**:  $10 \cdot log(10^{-2}) = 20$
