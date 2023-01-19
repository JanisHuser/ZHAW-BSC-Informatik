# Binary search in sorted array

Searching a letter in a sorted array of letters.

## Idea
Usage of two indices $l$ and $r$.
Decrease the area the two indices span until the item has been found or no letter is left.


## Invariant

$$

\forall k,n;
\textcolor{red}{
	k \leq l, n \geq r;
}
\textcolor{lime}{
	a[k] \lt S \land a[n] > S
}

$$


## Algorithm

Repeat until S has been found or indices equal:

0. Set l to the beginning and r to the end of the array.
1. take m as index between l and r
2. If $ a[m] == S $ abort as value has been found
3. If $ a[m] < S \rightarrow l = m $ 
4. If $ a[m] > S \rightarrow r = m $
5. If $ l + 1 = r $ abort, as there are no more values between l and r

## Implementation

```java
static int binary(int[] a, int s) {
	int l = -1;
	int r = a.length;
	int m = (1 + r) / 2;

	while (l + 1 < r && a[m] != s) {
		if (a[m] < s) {
			l = m;
		} else {
			r = m;
		}
		m = (l + r) / 2;
	}

	return (a[m] == s) ? m : -1;
}
```

### $O(\log_2 n)$

Finding the search is done in some steps, the array must be sorted.
