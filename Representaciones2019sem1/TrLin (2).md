
# Transformaciones matriciales

## Defina (D) o describa (d) según corresponda

Pg. 307
* (D) transformaciones generales
* (d) dominio
* (d) codominio
* (d) contradominio

Pg. 308 
* (d) transformaciones iguales

Pg. 309
* (D) transformación matricial 

Pg. 310
* (d) Teoremas 1 y 2 
* (D) reflexiones 

Pg. 311
* (D) comprensión, expansión 

Pg. 312
* (D) cortes 

Pg. 313
* (D) rotaciones

Pg. 314
* (D) proyecciones 

Pg. 317, 318
* Ejercicios: 9, 11, 13, 15, 23, 29, 31, 33


Notas:
* Asumir los espacios vectoriales $V=\mathbb{R}^n$ y $W=\mathbb{R}^m$ cuando corresponda.
* Sólo hacer los ejemplos de las transformaciones lineales que tienen los anteriores espacios vectoriales. 

Pg. 320
* (D) transformación lineal
* Ejemplo 5

Pg. 321
* Ejemplo 6
* Ejemplo 7 (Toda transformación matricial es lineal.) 

<!--
Pg. 323
* Ejemplo 9
-->

Pg. 329
* Ejercicios 1,3,5,11,

Nota:
No hacer los ejemplos: 28(Pag. 333), 29(Pag. 334), {31, 32}(Pag. 336), 37(Pg. 339) {38,39}(Pg. 340), {40,41,42}(Pg. 341)

Pg. 331 
* (D) Núcleo (en clase usamos Nu(T), imagen, Im(T) en vez de Ker(T), contradominio, R(T) respectivamente)


Pg. 332
* Ejemplo 25, 26

Pg. 333
* Teorema 6
* Ejemplo 27
* (D) nulidad
* (D) rango

Pg. 335
* Teorema 7
* Ejemplo 30

Pg. 336
* Teorema 8

Pg. 337
* Ejemplo 33
* (D) transformación biunívoca (inyectiva)
* (D) transformación sobre (sobreyectiva)

Pg. 338
* Ejemplo 34
* Teorema 9

Pg. 339
* Ejemplos 35,36

<!--Pg. 340
* Teorema 11
* (D) isomorfismo
-->

Pg. 343
* Para los ejercicios 1,3,5,7  encuentre el generador de $\text{Nu}(T)$ y de $\text{Im}(T)$.

Pg. 344
* Ejercicios 21, 23,27,29


# Obtener la matriz $A$ de la transformación matricial $T_A$

Si $A=[\vec{v}_0 \ \  \vec{v}_1 \ \  \ldots \ \  \vec{v}_{\ddot{n}} ]$ donde $\ddot{n}=n-1$

y $T_A\begin{pmatrix}x_0\\x_1\\ \vdots \\x_{\ddot{n} }\end{pmatrix}=A\begin{pmatrix}x_0\\x_1\\ \vdots \\ x_{\ddot{n}} \end{pmatrix}=[v_0 \ \  v_1 \ \ \ldots \ \ v_{\ddot{n} }]\begin{pmatrix}x_0\\x_1\\ \vdots \\x_{\ddot{n}} \end{pmatrix}$ 

entonces 

$T_A\begin{pmatrix}1\\0\\ \vdots \\0 \end{pmatrix}=v_0$ ,
$\ \ T_A\begin{pmatrix}0\\1\\ \vdots \\0 \end{pmatrix}=v_1$,
$\ \ \vdots$
$\ \ T_A\begin{pmatrix}0\\0\\ \vdots \\1 \end{pmatrix}=v_{\ddot{n}}$

Por lo tanto $A=[\vec{v}_0 \ \  \vec{v}_1 \ \ \ldots \ \ \vec{v}_{\ddot{n} }]=\left[ T_A\begin{pmatrix}1\\0\\ \vdots \\0 \end{pmatrix} \ \ T_A\begin{pmatrix}0\\1\\ \vdots \\0 \end{pmatrix}\ \ \ldots\ \ T_A\begin{pmatrix}0\\0\\ \vdots \\1 \end{pmatrix} \right]$

lo cual se denota en clase como 

