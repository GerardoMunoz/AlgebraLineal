# Representaciones de un sistema de ecuaciones

<!--
Para las siguientes representaciones asumimos una matriz $A$ de tamaño $2 \times 3$, que sus columnas son $v_0$, $v_1$ y $v_2$ y que sus renglones son $w_0^t$ y $w_1^t$
$$A=\begin{bmatrix}v_0 & v_1 & v_2 \end{bmatrix}=\begin{bmatrix}w^t_0 \\ w^t_1 \end{bmatrix}, \ \ \  \vec{x}=\begin{bmatrix}x_0 \\ x_1 \\ x_2 \end{bmatrix}, \ \ \  \vec{x}=\begin{bmatrix}b_0 \\ b_1 \end{bmatrix}$$
-->

Para las siguientes representaciones asumimos una matriz $A$ de tamaño $2 \times 3$ donde sus columnas son $v_0$, $v_1$ y $v_2$ 

$$A=\begin{bmatrix}v_0 & v_1 & v_2 \end{bmatrix}, \ \ \  \vec{x}=\begin{bmatrix}x_0 \\ x_1 \\ x_2 \end{bmatrix}, \ \ \  \vec{b}=\begin{bmatrix}b_0 \\ b_1 \end{bmatrix}, \ \ \ S=\{v_0,v_1,v_2\}$$


| Sistema de  Ecuaciones | Matriz  Extendida  |  Combinación Lineal de vectores  | Matriz por vector | Transformación Matricial     |
|------------|-----------|-------------|----------------|-|
|El planteamiento de problemas|El algoritmo de Gauss|La representación gráfica de vectores|Las operaciones matriciales|La composición de funciones|
| $\left.\begin{aligned}2x_0+4x_1+6x_2&=b_0\\2x_0+2x_1+2x_2&=b_1\end{aligned}\right.$ | $\begin{aligned}& \ \ \  x_0 \  \ \ x_1 \  \ \ x_2\\&\begin{bmatrix}2&4&6&:&b_0\\2&2&2&:&b_1\end{bmatrix}\end{aligned}$  | $\begin{aligned}x_0\begin{pmatrix}2\\2\end{pmatrix}+x_1\begin{pmatrix}4\\2\end{pmatrix}+x_2\begin{pmatrix}6\\2\end{pmatrix}=\begin{pmatrix}b_0\\b_1\end{pmatrix}\end{aligned}$ | $\begin{bmatrix}2&4&6\\2&2&2\end{bmatrix}\begin{pmatrix}x_0\\x_1\\x_2\end{pmatrix}=\begin{pmatrix}b_0\\b_1\end{pmatrix}$|$T_A\begin{pmatrix}x_0\\x_1\\x_2\end{pmatrix}=\begin{pmatrix}2x_0+4x_1+6x_2\\2x_0+2x_1+2x_2\end{pmatrix}=\begin{pmatrix}b_0\\b_1\end{pmatrix}$|
|- |$[A:\vec{b}]$ |$x_0 \vec{v_0}+x_1 \vec{v_1}+x_2 \vec{v_2}= \vec{b}$|$A\vec{x}=\vec{b}$| $T_A(\vec{x})=\vec{b}$ |
|Sistema de $m$ de ecuaciones con $n$ variables |-   | Combinación lineal de $n$ vectores de $\mathbb{R}^m$ | $A_{m \times n}$, Matriz $A$  de tamaño $m \times n$ | $T_A:\mathbb{R}^m \rightarrow \mathbb{R}^n$|
|<u>Solución del S.H. </u>| - | -  | $\text{Nu}(A)$, **Espacio nulo** de $A$  | $\text{Nu}(T_A)$, **Núcleo** (o Kernel) de $T_A$ |
|Número de variables libres del S.H.| <u>Número de columnas de $A$ sin l-pivotes</u> | - | $\nu(A)$, **nulidad** de $A$ | $\nu(T_A)$, **nulidad** de $T_A$ |
|¿Tiene el S.H. solución única? | ¿Tiene $A$ un l-pivotes en cada columna? | <p>¿Es $S$ **Linealmente Independiente** (L. I.)? </p> <p>¿No es $S$ **Linealmente Dependiente** (L. D.)? </p><p>¿Ningún vector se puede escribir como combinación lineal de los otros?</p>|<p> ¿ $\nu(A)=0$? </p><p>¿$\text{Nu}(A)=\{\vec{0}\}$?</p>| ¿Es $T_A$  inyectiva? |  
|Conjunto de VTC consistentes | - | $\text{Gen}(S)$, **Espacio generado** por $S$ | <p>$\text{Col}(A)$, **Espacio columna** de A.</p> <p>(Se pueden <u>quitar columnas</u> sin l-pivotes) </p>| $\text{Im}(T_A)$, **Imagen** de $T_A$ |
|Número de variables delanteras del S.H.| <u>Número de l-pivotes de $A$</u>   |  $\text{Dim}(\text{Gen}(S))$ | $\rho(A)$, **rango** de $A$ | $\rho(T_A)$, **rango** de $T_A$ |
|¿Es consistente para todo VTC? |<p> ¿$A$ tiene un l-pivotes en cada renglón?</p><p> ¿$A$ tiene $m$ l-pivotes?</p><p> ¿Si $B \sim A$ entonces $B$ no tiene renglones de ceros?</p>   |<p>¿$\text{Dim}(\text{Gen}(S))=m$?</p><p> ¿ $\text{Gen}(S)=\mathbb{R}^m$?</p> | <p>¿$\rho(A)=m$? </p><p>¿$\text{Col}(A)=\mathbb{R}^m$?</p>| ¿Es $T_A$  sobreyectiva? |  

<!--|Número $m$ de variables| - | Número $m$ de vectores en $S$|   Número $m$ de columnas de $A$ | Dimensión $m$ del codominio de $T_A$|-->


Abreviaturas: 
* l-pivote: lugar del pivote en una matriz escalón equivalente
* L.I.: Linealmente Independiente
* S.H.: Sistema Homogéneo
* VTC: Vector(es) de Términos Constantes ($\vec{b}$)

<!--* CCC Conjunto de vectores de términos Constantes ($\vec{b}$) Consistentes
* CTTC Consistente para todo vector de términos constantes-->
 



.
