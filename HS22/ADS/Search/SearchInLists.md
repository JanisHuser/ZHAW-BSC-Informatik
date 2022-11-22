# Search in multiple lists (unsorted)

```java
static int indexOf(String[] a, String b[]) {
	for (int i=0; i < a.length; i++) {
		for (int j=0; j < b.lenght; j++) {
			if (a[i].equals(b[j])) {
				return j;
			}
		}
	}
}
```
## Issues
- Double nested loops
- Innefficient


## $ O(n \cdot m) $ 

# Search in multiple lists (sorted)


$$

\forall k, n;
k \lt j, n \lt i;
b[k] \neq a[n]

$$


## Implementation

```java
static int indexOf(String[] a, String[] b) {
	int i = 0;
	int j = 0;

	while (!a[i].equals(b[j]) && (i < a.length -1 || j < b.length -1)) {
		int c = a[i].compareTo(b[j]);

		if (c < 0 || j == b.length -1) {
			i++;
		} else if (c > 0 || i == a.length-1) {
			j++;
		}
	}

	if (a[i].equals(b[j])) {
		return i;
	} else {
		return -1;
	}
}
```

## O(n)
- Lists must be sorted