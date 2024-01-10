# SEP


## Müssen Linux Befehle angewendet werden?

- Blödes Fakteswissen kommt nicht
- Also auch keine Linux Befehle

## Wan wird ein Port als Closed, Open oder Filtered angesehen

Bei NMAP wird standardmässig eine TCP Verbindung versucht,
- Open: Wenn der TCP SYN mit einem TCP SYN ACK beantwortet wird
- Closed: Wenn der TCP SYN mit einem TCP RESET beantwortet wird
- Filtered: Wenn gar nichts passiert, oder eine ICMP Fehlermeldung erhaltn wird

## Müssen wir die Building Blocks bei TLS kennen

- Nur was die Bezeichnungen hiessen 
- Nein, nur dass es sich um eine Art "Counter Mode" handelt

## Certificate Transparency

- Hat mit Revocation nichts zu tun
- Zertifikate, die nicht von der CA, aber mit dem Private Key der CA ausgestellt worden sind, sollen nicht in die Liste kommen
- Wenn CA unterwandert wird, dann wird der Private Key dieser 

## Practical Limitations of CRL's

- Zertifikate für langlebiges Dokumente
	- z.B. Testamente, x Monate später wird der Schlüssel geklaut
	- das noch gültige Testament soll noch funktionieren, um Dokument zu prüfen
	- Da die CRL das Ausstellungsdatum beinhaltet, darf das Zertifikat auch nicht entfernt werden, um die vorherigen Dokumente noch validieren zu können/dürfen
- CRL ist eine Append-Only Liste

## MAC SEC - Was ist der SEC TAG

- Dozent musste nachsehen, daher wird es eher nicht kommen
- IV Tag mit mehr Informationen

## VLAN

### WEP


- Bietet Integrität nur gegen zufällige Veränderung.
- Anpassungen im Header werden nicht getrackt, nur die Payload wird gesichert.

**Warum funktioniert der MITM?**

Annahmen:
- Der Angreifer hört eine Packages ab, für die er den Plaintext kennt
- HTTP Packages sind oft gleich, daher ist dies möglich


ZIEL: Siphertext so zu modifizieren, dass der Empfänger einen **anderen** Plaintext entschlüsselt, **ohne** dies zu merken.

Nur die Payload wird mit einer CRC behandelt, der Angreifer kann dann rückrechnen, mit XOR den Keystream zurückrechnen, und mit diesem den eigenen Payload verschlüsseln

- Der Attacker kennt den Plaintext (der Nachricht, und den eigens ausgedachten), kann somit auch den Keystream zurückrechnen
- Mit dem Keystream kann


Stream-sipher:

- Key Stream Sipher hat die Länge der Plaintext nachricht
- Key Stream XOR Plaintext = Nachricht 

### Unterschied CCMP - TKIP

- Temporal Key Integrity Protocol (TKIP):
- Counter Mode CBC-MAC Protocol (CCMP):

CCMP ist das bessere Format als TKIP,weil 
- TKIP RC4 mit dem Michael Algorithmus verwendet. Diese sind relativ schlecht implementiert und somit schwach.
- CCMP AES mit einer 128 Bit key length verwendet.


### FIDO

- Der Authenticator, UBI KEY, enthält einen Schlüsselpath. Der Private Key verlässt den Authenticator nie. 
- Die Party Information kommt vom Browser. Die Relying Party ist auf diese abgestimmt, somit kann eine Phising Seite diese nicht fälschen.

## Port-Based-Authentication

- Es funktioniert nur mit EAP-Messages, kann aber auch als Authentication Methode verwendet werden.

-> EAP transportiert **andere** Protokolle, ist also ein Wrapper. Der Switch lässt diese EAP Pakete durch, welche dann von diesem Switch weiter verwendet werden können.

