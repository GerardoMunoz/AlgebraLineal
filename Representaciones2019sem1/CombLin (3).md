# Combinación Lineal


Defina (D) o describa (d) según corresponda basado en [Nakos]

Pg. 62
* (d) vector
* (d) elemento o componente 
* (d) tamaño del vector
* (d) $\mathbb{R}^n$
* (d) coordenadas
* (d) plano de coordenadas cartesianas
* (d) punto
* (d) flecha

Pg. 63
* (D) vectores iguales
* (D) suma vectorial
* (d) ley del paralelogramo
* (d) escalar
* (D) multiplicación por escalar
* (D) opuesto

Pg. 64
* (D) diferencia (resta)
* (D) vector cero
* (d) vectores de la base estándar (columnas de la identidad)

Pg. 66
* (d) conjunto de vectores
* (D) sucesión de vectores (lista de vectores)
* (d) matrices como sucesión de vectores

Pg. 67
* (D) COMBINACIÓN LINEAL (de vectores)
* (d) coeficientes de la combinación lineal

Pg. 69
* (d) relación entre sistema lineal y combinación lineal

Pg. 75, 76, 77, 78
*  Ejercicios 5, 7, 21, 23, 27, 33, 35, 45a, 46, 47, 51, 52


Pg. 154
* (d) tamaño de una matriz
* (d) renglón i (en clase usualmente el primer elemento es el cero)
* (d) columna j (en clase usualmente el primer elemento es el cero)
* (d) elemento i,j (en clase usualmente el primer elemento es el cero)
* (d) matriz como secuencia (lista) de columnas
* (d) matriz renglón
* (d) matriz columna o vector
* (d) matriz cuadrada


Pg. 155
* (D) matriz cero
* (d) diagonal principal
* (d) matriz triangular superior e inferior
* (d) matriz diagonal
* (d) matriz escalar
* (D) matrices iguales
* (D) suma de matrices
* (D) diferencia de matrices (resta de matrices)

Pg.156 
* (D) producto por escalar (escalar por matriz)
* (D) matriz opuesta
* (D) leyes para la suma de matrices y multiplicación por escalar

Pg 167
* Ejercicios 1,4,5,

Pg. 105
* (D) Matriz por vector

Pg. 106
* (d) Matriz identidad

Pg. 107
* (d) relación entre sistema lineal y matriz por vector


Pg. 111
* Ejercicios: 1, 3 ($A$ y $v$ están dadas al principio), 5 (tiene que encontrar $A$ y $b$), 7


Pg. 108
* (d) espacio nulo (núcleo)
* (d) nulidad (En clase la nulidad es la dimensión del espacio nulo)

Pg. 109
* (d) (relación entre la solución homogénea y la no homogénea)

Pg. 112 
* Ejercicios: 14,15, 
* Encuentre el espacio nulo de A en el ejercicio 15

Pgs. 96,97
* (D) linealmente dependiente
* (D) linealmente independiente

Pg. 98
* Teorema 11 (aún no se ha visto el ángulo)

Pg. 99
* (d) criterios de independencia lineal

Pg. 100, 101, 102
* (d) Teoremas 14,15,16

Pg. 102
* (d) interpretación geométrica 

Pg. 103, 104
* Ejercicios: 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 22,

Pg. 90
* (D) espacio generado
* (d) conjunto generador

Pg. 92
* (d) reducción del conjunto generador

Pg. 93
* (d) Teorema 10
* (d) relación entre el generador y los sistemas lineales

Pg. 94
* (d) interpretación geométrica del conjunto generado
* Ejercicios:  1,2,3,4

Pg. 95, 96
Ejercicios: 7, 11a, 15, 20, 21, 23, 24, 28, 29

Pg. 226
* (D) subespacio de $\mathbb{R}^n$
Pg. 228
* (d) el generado de un conjunto de vectores es un subespacio de $\mathbb{R}^n$

Otros
* (hechos) para todo subespacio $V$ de $\mathbb{R}^m$:
  * existe un conjunto $S \subseteq \mathbb{R}^m$ de hasta  $m$ vectores tal que   $\text{Gen}(S)=V$. 
  * existe un sistema de hasta $m$ ecuaciones y $m$ variables tal que $V$ es el conjunto solución del sistema.   


* (D) si $S \subseteq \mathbb{R}^m$.  La **dimensión de  $\text{Gen}(S)$**  de  es:
  * el máximo número de vectores L.I. de $S$.
  * el número de l-pivotes (el rango) de la matriz $A$ asociada a $S$.

Pg 233
Para los ejercicios de 1 al 9 encuentre un conjunto que genera el subespacio.






<!-- 
Pgs. 158, 159, 160, 161, 162
* (D) multiplicación matricial
* (d) cálculo renglón-columna
* (D) leyes de la multiplicación matricial
* (d) potencias de una matriz cuadrada
* (d) problemas en la mult. de matr. 
Pg. ---
* ejerccicios -------
-->



<!--
$c_0\begin{pmatrix}1\\0\\2\end{pmatrix}+c_1\begin{pmatrix}0\\1\\2\end{pmatrix}+c_2\begin{pmatrix}1\\1\\0\end{pmatrix}+c_1\begin{pmatrix}1\\1\\1\end{pmatrix}$
-->

