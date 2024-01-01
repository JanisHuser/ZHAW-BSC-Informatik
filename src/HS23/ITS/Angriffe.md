# DDoS - Distributed Denial of Service

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


## Angriffe erkennen

Grundsätzlich ist es Ziel Website langsam zu machen oder sogar Offline zu nehmen, kann aber auch Lastspitze sein. Weitere Prüfungen:

- Verdächtig viel Traffic, der von einer einzelnen IP-Adresse oder einem IP-Bereich stammt
- Eine Flut von Traffic von Nutzern, die ein gemeinsames Verhaltensprofil teilen, wie z. B. Gerätetyp, Geolocation oder Web-Browser-Version
- Ein unerklärlicher Anstieg von Anfragen an eine einzelne Seite oder einen Endpunkt
- Seltsame Traffic-Muster wie Spitzen zu ungewöhnlichen Tageszeiten oder Muster, die unnatürlich erscheinen (z. B. eine Spitze alle 10 Minuten)

### Prävention

- Geo IP Blocking
- Notfall Server auf anderem Provider
- UpLink von Webseiten vom Rest trennen
- Infrastruktur und Netzwerk kennen um schnellst möglichst zu reagieren.

## Angriffe abwehren

Grösstes Problem Kunden von Angreiffern zu unterscheiden. Zudem können komplexe Angriffe auch mehrere Angriffsarten kombinieren.

### Blackhole Routing

Route die ins nichts führt. Das kann der gesamten Traffic sein oder ausgewählter durch Regeln. Ist normalerweise aber nicht gewünscht da so durch das Ziel des Angreifers erreicht wird.

### Rate Limiting

Limitierung der Anfragen pro Zeit. Kann meist nicht einen komplexen DDoS Angriff abwehren. Wird eingesetzt aber besser geeignet um Web Scrapper oder Brute-Force Anmeldungen zu verlangsamen.

### Web Application Firewall

Analysieren Web Traffic bevor es zum Server geht und lassen nur durch was nicht von Regeln gefiltert wird. Kann schützten von SQL Injection, XSS, CSRF und File Inclusion.

Fungiert als eine Art Reverse Proxy.

Kann gegen Layer 7 Angriffe helfen um gewisse Regeln im Falle eines Angriffes zu implementieren.

### Anycast-Netzwerk-Diffusion

Dieser Bekämpfungsansatz nutzt ein Anycast-Netzwerk, um den Angriffs-Traffic so auf ein Netzwerk verteilter Server zu verstreuen, dass der Traffic vom Netzwerk absorbiert wird.

Wie beim Kanalisieren eines reißenden Flusses in kleinere, voneinander getrennte Kanäle werden hier die Auswirkungen des Angriffs-Traffics so weit verteilt, bis sie kontrollierbar sind und die destabilisierende Wirkung des Angriffs zerstreut wird.

Die Zuverlässigkeit eines [Anycast-Netzwerks](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) in Bezug auf die Abwehr eines DDos-Angriffs ist von der Größe des Angriffs sowie der Größe und Effizienz des Netzwerks abhängig. Ein wichtiger Faktor des Cloudflare-Schutzes vor DDoS-Angriffen ist die Verwendung eines verteilten Anycast-Netzwerks.

Cloudflare hat ein Netzwerk mit 228 Tbps Tbit/s, was um eine Zehnerpotenz größer ist als der größte verzeichnete DDoS-Angriff.

![Untitled](Distributed%20Denial-of-Service%20DDoS%20f3a4894863ee4381914bae853d544052/Untitled%203.png)