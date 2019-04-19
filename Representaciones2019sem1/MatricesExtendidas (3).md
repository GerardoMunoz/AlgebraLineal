

# Matrices extendidas

## Definia(D) o describa(d) según corresponda
Pg. 4

* (d) Matriz: 
* (D) Matriz de coeficientes: 
* (D) Vector de (términos) constantes: 
* (D) Matriz aumentada: 

Pg. 15
* (d) Elementos de una matriz: 
* (d) Renglones de una matriz (En clase el PRIMER renglón es $r_0$): 
* (d) Columnas de una matriz: 
* (d) Tamaño de una matriz: 

Pg. 16 
* (d) Renglón cero (renglón de ceros): 
* (d) Renglón no cero (renglón no de ceros): 
* (d) Elemento delantero de un renglón: 
* (d) Uno delantero:
* (d) Propiedades E1,E2,E3,E4 de la forma Escalón:
* (d) Matriz en forma escalón:
* (d) Matriz en forma (escalón) reducida:
 
Pg. 7
* (D) Operaciones elementales en renglones:
* (D) Eliminación:
* (D) Escalonamiento:
* (D) Intercambio:

Pg. 17
* (D) Matrices equivalentes:

Pg. 18
* (D) Eliminación de Gauss:

Pg. 20
* (D) Teorema de la unicidad de la forma (escalón) reducida: 
* (D) Pivote: 
* (D) Lugar pivote (l-pivote): 

Pg. 21
* (d) Variables delanteras: 
* (d) Variables libres:
* (d) Parámetros:

Pg. 23 
* (d) Solución de un sistema lineal:

<!--Pg. 23,24,25
Teoremas 2,3,4,5-->


## Ejercicios del libro [Nakos]

Pg. 13
* Ejercicios 9,10, 11,12,13,14
* Compare los conjuntos solución 
  * de los ejercicios 10 y 11, 
  * de los ejercicios 13 y 14

Pgs. 27,28,29
* Ejercicios 1,2,3,4,5,16,19,21,23,45,46,47,48,
 


## Núcleo y espacio columna
Sea $A$ una matriz de tamaño $m \times n$

El **núcleo** de $A$ se denota $\text{Nu}(A)$ y es la solución del sistema homogéneo $[A:\vec{0}]$.