# Ejercicio
$S=\left\{ 
\begin{pmatrix}1\\0\\2\end{pmatrix},
\begin{pmatrix}0\\1\\2\end{pmatrix},
\begin{pmatrix}1\\-1\\0\end{pmatrix},
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\}$

Para el anterior conjunto de vectores $S$ encuentre:

* La matriz $A$ asociada a $S$. 
* El número $n$ de vectores de $S$.
* La dimensión de $\mathbb{R}^m$ que contiene a $S$.
* El espacio nulo de $S$.
* La dimensión del espacio nulo de $S$.
* Geométricamente que es el espacio nulo de $S$.
* ¿Es Linealmente Independiente $S$? 
* $\text{Gen}(S)$.
* La dimensión de  $\text{Gen}(S)$.
* Geométricamente que es el espacio generado por $S$.
* ¿$S$ genera todo $\mathbb{R}^m$?

# La matriz $A$ asociada a $S$
$A=\left[ 
\begin{matrix}
1 & 0 & 1  & 1\\
0 & 1 & -1 & 1\\
2 & 2 & 0  & 1
\end{matrix},
\right]$

# El número $n$ de vectores de $S$
$n=4$

# La dimensión de $\mathbb{R}^m$ que contiene a $S$
$m=3$

# El espacio nulo de $S$
El espacio nulo es la solución del sistema homogéneo $[A:\vec{0}]$

$A=\left[ 
\begin{matrix}
1 & 0 & 1  & 1 &:& 0\\
0 & 1 & -1 & 1 &:& 0\\
2 & 2 & 0  & 1 &:& 0
\end{matrix},
\right]
\stackrel{-2r_0+r2->r2}{\rightarrow}
\left[ 
\begin{matrix}
1 & 0 & 1  & 1 &:& 0\\
0 & 1 & -1 & 1 &:& 0\\
0 & 2 & -2  & -1 &:& 0
\end{matrix},
\right]
\stackrel{-2r_1+r2->r2}{\rightarrow}
\left[ 
\begin{matrix}
1 & 0 & 1  & 1 &:& 0\\
0 & 1 & -1 & 1 &:& 0\\
0 & 0 & 0  & -3 &:& 0
\end{matrix},
\right]$

Si las variables asociadas a cada columna son $x_0, x_1, x_2, x_3$ respectivamente entonces $x_2$ es la única variable libre

$x_2=t$

A continuación se despejan las variables delanteras $x_0, x_1, x_3$ de derecha a izquierda

$\begin{aligned}
-3x_3&=0\\
x_3&=0\\
\end{aligned}$

$\begin{aligned}
x_1-t+0
&=0\\
x_1&=t\\
\end{aligned}$

$\begin{aligned}
x_0+t+0&=0\\
x_0&=-t\\
\end{aligned}$

La solución general es 

$\begin{pmatrix}x_0\\x_1\\x_2\\x_3\end{pmatrix}=
\begin{pmatrix}0\\0\\0\\0\end{pmatrix}
+t\begin{pmatrix}-1\\1\\1\\0\end{pmatrix}$

y por lo tanto el espacio nulo es

$\begin{aligned}
Nu(S)&=\left\{ 
\begin{pmatrix}0\\0\\0\\0\end{pmatrix}
+t\begin{pmatrix}-1\\1\\1\\0\end{pmatrix}
\mid t \in \mathbb{R}
\right\}\\
&=\text{Gen}\left\{ 
\begin{pmatrix}-1\\1\\
1\\0\end{pmatrix}
\right\}
\end{aligned}$



# La dimensión del espacio nulo de $S$
Como es el número de variables libres del sistema homogéneo $[A:\vec{0}]$, entonces corresponde la nulidad de $A$.

$\nu(A)=1$

# Geométricamente que es el espacio nulo de $S$

Como $\nu(A)=1$ entonces el espacio nulo es una recta en $\mathbb{R}^4$ que pasa por el origen.

# ¿Es Linealmente independiente $S$? 
No son L.I. porque hay una variable libre.

# $\text{Gen}(S)$
Se pueden eliminar las columnas que no tienen l-pivote

$\begin{aligned}
\text{Gen}(S)&=\text{Gen}\left\{ 
\begin{pmatrix}1\\0\\2\end{pmatrix},
\begin{pmatrix}0\\1\\2\end{pmatrix},
\begin{pmatrix}1\\-1\\0\end{pmatrix},
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\}\\
&=\text{Gen}\left\{ 
\begin{pmatrix}1\\0\\2\end{pmatrix},
\begin{pmatrix}0\\1\\2\end{pmatrix},
\begin{pmatrix}1\\1\\1\end{pmatrix}
\right\}\\
\end{aligned}$


# La dimensión de$\text{Gen}(S)$
Corresponde al número de l-pivotes de $A$, es decir al rango de $A$.

$\rho(A)=3$

# Geométricamente que es el espacio generado por $S$

Como $\rho(A)=3$, entonces el espacio generado es un espacio de 3 dimensiones en $\mathbb{R}^3$ . Es decir, es todo el espacio $\mathbb{R}^3$.

# ¿$S$ genera todo $\mathbb{R}^m$?
Sí, porque para que genere todo $\mathbb{R}^m$ se requiere que haya $m$ l-pivotes. Es decir, un pivote por cada renglón.



