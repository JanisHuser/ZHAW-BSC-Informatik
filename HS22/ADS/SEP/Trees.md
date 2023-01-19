# Operationen



## Höhe / Tiefe
```java
int height(Node root) {
	if (node == null) {
		return 0;
	}

	int lHeight = height(root.Left);
	int rHeight = height(root.Right);

	return max(lHeight, rHeight) +1;
}

```

# Generic Tree
A tree could contain multiple sub-nodes
![](https://media.geeksforgeeks.org/wp-content/uploads/20190612120758/generic-tree_gfg.png)



# Binary Tree
Eine Auflistung an Nodes
- Jede Node hat maximal zwei Sub-Nodes
![](https://www.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png)
# Sorted Binary Tree
- Struktur ist gleich wie Binary Tree
- Links ist das kleinere Element, Rechts das grössere

# Balanced Binary Tree
- Vollständig balancierter Baum
- Unterschied der Höhe links und Rechts darf 1 nicht überschreiten
**Depth**: $log_2(n+1)$
**Maximale Höhe**: $c_1 \cdot log(n) + c_2$

# B-Tree
- Self balanced
- Allows searches, sequential access, insertions and deletions in O(log n)

1. Werte in den Blättern einfügen
2. Zur Wurzel wachsend
3. Schlüssel in Blättern sind aufsteigen sortiert
4. Bereiche zwischen den Blättern zeigen auf weitere Blätter, die **NUR** Elemente innerhalb des Elternelements haben.
## Einfügen

![[Trees 2023-01-17 17.42.13.excalidraw]]

## Löschen
![[Trees 2023-01-17 17.48.53.excalidraw]]

![](https://martin-thoma.com/images/2012/07/b-tree-2-small.png)

# AVL Tree
The tree has to be balanced.

	BalanceFactor = height(left_subtree) - height(right_subtree)

- Left Rotation
- Right Rotation
- Left-Right Rotation (Do Left then Do Right Rotation)
- Right-Left Rotation (Do Right then do left rotation)