# DOM - Document Object Model

- Repräsentiert die angezeigte Website

## Window

- Globales Objekt der Browser Plattofrm
- Alle globalen Variablen und Methoden sind hier angehängt
- Neue globale Variablen landen ebenfalls hier

```javascript
window.alert === alert              // true
window.setTimeout === setTimeout    // true
window.parseInt === parseInt        // true
```

## Navigator

Represents the state and the identity of the user agent. It allows scripts to query it and to register themselves to carry on some activities.

```javascript
navigator.userAgent // "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"

navigator.language  // "de"

navigator.platform // "MacIntel"

navigator.onLine    // true
```

## Location

- Aktuelle Webadresse im Browser

```javascript

location.href                   // "https://gburkert.github.io/selectors/"
location.protocol               // "https:"
document.location.protocol      // "https:"
```

## DOM Scripting

```javascript

let aboutus = document.getElementById("aboutus")
let aboutLinks = document.getElementsByTagName("a")

let aboutImportant = aboutus.getElementyByClassName("important")

let navLinks = document.querySelectorAll("nav a")
```