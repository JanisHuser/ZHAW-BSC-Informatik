# Funktionen

## Funktion definieren

```javascript
const squareV1 = function(x) {
    return x * x;
}

function squareV2(x) {
    return x*x;
}

const squareV3 = x => x * x;
```


## Gültigkeitsbereiche

```javascript
let     m = 10      // block scope
const   n = 10      // constant with block scope
var     p = 10      // variable with function scope
```

## Globale Variablen

- Ausserhalb von Funktionen definiert
- In Funktionen kein const, let, var
- Gültigkeitsbereich möglichst einschränken

```javascript
result = 1 + 2
```

## Parameter

Parameter sind standardmässig undefined, somit müssen nicht alle Parameter gesetzt werden.


## Rest-Parameter

```javascript
function max ([...numbers]) {
    let result = -Infinity;
    for (let number of numbers) {
        if (number > result) {
            result = number;
        }
    }

    return result
}

console.log(max(4, 1, 9, -2))
```

### Alternative

```javascript
function max () {
    let result = -Infinity;
    for (let number of arguments) {
        if (number > result) {
            result = number;
        }
    }

    return result
}

console.log(max(4, 1, 9, -2))
```

## Dekorieren

```javascript
function trace (func) {
    return (...args) => {
        console.log(args)
        return func(...args)
    }
}

let factorial = (n) => (n <= 1) ? 1 : n * factorial(n-1)

factorial = trace(factorial)

console.log(factorial(3))
```