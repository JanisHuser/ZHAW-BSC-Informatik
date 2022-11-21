# Iteratives Verfahren

Wird nur dann angewendet, wenn grossteil der Matrix in der Diagonale ist.


\\[
Ax = b => (R + D + L)x = b
\\]


\\[
(D+(R+L))x = b => Dx + (R+L)x = b
\\]

\\[
Dx = -(R+L)x+b
\\]

\\[
x^{k+1} = D^{-1}(R+L)x^{k}+X^{-1}*b
\\]