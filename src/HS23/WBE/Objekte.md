# Objekte


## Objektliterale

```javascript
let person = {
    name: "John Baker",
    age: 23,
    "exam rsults": [5,5, 5.0, 5.0, 6.0, 4.5]
}
```

## Zugriff

```javascript
console.log(person.name)
console.log(person["exam results"])
```

Zugriff auf nicht vorhandenes Attribut liefert "undefined"

## Optional

```javascript

console.log(person.age.month)  // TypeError
console.log(person.age?.month)  // undefined 
```

## Erweitern

```javascript
person.lastname = "Rüdiger"
```

## Entfernen

```javascript
let obj = {
    message: "ready",
    ready: true,
    tasks: 3
}

delete obj.message
```

## Attribute in Objekt

```javascript
let obj = {
    message: "ready",
    ready: true,
    tasks: 3
}

"message" in obj // true

```

## Methoden

```javascript

let cat = {
    type = "cat",
    sayHello: () => "Meow"
}

cat.sayHello() // Meow

```

## Interner Zugriff

```javascript

let cat = {
    type = "cat",
    sayHello() { "Meow from " + this.type }
}
```

- <span color="red">Pfeilnotation funktioniert nicht</span>

## Analyse

### Keys

```javascript
let obj = {a:1, b: 2}

Object.keys(obj)
```

### Values

```javascript
let obj = {a:1, b: 2}

Object.values(obj)
```

### Zusammenführen

```javascript
let obj1 = {a:1, b: 2}
let obj2 = {c:1, d: 2}
let obj3 = {e:1, f: 2}

Object.assign(obj1, obj2)

Object.assign(obj1, obj2, obj3)

let objCopy =  Object.assign({}, obj1)

objCopy == obj1 // false
```

## Spread Syntax

```javascript
let obj1 = {a:1, b: 2}
let obj2 = {c:1, d: 2}

{...obj1, ...obj2, f:4}
```


## Objekte Destrukturieren

```javascript
let obj = {a:1, b: 2}

let {a, b} = obj

console.log(a) //1

```