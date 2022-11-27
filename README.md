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

$$M=\begin{pmatrix}
 a & b & c \\
 d & e & f \\
 \end{pmatrix}$$
 
 Aus dieser Matrix werden dann die Matrizen $A$, $A_1$ und $A_2$ gebildet.
 
 $$A=\begin{pmatrix}
 a & b\\
 d & e\\
 \end{pmatrix}$$
 
 $$A_1=\begin{pmatrix}
 c & b\\
 f & e\\
 \end{pmatrix}$$
 
 $$A_2=\begin{pmatrix}
 a & c\\
 b & f\\
 \end{pmatrix}$$
 
 Die Variabeln $x$ und $y$ werden dann durch die Division von Determinanten berechnet.
 $$x=\frac{det(A_1)}{det(A)}$$
 $$y=\frac{det(A_2)}{det(A)}$$

## solve_gauss
Löst Lineare Gleichungssysteme mit dem Gaussalgorithmus.
Beim Gaussalgorithmus wird die Matrix in diese Form gebracht:

$$M=\begin{pmatrix}
 1 & 0 & \dots & 0  & a_1\\
 0 & 1 & \dots & 0 & a_2\\
 \vdots & \vdots &  \ddots  & \vdots & \vdots \\
 0 & 0 & \dots & 1 & a_n\\
 \end{pmatrix}$$
 
Die Lösungen der Variablen sind dann:

$$ \mathbb{L}=\begin{pmatrix}
a_1\\
\vdots\\
a_n\\
\end{pmatrix}$$


## solve_simplex
Löst Lineare Maximierungsprobleme mit dem Simplexalgorithmus.