La **nulidad** de $A$ se denota $\nu(A)$ y es:
* el número de columnas de $A$ sin l-pivotes 
* coincide con el número de variables libres del sistema homogéneo $[A':\vec{0}]$ 
* también con el número de parámetros de la solución del sistema homogéneo $[A':\vec{0}]$

El **espacio columna** de $A$ se denota $\text{Col}(A)$ y es
* el conjunto de todos los vectores constantes $\vec{b}$ en función de las variables delanteras mientras las variables libres son cero.
* también corresponde al CCC del sistema $[A:\vec{b}]$ (Conjunto de vectores de términos Constantes $\vec{b}$ que hacen el sistema $[A:\vec{b}]$ sea Consistente).

El **rango** de $A$ se denota $\rho(A)$ y es:
* el número de columnas de $A$ con l-pivotes
* coincide con el número de variables delanteras de $[A':b']$ 
* también es el número de parámetros que tiene el espacio columna.


## Propiedades

* En cualquier matriz:
  * en cada columna y en cada renglón hay máximo un l-pivote, 
  * el número de pivotes es menor que el número de renglones y que el número de columnas  

* En matrices extendidas: 
  * Si en la columna de términos constantes hay un elemento delantero, el conjunto solución del sistema es vacío. En este caso se dice que el sistema de ecuaciones es __inconsistente__.
  * Si en la columna de términos constantes no hay un l-pivote entonces el conjunto solución no es vacío y se llama __consistente__.
  * Si todas las columnas de la matriz de coeficientes tienen l-pivote entonces el conjunto solución no tiene __infinitas soluciones__.  
  * Si el conjunto solución no es vacío y no tiene infinitas soluciones entonces tiene __solución única__

<!--Sea $[A:\vec{b}]$ una matriz extendida, donde: 
* la matriz de coeficientes $A$ tiene $m$ renglones y $n$ columnas es dada
* el vector de términos constantes $\vec{b}$ de $m$ renglones es arbitrario. 
-->

* Grupo de afirmaciones equivalentes de la unicidad de la solución
  * en cada columna hay un pivote
  * $A$ tiene $n$ pivotes
  * $\nu(A)=0$
  * $\text{Nu}(A)=\{\vec{0}\}$
  <!--* el sistema $[A:\vec{b}]$ no tiene infinitas soluciones -->
  * el sistema homogéneo $[A:\vec{0}]$ tiene solución única 

* Grupo de afirmaciones equivalentes de la totalidad de los términos constantes
  * en cada renglón hay un pivote
  * $A$ tiene $m$ pivotes
  * $\rho(A)=m$
  * $\text{Col}(A)=\mathbb{R}^m$
  * el sistema $[A:\vec{b}]$ es consistente para todo $\vec{b} \in \mathbb{R}^m$



## Ejemplo:
$\begin{bmatrix}
        2 & 1 & 2 & 2 & : & 6\\
        0 & 3 & 4 & 1 & : & 5\\
        0 & 3 & 4 & 1 & : & 0\\
        0 & 0 & 0 & 0 & : & 3
	\end{bmatrix}$
	$\begin{bmatrix}
        2 & 1 & 2 & 2 & : & 6\\
        0 & 3 & 4 & 1 & : & 5\\
        0 & 0 & 0 & 1 & : & 0\\
        0 & 0 & 0 & 0 & : & 0
	\end{bmatrix}$
	$\begin{bmatrix}
        2 & 1 & 2 & 2 & : & 6\\
        0 & 3 & 4 & 1 & : & 5\\
        0 & 0 & 1 & 1 & : & 0\\
        0 & 0 & 0 & 3 & : & 0
	\end{bmatrix}$
	$\begin{bmatrix}
        2 & 1 & 2 & 2 & : & 6\\
        0 & 3 & 4 & 1 & : & 5\\
        2 & 4 & 6 & 3 & : & 0\\
        0 & 0 & 0 & 0 & : & 0
	\end{bmatrix}$

La primera matriz extendida es inconsistente ya que tiene un elemento delantero en los términos constantes.

Las matrices extendidas segunda y tercera son consistentes ya que están en forma escalón y sus pivotes no son términos constantes. La segunda matriz tiene infinitas soluciones ya que hay una columna de la matriz de coeficientes sin pivote. La tercera matriz tiene solución única ya que todas las columnas de la matriz de coeficientes tienen pivotes.

Para la cuarta matriz extendida, no podemos afirmar a priori que sea inconsistente, porque no tiene elementos delanteros en los términos constantes. Tampoco podemos afirmar a priori que sea consistente, ya que no está en forma escalón. Con las operaciones elementales, esta matriz se puede transformar a una matriz en forma escalón, con la cual sí es posible identificar si es o no consistente.


## Ejercicios de Matriz extendida

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
2x+2y+2z&=b_1
\end{aligned}\right)$


Para el anterior sistema de ecuaciones encuentre:

* la respectiva matriz de coeficientes $A$ y su número de columnas $n$.
* El vector de términos constante $\vec{b}$ y su número de renglones $m$.
* La matriz extendida $[A:\vec{b}]$.
* Una matriz $A'$ equivalente a $A$ en forma escalón.
* Una matriz $A''$ equivalente a $A$ en forma escalón reducida.
* El sistema de ecuaciones homogéneo asociado a $[A'':\vec{0}]$.
* $\nu(A)$.
* $\text{Nu}(A)$.
* ¿$\text{Nu}(A)=\{\vec{0}\}$?
*  $\rho(A)$.
*  $\text{Col}(A)$, el espacio columna de $A$.
* ¿$\text{Col}(A)=\mathbb{R}^m$?


### La matriz de coeficientes $A$ y el número de columnas $n$
$A=\begin{bmatrix}
2&4&6\\
2&2&2
\end{bmatrix}$

$n=3$


### El vector de términos constante $b$ y el número de renglones $m$
$b=\left(\begin{matrix}
b_0\\
b_1
\end{matrix}\right)$

$m=2$

### La matriz extendida $[A:\vec{b}]$

$[A:\vec{b}]=\begin{bmatrix}
2&4&6&:&b_0\\
2&2&2&:&b_1
\end{bmatrix}$

### Una matriz $A'$ equivalente a $A$ en forma escalón

$\begin{bmatrix}
2&4&6\\
2&2&2
\end{bmatrix}
\stackrel{-r_0+r1->r1}{\longrightarrow}
\begin{bmatrix}
2&4&6\\
0&-2&-4
\end{bmatrix}$

$A'=\begin{bmatrix}
2&4&6\\
0&-2&-4
\end{bmatrix}$

### Una matriz $A''$ equivalente a $A$ en forma escalón reducida

$\begin{bmatrix}
2&4&6\\
0&-2&-4
\end{bmatrix}
\stackrel{2r_1+r0->r0}{\longrightarrow}
\begin{bmatrix}
2&0&-2\\
0&-2&-4
\end{bmatrix}$

$A''=\begin{bmatrix}
2&0&-2\\
0&-2&-4
\end{bmatrix}$

### El sistema de ecuaciones homogéneo asociado a $[A'':\vec{0}]$
$\left(\begin{aligned}
2x+0y-2z&=0\\
0x-2y-4z&=0
\end{aligned}\right)$


### La nulidad de $A$
$\nu(A)=1$

Ya que sólo hay una columna sin pivote, la cual corresponde a la variable libre

$z=t$

### $\text{Nu}(A)$. El núcleo de $A$
Encontramos la solución del sistema homogéneo. Primero se despeja la variable delantera de la segunda ecuación en términos del parámetro $z=t$.

$\begin{aligned}
-2y-4t&=0\\
-2y&=4t\\
y&=-2t\\
\end{aligned}$

Ahora se despeja la  variable delantera de la primera ecuación en términos del parámetro $z=t$.

$\begin{aligned}
2x-2t&=0\\
2x&=2t\\
x&=t\\
\end{aligned}$

La solución general es

$\left(\begin{matrix}
x\\
y\\
z
\end{matrix}\right)=
\left(\begin{matrix}
0\\
0\\
0
\end{matrix}\right)
+t\left(\begin{matrix}
1\\
-2\\
1
\end{matrix}\right)$

El núcleo de $A$, que corresponde al conjunto solución de $[A:\vec{0}]$ es

$\text{Nu}(A)=\left\{
\left(\begin{matrix}
0\\
0\\
0
\end{matrix}\right)
+
t\left(\begin{matrix}
1\\
-2\\
1
\end{matrix}\right)
\mid t \in \mathbb{R}
\right\}$




### ¿$\text{Nu}(A)=\{\vec{0}\}$?
No. Por el punto anterior se ve que el núcleo de $A$ tiene infinitos elementos. 

### El rango de $A$
$\rho(A)=2$


### $\text{Col}(A)$. El espacio columna de $A$
Al hacer la variable libre $z=0$ el sistema de ecuaciones queda

$\left(\begin{aligned}
2x+4y&=b_0\\
2x+2y&=b_1
\end{aligned}\right)$

y por lo tanto el conjunto de términos constantes en función de las variables delanteras $x,y$ es.

$\text{Col}(A)=\left\{
\left(\begin{aligned}
2x+4y\\
2x+2y
\end{aligned}\right)
\mid x,y \in \mathbb{R}
\right\}$



### ¿$\text{Col}(A)=\mathbb{R}^2$?

Sí. Como cada vector de términos constates es consistente entonces $\text{Col}(A)=\mathbb{R}^2$.

