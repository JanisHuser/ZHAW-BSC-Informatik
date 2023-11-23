# Asynchron

## File API

### Dateinformationen

[FS Stats](https://nodejs.org/api/fs.html#class-fsstats)

```javascript
const fs = require('fs')
fs.stat('test.txt', (err , stats) => {
    if (err) {
        throw err
    }

    stats.isFile()  // true
    stats.isDirectory() // false
    stats.isSymbolicLink()  // false
    stats.size      // 1024000 (bytes)
})
```

### Lesen einer Datei

```javascript
const fs = require('fs')
fs.readFile('test.txt', "utf8", (err , data) => {
    if (err) {
        throw err
    }

    console.log(data)
})
```

### Beschreiben einer Datei

```javascript
const fs = require('fs')
const content = "Node was here!"
fs.readFile('test.txt', content, (err , data) => {
    if (err) {
        throw err
    }

    console.log(data)
})
```

| Funktion | Bezeichnung |
|--|---|
| fs.access | Zugriff auf Datei oder Ordner prüfen |
| fs.mkdir | Verzeichnis anlegen |
| fs.readdir | Verzeichnis lesen, liefert Array von Einträgen |
| fs.rename | Verzeichnis umbenennen |
| fs.rmdir | Verzeichnis löschen |
| fs.chmod | Berechtigungen ändern |
| fs.chown | Besitzer und gruppe ändern |
| fs.copyFile | Datei kopieren |
| fs.link | Erstellt einen neuen festen Link |
| fs.symlink | Erstellt einen neuen symbolic link |
| fs.watchFile | Datei auf Änderungen überwachen |

## Calllbacks

Callbacks erlauben es Funktionen an einen EventHandler, oder anderen Funktionen mitzugeben.

```javascript
document.getElementById("button").addEventListener("click", () => {
    // element of id "button" clicked
});
```


### Set Timeout

- Der Callback wird zu einem späteren Zeitpunkt (in ms) ausgeführt
- Eintrag in die Timer-Liste, auch wenn Zeit auf 0 gesetzt wird
- Kann mit clearTimeout entfernt werden

```javascript
const id = setTimeout(() => {
    // runs after 50 milliseconds
}, 50);
clearTimeout(id);
```

### Intervall

```javascript
const id = setTimeout(() => {
    // runs every 2000 milliseconds = 2 seconds
}, 2000);
clearInterval(id);
```

### Sofort als möglich

```javascript
setImmediate(() => {
    // runs as best as possible
});
```

## Event Emitter

### Auf etwas hören
```javascript
const EventEmitter = require('events')
const door = new EventEmitter()

door.on('open', () => {
    console.log("Door was opened")
});

door.on('open', (speed) => {
    console.log(`Door was opened, speed: ${speed || 'unknown'}`)
});
```

### Event auslösen

```javascript
door.emit('open')
door.emit('open', 'slow')
```

## Promises

```javascript
// Funktion, die einen Promise erstellt und zurückgibt
function doSomethingAsync() {
  return new Promise((resolve, reject) => {
    // Simuliert eine asynchrone Aufgabe (z. B. eine Netzwerkanfrage)
    setTimeout(() => {
      const success = true;

      if (success) {
        resolve("Erfolg!");
      } else {
        reject("Fehler!");
      }
    }, 2000); // Simuliert eine Verzögerung von 2 Sekunden
  });
}

// Verwendung des Promises
doSomethingAsync()
  .then((result) => {
    console.log("Erfolgreich: " + result);
  })
  .catch((error) => {
    console.error("Fehler: " + error);
  });
```


### Zustände

| Zustand | Beschreibung |
|--|--|
| Pending | Ausgangszustand |
| Fullfilled | Erfolgreich abgeschlossen |
| rejected | Ohne Erolg abgeschlossen |

- Der Zustandswechsel kann nur einmalig passieren
- Der Endzustand kann entweder *fullfilled* oder *rejected* sein

### Promise.All

- Erhält einen Array von Promises
- fullfilled sobald **ALLE** fullfilled sind
- Ist **ein** Promise rejected, dann ist das gesamte Objekt rejected

### Promise.Race

- Erhält einen Array von Promises
- Erfüllt sobald **eine** davon fullfileed ist
- Ist **ein** Promise rejected, dann ist das gesamte Objekt rejected


## Async / Await

```javascript
function resolveAfter2Seconds(x) {
    return new Promise(resolve => {
        setTimeout( () => {
            resolve(x)
        });
    });
}

async function add1(x) {
    var a = resolveAfter2Seconds(20)
    var b = resolveAfter2Seconds(30)

    return x + await a + await b
}

add(10).then(console.log)
```