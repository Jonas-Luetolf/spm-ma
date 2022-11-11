# SPM Ma 2022/2023
## Schwerpunktfach Mathematik Lineare Algebra
## dependencies
- [NumPy](https://numpy.org/) Copyright (c) 2005-2022, NumPy Developers


## solve_det
Löst Lineare Gleichungssysteme mit zwei Variabeln.
z.B. 
$$ax+by=c$$
$$dx+ey=f$$
Aus den beiden Gleichungen wird eine Matrix geblidet.

$$A=\begin{pmatrix}
 a & b & c \\
 d & e & f \\
 \end{pmatrix}$$
 
 Aus dieser Matrix werden dann die Matrizen $A_1$ und $A_2$. Die Variabeln $x$ und $y$ werden dann mit der Determinantenmethode berechnet.
 $$x=\frac{det(A_1)}{det(A)}$$
 $$y=\frac{det(A_2)}{det(A)}$$
