# Webserver


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