$A=T_A^*(I)=T_A^*\left(\left[ \begin{matrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots  \\ 0 & 0 & \cdots & 1 \end{matrix}\right]\right)=\left[ T_A\begin{pmatrix}1\\0\\ \vdots \\0 \end{pmatrix} \ \ T_A\begin{pmatrix}0\\1\\ \vdots \\0 \end{pmatrix}\ \ \ldots\ \ T_A\begin{pmatrix}0\\0\\ \vdots \\1 \end{pmatrix} \right]$


# Ejercicio
Sea $T_A:\mathbb{R}^n \rightarrow \mathbb{R}^m$ una transformación matricial dada por
$T_A\begin{pmatrix}x_0\\x_1\\x_2\end{pmatrix}=
\begin{pmatrix}3x_0-x_1\\x_0+4x_2\\2x_1\\x_1+5x_2\end{pmatrix}$

Encuentre:
* La dimensión $n$ del dominio de $T_A$.
* La dimensión $m$ del codominio de $T_A$.
* La matriz $A$ asociada a la transformación $T_A$.
* $\text{Nu}(T_A)$
* $\nu(T_A)$
* ¿Es $T_A$ inyectiva?
* $\text{Im}(T_A)$
* $\rho(T_A)$
* ¿Es $T_A$ sobreyectiva?


# La dimensión $n$ del dominio
La dimensión $n$ del dominio de $T_A:\mathbb{R}^n \rightarrow \mathbb{R}^m$ coincide con el número de renglones del vector que va a ser transformado.

n=3

# La dimensión $m$ del codominio
La dimensión $m$ del codominio de $T_A:\mathbb{R}^n \rightarrow \mathbb{R}^m$ coincide con el número de renglones del vector resultado de la transformación.

m=4

# La matriz $A$ asociada a la transformación $T_A$

$A=T_A^*(I)=
T_A^*\left(\left[ \begin{matrix} 1 & 0 &  0 \\ 0 & 1 &  0  \\ 0 & 0 &  1 \end{matrix}\right]\right)=
\left[ T_A\begin{pmatrix}1\\0\\0 \end{pmatrix} \ \ T_A\begin{pmatrix}0\\1\\0 \end{pmatrix}\  \ T_A\begin{pmatrix}0\\0 \\1 \end{pmatrix} \right]=
\left[ 
\begin{matrix}
3 & -1 & 0 \\
1 & 0  & 4 \\
0 & 2  & 0 \\
0 & 1  & 5
\end{matrix}
\right]$

# $\text{Nu}(T_A)$
El núcleo de $T_A$ es la solución del sistema homogéneo $[A:\vec{0}]$

$\left[ 
\begin{matrix}
3 & -1 & 0 & : & 0\\
1 & 0  & 4 & : & 0 \\
0 & 2  & 0 & : & 0 \\
0 & 1  & 5 & : & 0
\end{matrix}
\right]
\stackrel{r_0<->r_1}{\longrightarrow}
\left[ 
\begin{matrix}
1 & 0  & 4 & : & 0 \\
3 & -1 & 0 & : & 0\\
0 & 2  & 0 & : & 0 \\
0 & 1  & 5 & : & 0
\end{matrix}
\right]
\stackrel{-3r_0+r_1->r_1}{\longrightarrow}
\left[ 
\begin{matrix}
1 & 0  & 4 & : & 0 \\
0 & -1 & -12 & : & 0\\
0 & 2  & 0 & : & 0 \\
0 & 1  & 5 & : & 0
\end{matrix}
\right]
\stackrel{
\begin{aligned}
2r_1+r_2->r_2\\
r_1+r_3->r_3\\
\end{aligned}
}{\longrightarrow}
\left[ 
\begin{matrix}
1 & 0  & 4 & : & 0 \\
0 & -1 & -12 & : & 0\\
0 & 0  & -24 & : & 0 \\
0 & 0  & -7 & : & 0
\end{matrix}
\right]
\stackrel{-\frac{7}{24}r_2+r_3->r_3}{\longrightarrow}
\left[ 
\begin{matrix}
1 & 0  & 4 & : & 0 \\
0 & -1 & -12 & : & 0\\
0 & 0  & -24 & : & 0\\
0 & 0  & 0 & : & 0\\
\end{matrix}
\right]$

Como todas las columnas de $A$ tienen  l-pivote entonces la única solución del sistema homogéneo es el origen.

$\text{Nu}(T_A)=\left\{\begin{pmatrix}
0\\0\\0
\end{pmatrix}\right\}$

# $\nu(T_A)$
La nulidad de $T_A$ es el número de columnas de $A$ sin l-pivote

$\nu(T)=0$

# ¿Es $T_A$ inyectiva?
Como el sistema $[A:\vec{0}]$ tiene solución única entonces $T_A$ sí es inyectiva.

# $\text{Im}(T_A)$

$\text{Im}(T_A)=\text{Gen}(A)=\text{Gen}\left(\left[ 
\begin{matrix}
3 & -1 & 0 \\
1 & 0  & 4 \\
0 & 2  & 0 \\
0 & 1  & 5
\end{matrix}
\right]\right)$

Como todas las columnas tienen l-pivotes, no se puede quitar ninguna.

# $\rho(T_A)$
El rango de $T_A$ es el número de l-pivotes de $A$.

$\rho(T_A)=3$

# ¿Es $T_A$ sobreyectiva?
Como $A$ no tiene un l-pivote en cada renglón entonces $T_A$ no es sobreyectiva.



