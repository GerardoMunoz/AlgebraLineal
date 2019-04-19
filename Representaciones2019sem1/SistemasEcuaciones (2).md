
# Sistema de ecuacioines
## Definiciones del libro
Defina (D) los conceptos a partir de la definición del libro [Nakos] o 
describa (d) los conceptos con sus propias palabras, según corresponda.   
Pg. 2
* (d) Variables:
* (d) Ecuación lineal: 
* (d) Coeficientes de la ecuación: 
* (d) Término constante: 
* (d) Ecuación homogénea: 
* (d) Ecuación homogénea asociada: 
* (d) Variable delantera: 
* (d) Variable libre: 

Pg. 3
* (D) Solución particular de una ecuación: 
* (d) Solución general de una ecuación: 
* (D) Conjunto solución de una ecuación: 
* (d) Parámetros de una ecuación: 

Pg. 4
* (d) Sistema de ecuaciones lineales: 
* (d) Coeficientes del sistema: 
* (d) Términos constantes: 
* (d) Sistema homogéneo: 
* (d) Sistema homogéneo asociado: 

Pg. 5 
* (D) Solución particular de un sistema: 
* (d) Solución general de un sistema (usar la notación vectorial de la clase): 
* (D) Conjunto solución de un sistema (usar la notación vectorial de la clase): 
* (D) Sistema consistente: 
* (D) Sistema inconsistente: 

Pg. 6
* (D) Solución trivial de un sistema: 
* (D) Solución no trivial de un sistema: 
* (d) Sustitución hacia atrás: 

<!--Pg. 7
* (D) Operaciones elementales en ecuaciones: 
* (D) Eliminación: 
* (D) Escalonamiento: 
* (D) Intercambio:--> 

## Ejercicios
Pg. 12
Ejercicios 1,2,3,4

Pg. 13
Ejercicio 13




## Conjunto de vectores de Términos Constantes que hacen que un sistema de ecuaciones lineal sea Consistente (CCC)

### Ejemplo de sistema consistente

El siguiente es un sistema de 2 ecuaciones lineales con 3 variables. 

$\left(\begin{aligned}
2x+4y+6z&=2\\
3x+6y+9z&=3
\end{aligned}\right)$

Este sistema es equivalente al siguiente sistema, multiplicando la primera ecuación por $1/2$ y la segunda ecuación por $1/3$

$\left(\begin{aligned}
x+2y+3z&=1\\
x+2y+3z&=1
\end{aligned}\right)$

Al restarle el primer renglón al segundo obtenemos

$\left(\begin{aligned}
x+2y+3z&=1\\
0x+0y+0z&=0
\end{aligned}\right)$

Como la segunda ecuación es $0=0$, no ayuda en la solución del sistema. Con la primera ecuación podemos obtener la **variable delantera** $x$ en función de las **variables libres** $y,z$. 

$x=1-2y-3z$

Esto implica que el sistema es consistente y tiene infintas soluciones.

### Ejemplo de sistema inconsistente con los mismos coeficientes

El siguiente sistema  tiene los mismos coeficientes que el ejercicio anterior pero varían los términos constantes

$\left(\begin{aligned}
2x+4y+6z&=2\\
3x+6y+9z&=6
\end{aligned}\right)$

Nuevamente, multiplicando la primera ecuación por $1/2$ y la segunda ecuación por $1/3$

$\left(\begin{aligned}
x+2y+3z&=1\\
x+2y+3z&=2
\end{aligned}\right)$

Al restarle el primer renglón al segundo obtenemos

$\left(\begin{aligned}
x+2y+3z&=1\\
0x+0y+0z&=1 !!!
\end{aligned}\right)$

Como la segunda ecuación es $0=1$, implica que el sistema es inconsistente.

### Conclusión de los ejemplos

En los dos ejemplos anteriores se muestra que para los mismos coeficientes hay unos *vectores términos contantes* (como $\left( \begin{matrix} 2\\ 3 \end{matrix} \right)$) que hacen al sistema consistente y otros *vectores términos constantes* (como $\left( \begin{matrix} 2\\ 6 \end{matrix} \right)$ ) que hacen al sistema inconsistente. Sería interesante poder conocer el **C**onjunto de los *vectores de términos **C**onstantes* que hacen al sistema **C**onsistente (CCC).

### Obtención del CCC para el ejemplo anterior

Partimos del mismo sistema de ecuaciones, pero colocamos unos términos constantes arbitrarios

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
3x+6y+9z&=b_1
\end{aligned}\right)$


Hacemos los mismos pasos para obtener eliminar la variable $x$ en la segunda ecuación

$\left(\begin{aligned}
x+2y+3z&=\frac{b_0}{2}\\
x+2y+3z&=\frac{b_1}{3}
\end{aligned}\right)$

y luego 

$\left(\begin{aligned}
x+2y+3z&=\frac{b_0}{2}\\
0x+0y+0z&=\frac{b_1}{3} - \frac{b_0}{2} 
\end{aligned}\right)$

De aquí podemos concluir que el CCC es

$\left\{ \left( \begin{matrix} b_0 \\ b_1 \end{matrix} \right) \mid \frac{b_1}{3} - \frac{b_0}{2} =0 \right\}$

