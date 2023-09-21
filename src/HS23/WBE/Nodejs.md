# Nodejs

Ist nicht die einziege Javascript-Laufzeitumgebung ausserhalb von Browsern. Weitere Alternativen sind:

- Deno ([https://deno.land](https://deno.land))
- Bun ([https://bun.sh](https://bun.sh))

- Asynchrone, ereignisbasierte Javascript-Laufzeitumgebung
- Grundlage für skalierbare Netzwerk-Anwendungen
- Basiert auf Googles V8 Engine
- Open Source und plattformübergreifend

## Beispiel

```javascript
// ==== hello-world.js ====
const http = require('http');

const hostname = '127.0.0.1';
const port = '3000';

const server = http.createServer((req, res) => {
	res.statusCode = 200;
	res.setHeader('Content-Type', 'text/plan');
	res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
	console.log(`Server running at http://${hostname}:${port}/`);
});

```

## Verwendung

Startet das Script, zu dem der Pfad führt
```shell
$ node hello-world.js
Server running at http://127.0.0.1:3000/
# Abbruch mit CTRL-C
```


Startet eine interaktive REPL (Read Eval Print Loop) Shell gestartet werden
```shell
$ node
Welcome to Node.js vs.12.16.2
Type ".help" for more information.
```

## Frameworks

- Node-js ist eine low-level Plattform
- Zahlreiche Frameworks und Tools bauen darauf auf

### Beispiele

- Express: Webserver, Nachfolger: Koa
- Socket.io: Echtzeitkommunikation
- Next.js: serverseitiges React Rendering
- Webpack: JavaScript Bundler
- Babel, TypeScript
- uvm.

## NPM

- Paketverwaltung für Node.js
- Repository mit > 1 Mio Paketen
- Werkzeuge zum Zugriff auf das Repository (npm, yarn)
- Seit 2020: Github / Microsoft