# Arrays

- Können von beliebigen Typen sein
- Typen können gemischt werden

## Is Array

```javascript
let data = [1, 2, 3]
typeof(data)    // 'object'
Array.isArray(data)     // true
```

## Methoden

### Hinzufügen

```javascript
let data = [1, 2, 3]
data.push(10)   // 4

data.push(11, 12)   // 6
```

### Letztes Element löschen

```javascript
let data = [1, 2, 3]
data.pop(10)   // 36
```

### Shift 

Entfernen am Array Anfang

```javascript
let data = [1, 2, 3]
data.shift()   // 1

console.log(data)   // [2, 3]
```

### Unshift
Entfernen am Array Anfang 

```javascript
let data = [1, 2, 3]
data.unshift(5)   // 4

console.log(data)   // [5, 1, 2, 3]
```

### Erstes Element in Array finden

```javascript
let data = [1, 2, 3, 1]
console.log(data.indexOf(1))   // 0
```

### Letzes Element in Array finden

```javascript
let data = [1, 2, 3, 1]
console.log(data.lastIndexOf(1))   // 3
```

### Bereich eines Arrays ausschneiden

```javascript
let data = [1, 2, 3, 1]
data.slice(1, 3)       // [2, 3]
```

### Arrays zusammenhängen

```javascript
let data = [1, 2, 3, 1]
data.concat([100, 101])     //[1, 2, 3, 1, 1000, 101]
```

## Iterieren

### Standard for schleife

```javascript
for (let i=0; i < myArray.length; i++) {
    console.log(myArray[i]);
}
```

### Einfachere Variante

```javascript
for (let item in myArray) {
    console.log(item);
}
```

## Spread-Syntax

```javascript
let parts = ["shoulders", "knees"]

["head", ...parts, "and", "toes"]   // ["head", "shoulders", "knees", "and", "toes"]
```

## Destrukturieren

```javascript
let numbers = [1,2,3]
let [a,b,c] = numbers

console.log(c)      // 3

```

## Abbilden

```javascript
let num = [5, 2, 9, -3, 15, 7, -5]

num.map(n => n*n)   // [25, 4, 81, 9, 225, 49, 25]
```

## Reduzieren

```javascript
let num = [5, 2, 9, -3, 15, 7, -5]

num.reduce((curr, next) => curr + next) // 30
```