Otra forma de obtener el CCC consiste en partir del sistema original

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
3x+6y+9z&=b_1
\end{aligned}\right)$

haciendo cero las variables paramétricas $y=0, \ \ z=0$

$\left(\begin{aligned}
2x&=b_0\\
3x&=b_1
\end{aligned}\right)$

entonces el CCC es

$\left\{ \left( \begin{matrix} 2x\\ 3x \end{matrix} \right) \mid x \in \mathbb{R} \right\}$

Más adelante estudiaremos con más detalle este CCC 

### Nota sobre igualdad de conjuntos (opcional)

Usualmente mostrar la igualdad de conjuntos $(A=B)$ implica dos demostraciones:
* Si $v \in A$ entonces $v \in B$.
* Si $u \in B$ entonces $u \in A$.

Para mostrar la igualdad de los conjuntos

$\left\{ \left( \begin{matrix} b_0 \\ b_1 \end{matrix} \right) \mid \frac{b_1}{3} - \frac{b_0}{2} =0 \right\}=
\left\{ \left( \begin{matrix} 2x\\ 3x \end{matrix} \right) \mid x \in \mathbb{R} \right\}$

 realizan las dos pruebas:
* Para la primera prueba comenzamos tomando un elemento del primer conjunto.
  * $v=\left( \begin{matrix} b_0 \\ b_1 \end{matrix} \right)$ donde $\frac{b_1}{3} - \frac{b_0}{2} =0$.
  * se despeja $b_1$ y se remplaza $v=\left( \begin{matrix} b_0 \\ \frac{3b_0}{2} \end{matrix} \right)$.
  * al realizar el cambio de variable $b_0=2x$ se obtiene  $v=\left( \begin{matrix} 2x \\ 3x \end{matrix}. \right)$ que es un elemento del segundo conjunto.

* Para la segunda prueba comenzamos con un elemento del segundo conjunto.
  * $u=\left( \begin{matrix} 2x \\ 3x \end{matrix} \right)$.
  * como $u$ cumple la condición $\frac{3x}{3} - \frac{2x}{2} =0$ entonces $u$ es un elemento del primer conjunto.








# Ejercicios de sistemas de ecuaciones

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
2x+2y+2z&=b_1
\end{aligned}\right)$

Para el anterior sistema de ecuaciones determine:
* Las variables.
* Los términos constantes.
* Un sistema de ecuaciones que elimina la variable delantera en las siguientes ecuaciones.
* Las variables libres.
* Las variables delanteras.
* El conjunto solución del sistema homogéneo.
* ¿Tiene el sistema homogéneo solución única?
* El conjunto de vectores de términos constantes para el cual el sistema es consistente (CCC).
*  ¿Es consistente el sistema para todos los vectores de términos constantes?



## Variables del sistema de ecuaciones

$\left( \begin{matrix} x \\ y \\ z \end{matrix} \right) \in \mathbb{R}^3$

## Términos constantes del sistema de ecuaciones

$\left( \begin{matrix} b_0 \\ b_1 \end{matrix} \right) \in \mathbb{R}^2$


## Sistema de ecuaciones eliminando la variable delantera en las ecuaciones siguientes

Para este ejemplo $x$ es la variable delantera de la primera ecuación, entonces la vamos a eliminar en la segunda ecuación. En este caso basta con restarle a la segunda ecuación a la primera ecuación y así obtenemos

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
0x-2y-4z&=b_1 - b_0
\end{aligned}\right)$

## Variables libres
La única variable que es libre en todas las ecuaciones es 

$z \in \mathbb{R}$.  

## Variables delanteras 
En este ejemplo obtuvimos una variable delantera por cada ecuación. Las variables delanteras son 

$\left( \begin{matrix} x \\ y  \end{matrix} \right) \in \mathbb{R}^2$



## El conjunto solución del sistema homogéneo: 
En el sistema homogéneo $b_0=0$ y $b_1=0$.

$\left(\begin{aligned}
2x+4y+6z&=0\\
0x-2y-4z&=0
\end{aligned}\right)$

Despejando la variable delantera $y$ de la segunda ecuación en términos de la variable libre $z$ se obtiene.


$y=-2z$

Luego se remplaza $y$ en la primera ecuación y se despeja la variable delantera $x$ en términos de la variable libre $z$.

$\begin{aligned}
2x+4(-2z)+6z&=0\\
2x-8z+6z&=0\\
2x-2z&=0\\
2x&=2z\\
x&=z\\
\end{aligned}$

Por lo tanto, el conjunto solución del sistema homogéneo es

$\left\{
\left(\begin{aligned}
z\\
-2z\\
z
\end{aligned}\right)
\mid z \in \mathbb{R}\right\}$


## ¿Tiene el sistema homogéneo solución única?
Cómo hay una variable libre entonces el sistema homogéneo no tiene solución única.

## El **C**onjunto de vectores de términos **C**onstantes para el cual el sistema es **C**onsistente (CCC).
Como este sistema

$\left(\begin{aligned}
2x+4y+6z&=b_0\\
0x-2y-4z&=b_1 - b_0
\end{aligned}\right)$

no puede ser inconsistente entonces el CCC es $\mathbb{R^2}$.

## ¿Es consistente el sistema para todos los términos constantes?

Por el punto anterior, el sistema sí es consistente para todos los términos constantes.























