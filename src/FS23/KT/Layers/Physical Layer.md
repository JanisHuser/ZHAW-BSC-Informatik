# Physical Layer (Bitübertragungsschicht)

## Serielle asynchrone Übertragung (ohne Synchronisations-Takt)

Zwischen Sender und Empfänger werden folgende Abmachungen gemacht

- Bitrate
- Anzahl Datenbits (Typischerweise 1 Byte)
- Anzahl Stopbits (Typischerweise 1 Bit)

<img src="../media/Pasted image 20230604135039.png" width="300"/>

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