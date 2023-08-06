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

<img src="../media/Pasted%20image%2020230604133437.png" width="300" />


**7. Application Layer (Verarbeitungsschicht)**

Anwendungen greifen auf das Internet zu

**6. Presentation Layer (Darstellungsschicht)**

Daten werden für die Anwendung formatiert (HTTP, Email, ...)

**5. Session Layer (Session Layer)**

Koltrolliert Sessions und Ports

**4. Transport Layer (Transportschicht)**

Transport von Daten in Protokollen (TCP, UDP, ...)

**3. Network Layer (Vermittlungsschicht)**

- Paketierung von Daten / Unterteilen von Daten
- Fragmente erstellen / zusammensetzen
- Flusskontrolle
- Zwischenspeichern von Daten

**2. Datalink Layer (Sicherungsschicht)**

- Adressierung
- Zugriff auf Ressourcen
- Netzüberlastung vermeiden / Fehlererkennung

**1. Physical Layer (Bitübertragungsschicht)**

- Rohe Übertragung von Bits (ungesichert)