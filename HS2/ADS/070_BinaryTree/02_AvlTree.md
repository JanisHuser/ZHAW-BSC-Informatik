# AVL Tree

## Balance Factor
The Balance factor of a node is the difference between the height of the left subtree and that of the right subtree of that node.

$$

\text{Balance Factor}
=

(
	\text{Height of left subtree}
	-
	\text{Height of right subtree}
)

$$

### Range
The value of of the balance factor should always be between -1 and +1.


## Operations

### Left Rotation
Used when the right subtree has a greater height than the left subtree.

			p
			|
			x
		  /	  \
		a		y
			  /	  \
		 	b		c

1. Set the right subtree of x to b. And set p as the parent of y

					p
					|
			x		y
		  /	  \		  \
		a		b	    c


2. Set x as the left subtree of y

			p
			|
			y
		  /	  \
		x		c
	  /   \
	a	 	b


### Right Rotation
Used when the left subtree has a greater height than the right subtree

			p
			|
			y
		  /	  \
		x		a
	  /	  \
	 b		c

1. Set the left right subtree of x to b. And set p as the parrent of x.

			p
			|
			x		y
		  /	  	  /	  \
		c		b	    a


2. Set y as the right subtree of x

			p
			|
			x
		  /	  \
		a		y
			  /	  \
		 	b		c


### Left-Right Rotation

1. Do left rotation on x-y.


![](lr_1.png)
2. Do right rotation on y-z.

![](lr_2.png)


### Right-Left Rotation

1. Do right rotation on x-y
![](rl_1.png)

2. Do left rotation on y-z
![](rl_2.png)

## Inserting a Node

A new node is always inserted as a leaf node with balance factor equal to 0.

