# Differentialgleichung

## Transformation in DGL System 1. Ordnung


1. Die Differentialgleichung nach der höchsten vorkommenden Ableitung der unbekannten Funktion auflösen.
2. Neue Hilfsfunktionen für die unbekannte Funktion und deren Ableitungen bis Ordnung der höchsten Ableitung minus 1 einführen.
3. Das System erster Ordnung durch Ersetzen der höheren Ableitung durch die Funktionen aufstellen.
4. Das entsprechende Anfangswertproblem in vektorieller Form aufschreiben.

$$
Lq'' + Rq' + \frac{1}{C}q = U
$$

Aus Ableitungen die Funktion nehmen

$$
Lq''(t) + Rq'(t) + \frac{1}{C}q(t) = U
$$


$$
\Rightarrow
Lq''(t) = U - Rq'(t) - \frac{1}{C}q(t)
\\
\Rightarrow
q''(t) = \frac{1}{L} \cdot (U - Rq'(t) - \frac{1}{C}q(t))
$$


**Ersatzwerte für Funktionen erstellen**

$$
z_1(x) = q(t) \;\;\;\;\;\;, z_2(x) = q'(t) \\
z_1'(x) = q'(t) \;\;\;\;\;\;, z_2'(x) = q''(t) \\
$$

**Ersatzwerte einsetzen**

$$

q''(t) = \frac{1}{L} \cdot (U - Rq'(t) - \frac{1}{C}q(t))
\\
\Rightarrow
q''(t) 
= \frac{1}{L} \cdot (U - R \cdot z_2(x) - \frac{1}{C}\cdot z_1(x))
=
z_2'(x)
$$

**Gleichungssystem aufstellen**

$$

z'
=
\begin{pmatrix}
z_1'(x) \\
z_2(x)
\end{pmatrix}
=
\begin{pmatrix}
z_2(x) \\
\frac{1}{L} \cdot (U - R \cdot z_2(x) - \frac{1}{C}\cdot z_1(x))
\end{pmatrix}
$$


**Wenn Anfangswert gegeben:**

mit

$$
z(0)
=
\begin{pmatrix}
\sigma \\
\sigma
\end{pmatrix}
$$
