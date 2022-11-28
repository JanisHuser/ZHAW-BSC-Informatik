# Jacobi Verfahren

Ein Algorithmus zu näherungsweisen Lösung von linearen Gleichungssystemen.

## Beschreibung

$$

\begin{matrix}
a_{11} \cdot x_1 + \cdots + a_{1n} \cdot x_n = b_1 \\
a_{21} \cdot x_1 + \cdots + a_{2n} \cdot x_n = b_2 \\
							\vdots \\
a_{n1} \cdot x_1 + \cdots + a_{mn} \cdot x_n = b_n
\end{matrix}

$$


$$

x_i^{m+1}
:=
\frac{1}{a_{ii}}

\left(
b_i
-
\sum\limits_{j \neq i}
a_{ij}
\cdot x_j^(m)
\right)
,
i = 1,...,n
$$

## Algorithmus

Gegeben Startvektor $ x^{alt} $
für $ m=1,... $ bis Erfüllung eines Abbruchkriteriums
	$ x = b $
	fürr $ i=1 $ bis $ n $
		für $ j = 1 $ bis $ n $
			falls $ j \neq i $
				$ x_i = x_i - a_{ij} x_j^{alt};
		ende
		$ x_i = x_i / a_{ii}; $
	
	ende
	$ x^{alt} = x_i;
ende