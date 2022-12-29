# Hashing

Storing value s in a array at their "hashed" position.

## Advantages
- Efficient searching and inserting
- "Simple" binary trees might degenerate, hash tables are more resilient
- Fast and easy implementation


## Disadvantages
- Finding min and max is complicated
- Ordered output is impossible
- Ranged search, partial string search is impossible.

## Issues

- Multiple hash values might span a giant area
- The original key cannot be restored => original key value has to be stored aswell
- Hash functions might be hard to find
- Multiple different keys might result the same hashed value resulting in a collision

### Strings

Hashed strings require a huge amount of storag
$$
\text{Char} \times 256^{Position-1}
$$

#### Horner schema
The Horner schema minimizes the bytes needed to store a polygon

$$

2x^{4}-4x^{3}-5x^{2}+7x+11\;=\;(((2\cdot x-4)\cdot x-5)\cdot x+7)\cdot x+11
$$

## Most used implementation

### Divisionsrestmethode:
h(k) = k mod M

M often is a prime number.

### Multiplikationsmethode: 

h(k) = [m * ((k * c) mod 1)]

m = Anzahl Hashadressen 
0 < c < 1 (Goldener Schnitt = 0.618033)



## Algorithums

```java
public class Hashtable {
	final int MAX = 97;
	final int INVALID = Integer.MINVALUE;
	int[] keys = new int[MAX];
	int[] vals = new int[MAX];

	private void init() {
		for (int i=0; i < MAX; i++) {
			key[i] = INVALID;
		}
	}

	private int h(int key) {
		return key% MAX;
	}

	public void put(int key, int val) {
		int h = h(key);
		if (keys[h] == INVALID) {
			keys[h] = key;
			vals[h] = val;
		}
		else {
			// COLLISION
		}
	}

	public int get(int key) {
		int h = h(key);
		if (keys[h] == key) {
			return vals[h];
		}

		return INVALID;
	}
}
```


## Java implementation

Use prime numbers when hashing.

```java
public class Employee {
	int employeeId;
	String name;
	Department dept;

	@Override
	public int hashCode() {
		int hash = 1;
		hash = hash * 13 + employeeId;
		hash = hash * 17 + name.hashCode();
		hash = hash * 31 + (dept == null ? 0 : dept.hashCode());
		return hash;
	}
}

```