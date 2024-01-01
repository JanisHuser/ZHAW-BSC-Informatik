# Angriffe

## DDoS - Distributed Denial of Service

Es soll also für legitime Nutzer nicht mehr möglich sein auf die Systeme zuzugreifen oder die angebotenen Dienste zu nutzen. Geht die Attacke von vielen Rechnern aus, spricht man von einer DDoS (Distributed Denial of Service) Attacke.

### SYN Flood

Bei einem SYN-Flood-Angriff wird versucht, durch das Ausnutzen einer Schwachstelle im TCP/IP-Handshake einen Webdienst zu stören.

1. Der Angreifer sendet ein hohes Volumen an SYN-Paketen an den Zielserver, oft mit gefälschten IP-Adressen.
2. Der Server antwortet dann auf jede der Verbindungsanforderungen und lässt einen Port offen, der bereit ist, die Antwort zu empfangen.
3. Während der Server auf das endgültige ACK-Paket wartet, das nie ankommt, sendet der Angreifer weitere SYN-Pakete. Das Eintreffen jedes neuen SYN-Pakets veranlasst den Server, vorübergehend eine neue offene Port-Verbindung für eine bestimmte Zeitspanne aufrechtzuerhalten, und sobald alle verfügbaren Ports genutzt wurden, kann der Server nicht mehr normal funktionieren.

### DNS Amplification

1. Der Angreifer verwendet einen kompromittierten Endpunkt, um UDP-Pakete mit gespooften IP-Adressen an einen DNS-Recursor zu senden. Die gespoofte Adresse an den Paketen weist zur echten IP-Adresse des Opfers.
2. Jedes der UDP-Pakete stellt eine Anfrage an einen DNS-Resolver und setzt dabei oft ein Argument wie „ANY“ ein, um die größtmögliche Antwort zu erhalten.
3. Nach Empfang der Anfrage sendet der DNS-Resolver, der versucht, hilfreich zu sein, eine große Antwort an die gespoofte IP-Adresse.
4. Die IP-Adresse des Opfers empfängt die Antwort, und die umgebende Netzwerkinfrastruktur wird mit Traffic überflutet, wodurch ein Denial-of-Service verursacht wird.