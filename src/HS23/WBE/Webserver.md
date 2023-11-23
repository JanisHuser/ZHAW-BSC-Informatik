# Webserver

| Port | Service |
|---|---|
| 20 | FTP - Data |
| 21 | FTP - Control |
| 22 | SSH Remote Login Protocol |
| 23 | Telnet |
| 25 | Simple Mail Transfer Protocol (SMTP) |
| 53 | Domain Name System (DNS) |
| 80 | HTTP |
| 443 | HTTPs |

## HTTP Requests 

| Methode | Beschreibung |
|--|--|
| GET | Resource Laden |
| POST | Information senden |
| PUT | Resource anlegen, überschreiben |
| PATCH | Rresource anpassen |
| DELETE | REsource löschen |

## HTTP Response Codes

| Code | Beschreibung |
|---|--|
| 1xx | Information (101 switching protocols) |
| 2xx | Erolg (200 OK) |
| 3xx | Weiterleitung (301 moved permanently) |
| 4xx | Fehler in Anfrage (403 Forbidden, 404 Not Found) |
| 5xx | Server-Fehler (501 Not implemented) |

## Einfacher Web Server
```javascript
const {createServer} = require("http")
let server = createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/html"})
  response.write(`
    <h1>Hello!</h1>
    <p>You asked for <code>${request.url}</code></p>`)
  response.end()
})
server.listen(8000)
console.log("Listening! (port 8000)")

```

## Einfacher Web Client

```javascript
const {request} = require("http")

let requestStream = request({
    hostname: "eloquentjavascript.net,
    path: "/20_node.html",
    method: "GET",
    headers: {Accept: "text/html"}
}, response => {
    console.log("Server responded with status code:", response.statusCode);
})
requestStream.end()
```

## Streams

### Server

```javascript
const {createServer} = require("http")
createServer((request, response) => {
  response.writeHead(200, {"Content-Type": "text/plain"})
  request.on("data", chunk =>
    response.write(chunk.toString().toUpperCase()))
  request.on("end", () => response.end())
}).listen(8000)
```

### Client

```javascript
const {request} = require("http")
let rq = request({ hostname: "localhost", port: 8000,
method: "POST"
}, response => {
  response.on("data", chunk =>
    process.stdout.write(chunk.toString()));
})
rq.write("Hello server\n")
rq.write("And good bye\n")
rq.end()
```

## File Server

```javascript

const {createServer} = require("http") const methods = Object.create(null)
createServer((request, response) => {
let handler = methods[request.method] || notAllowed; handler(request)
.catch(error => {
if (error.status != null) return error return { body: String(error), status: 500 }
    })
    .then(({body, status=200, type="text/plain"}) => {
response.writeHead(status, {"Content-Type": type}) if (body && body.pipe) body.pipe(response)
else response.end(body)
    })
}).listen(8000)
```

[File Server](https://eloquentjavascript.net/20_node.
html#h_yAdw1Y7bgN)


## Express Web Server

```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
```

### Routing

```javascript
app.get('/', function (req, res) { res.send('Hello World!')
})
app.post('/', function (req, res) {
  res.send('Got a POST request')
})
app.put('/user', function (req, res) { res.send('Got a PUT request at /user')
})
app.delete('/user', function (req, res) {
  res.send('Got a DELETE request at /user')
})
```

### Statische Dateien


```javascript
app.use(express.static('public'))
// http://localhost:3000/css/style.css
// Pfad zur Datei: public/css/style.css

app.use('/static', express.static('public'))
// http://localhost:3000/static/css/style.css
// Pfad zur Datei: public/css/style.css
```

## Cookies

- HTTP als zustandsloses Protokoll konzipiert
- Cookies: Speichern von Informationen **auf dem Client**
- RFC 2965: HTTP State Management Mechanism
- REsponse: *Set-Cookie*-Header, Request: *Cookie*-Header
- Zugriff mit JavaScript möglich (ausser *HttpOnly* ist gesetzt)

## Sessions

- Cookies auf dem Client leicht manipulierbar
- Session: Client-spezifische Daten auf dem Server speichern
- Identifikation des Clients über *Session-ID* (Cookie o.ä.)
- **GEFAHR**: Session-ID gerät in falsche Hände (Session-Hijacking)

```javascript
const express = require('express')
const cookieParser = require ('cookie-parser')
const session = require('express-session')
const app = express();

app.use(cookieParser())
app.use(session({secret: "Strong Secret Here!"}))

app.get('/', function(req, res) {
  if (req.session.page_views) {
    req.session.page_views++
    res.send(`You visited this page ${req.session.page_views} times`) 
  }
  else {
    req.session.page_views = 0
    res.send("Welcome to this page for the first time")
  }
})

app.listen(3000)
```

## Fetch API

```javascript

const url = "https://.."

fetch(url).then(response => {
  console.log(response.status)    // 200
  console.log(response.headers.get("Content-Type")) // text/plain

  response.text().then(text => {
    // GET TEXT
  })

  response.json().then(json => {
    // GET JSON
  })
})
```