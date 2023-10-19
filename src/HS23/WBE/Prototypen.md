# Prototypen

```javascript
function speak (line) {
    console.log(`The ${this.type} rabbit says '${line}'`)
}

let whiteRabbit = {type: "white" , speak}
let hungryRabbit = {type: "hungry", speak}

hungryRabbit.speak("I could use a carrot right now.")

// → The hungry rabbit says 'I could use a carrot right now.
```

## Strict Mode

```javascript
"use strict"

function speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`)
}

speak("I could use a carrot right now.")

// -> TypeError 'Cannot read property type of undefined'
```

## Call / Apply

```javascript
function speak (line) {
    console.log(`The ${this.type} rabbit says '${line}'`)
}

let hungryRabbit = {type: "hungry", speak}

speak.call(hungryRabbit, "Burp!")  // The hungry rabbit says 'Burp!'   
speak.apply(hungryRabbit, ["Burp!"])   // The hungry rabbit says 'Burp!'
```

## Bind

```javascript
function speak (line) {
    console.log(`The ${this.type} rabbit says '${line}'`)
}

let hungryRabbit = {type: "hungry", speak}

let boundSpeak = speak.bind(hungryRabbit)

boundSpeak("Burp!")   // The hungry rabbit says 'Burp!'   
```


## Lambdas

```javascript
let test = []
test.map(n => n**2)
```

## Prototype Chain

```javascript
var Dragon = function(location){  
    /*
     * <Function>.call is a method that executes the defined function,
     * but with the "this" variable pointing to the first argument,
     * and the rest of the arguments being arguments of the function
     * that is being "called". This essentially performs all of
     * LivingEntity's constructor logic on Dragon's "this".
     */
    LivingEntity.call(this, location);
    //canFly is an attribute of the constructed object and not Dragon's prototype
    this.canFly = true;
};

/*
 * Object.create(object) creates an object with a prototype of the
 * passed in object. This example will return an object
 * with a prototype that has the "moveWest" and "makeSound" functions,
 * but not x, y, or z attributes.
 */
Dragon.prototype = Object.create(LivingEntity.prototype);

/*
 * If we didn't reset the prototype's constructor
 * attribute, it would look like any Dragon objects
 * were constructed with a LivingEntity constructor
 */
Dragon.prototype.constructor = Dragon;

/*
 * Now we can assign prototype attributes to Dragon without affecting
 * the prototype of LivingEntity.
 */
Dragon.prototype.fly = function(y){  
    this.y += y;
}

var sparky = new Dragon({  
    x: 0,
    y: 0,
    z: 0
});  
```

## Klassen

```javascript
class DateFormatter extends Date {
  get FormattedDate() {
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return `${this.getDate()}-${months[this.getMonth()]}-${this.getFullYear()}`;
  }
}

console.log(new DateFormatter('August 19, 1975 23:15:30').FormattedDate);
// Expected output: "19-Aug-1975"

```

### Properties

```javascript

class Person {
    constructor(name) {
        this.name = name;
    }
    get name() {
        return this._name;
    }
    set name(newName) {
        newName = newName.trim();
        if (newName === '') {
            throw 'The name cannot be empty';
        }
        this._name = newName;
    }
}

let p1 = new Person()
p1.Name = "hey"

console.log(p1.Name) // hey
```