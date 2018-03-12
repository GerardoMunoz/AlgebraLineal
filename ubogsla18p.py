import IPython
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import math


def angulo(ax,u,v,r,nombre='',fontsize=15):
    alpha_u=math.degrees(math.atan2(u[1],u[0]))
    alpha_v=math.degrees(math.atan2(v[1],v[0]))
    ax.add_patch(Arc((0,0),r,r,0,alpha_u,alpha_v))
    alpha=(alpha_u+alpha_v)/2
    x=r*math.cos(math.radians(alpha))/2
    y=r*math.sin(math.radians(alpha))/2
    if nombre!='':
        ax.text(x,y,nombre,fontsize=fontsize)


#def bloques(lista2):#.as_explicit()
    #recibe una matriz por bloques de sympy.Matrix y la retorna en un solo bloque 
#    ren0=None
#    for renglon in lista2:
#        elem0=renglon[0]
#        for elemento in renglon[1:]:
#            elem0=elem0.row_join(elemento)
            #print('p1',elem0,elemento)
#        if ren0 == None:
#            ren0=elem0
#        else:
#            ren0=ren0.col_join(elem0)
        #print('p2',elem0,ren0)
#    return None#ren0#.as_explicit()

def ejes(x0,y0,x1,y1,k=1):
    #fig=plt.figure(figsize=(8,6),dpi=80)
    #ax = plt.Axes(fig,[0.,0.,1.,1.])
    ax = plt.axes([0.,0.,k,k*1.34*(y1-y0)/(x1-x0)])
    ax.set_xlim(x0,x1)
    ax.set_ylim(y0,y1)
    return ax

def ejes3d(x0,x1,y0,y1,z0,z1):
    #fig=plt.figure(figsize=(8,6),dpi=80)
    #ax = plt.Axes(fig,[0.,0.,1.,1.])
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.set_xlim([x0,x1])
    ax.set_ylim([y0,y1])
    ax.set_zlim([z0,z1])
    return ax


def flecha(ax,v,sumar=[0,0],nombre='',fontsize=15,**kwargs):
    ax.arrow(float(sumar[0]),float(sumar[1]),float(v[0]),float(v[1]),head_width=0.02,head_length=0.02, length_includes_head=True,**kwargs)
    if nombre!='':
        ax.text(v[0]+sumar[0],v[1]+sumar[1],nombre,fontsize=fontsize)

from mpl_toolkits.mplot3d import Axes3D

def flecha3d(ax,A:Matrix,B:Matrix=None,nombres=None,fontsize=15,**kwargs):#problemas en 2D
    if B==None:
        B=zeros(*A.shape)
    elif A.shape!=B.shape:
        raise ValueError('flechas(ax,A) o flechas(ax,A,B) y A y B son del mismo tamaño')

    if isinstance(nombres,str):
        if A.cols==1:
            nombres=[nombres]
        else:
            nombres=[nombres+str(i) for i in range(A.cols)]
    elif (isinstance(nombres,list)) and (len(nombres)!=A.cols):
        raise ValueError('flechas(ax,A) o flechas(ax,A,n) y n="v" o  len(n)!=A.cols')
    elif not isinstance(nombres,list) and nombres!=None:
        raise ValueError('n es str o list')
        
    if A.rows==2:
        #v=A.col(0)
        #sumar=B.col(0)
        #ax.arrow(float(sumar[0]),float(sumar[1]),float(v[0]),float(v[1]),head_width=0.02,head_length=0.02, length_includes_head=True,**kwargs)
        #if nombre!='':
        #    ax.text(v[0]+sumar[0],v[1]+sumar[1],nombre,fontsize=fontsize)
        ax.quiver(B.row(0),B.row(1),A.row(0),A.row(1),**kwargs)
        if nombres!= None:
            for i in range(A.cols):
                ax.text(A.row(0)[i]+B.row(0)[i],A.row(1)[i]+B.row(1)[i],nombres[i],fontsize=fontsize)
        
    elif A.rows==3:
        #AT=A.T
        ax.quiver(B.row(0),B.row(1),B.row(2),A.row(0),A.row(1),A.row(2),**kwargs)
        if nombres!= None:
            for i in range(A.cols):
                ax.text(A.row(0)[i]+B.row(0)[i],A.row(1)[i]+B.row(1)[i],A.row(2)[i]+B.row(2)[i],nombres[i],fontsize=fontsize)
    else:
        raise ValueError('Sólo imprime matrices de 2 o 3 renglones')


def fun_cols_mat(f,A):
    B=f(A.col(0))
    for i in range(1,A.cols):
        B=B.row_join(f(A.col(i)))
    return B

def grafo(nodos,arcos,etiquetas=[],zoom=1,dx=1,dy=1,unid="",dist=100,radio=5,despl=20):
#nodos={nombre:(x,y,"dato bajo nodo"),}
#arcos=[("nombre",nodo1,nodo2),]
#etiquetas=[(x,y,"txt"),]
    def int2dist(num):
        return int2unid(num*dist)
    def int2unid(num):
        return '"'+str(num)+unid+'"'
    def i2u(num):
        return str(num)+unid
    def flecha(o1,o2,d1,d2):
        x1=0.9*(d1-o1)
        x2=0.9*(d2-o2)
        y12=(0.7*x1-0.7*x2)/10.0
        y21=(0.7*x1+0.7*x2)/10.0
        return '<polyline points="'+i2u(o1*dist)+','+i2u(o2*dist)+' '+i2u((o1+x1)*dist)+','+i2u((o2+x2)*dist)+' '+i2u((o1+x1-y12)*dist)+','+i2u((o2+x2-y21)*dist)+' '+   i2u((o1+x1-y21)*dist)+','+i2u((o2+x2+y12)*dist)+' '+ i2u((o1+x1)*dist)+','+i2u((o2+x2)*dist)+'" stroke="black" stroke-width="3"></polyline> '
    maxx=0
    maxy=0
    for nodo in nodos:
        maxx=max(maxx,nodos[nodo][0])
        maxy=max(maxy,nodos[nodo][1])
        
    svg='<svg width='+int2dist(maxx+dx)+' height='+int2dist(maxy+dy)+'>'
    for nodo in nodos:
        svg=svg+'<circle cx='+int2dist(nodos[nodo][0])+' cy='+int2dist(nodos[nodo][1])+' r='+int2unid(radio)+'></circle>'
        svg=svg+'<text x='+int2unid(nodos[nodo][0]*dist)+' y='+int2unid(nodos[nodo][1]*dist+despl)+'>'+nodos[nodo][2]+'</text>'
    for arco in arcos:
        svg=svg+flecha(nodos[arco[1]][0],nodos[arco[1]][1],nodos[arco[2]][0],nodos[arco[2]][1])
        svg=svg+'<text x='+int2unid((nodos[arco[1]][0]+nodos[arco[2]][0])/2*dist)+' y='+int2unid((nodos[arco[1]][1]+nodos[arco[2]][1])/2*dist+despl)+'>'+arco[0]+'</text>'
    for etiqueta in etiquetas:
        svg=svg+'<text x='+int2dist(etiqueta[0])+' y='+int2dist(etiqueta[1])+'>'+etiqueta[2]+'</text>'
    svg=svg+'</svg>'
    #print(svg)
    return IPython.display.SVG(data=svg)

def imprimir(*datos):
 salida=''
 for a in datos:
  if not(isinstance(a,str)):
    a=latex(a)
  salida=salida+'$'+a+'$'
 return IPython.display.Latex(salida)
 

def juntar(*columnas):#hacer encaramar o apilar para col_join
    A=columnas[0]
    for columna in columnas[1:]:
        A=A.row_join(columna)
    return A

def matList2listMat(A):#rellena ceros a la izq
#Convierte una matriz de listas en la lista de las matricas alineadas a derecha
#se usa con los coeficientes de los polinomios
    m=0
    for l in A:
        m=max(m,len(l))
    R=[]
    for k in range(m):
        coefi=lambda x:0 if (len(x)<=k) else x[len(x)-k-1]
        R.insert(0,A.applyfunc(coefi))
    return R
    
def mat(lista:str):#matrices str tipo matlab a sympy
#Genera una matriz de sympy a partir de una string estilo matlab, tener cuidado con '.' y '/'
        lista1=lista.split(';')
        #print('lista1')
        #print(lista1)
        lista2=list(map(lambda n: n.split(),lista1))
        lista3=list(map(lambda n: list(map(str2num,n)),lista2))
        return Matrix(lista3)
        #return lista3



def matriz_numer_denom(A):
#Factoriza el común denominador de las entradas de una matriz
    A=A.applyfunc(cancel)
    den=[]
    for a  in A:
        n,d=a.as_numer_denom()
        den.append(d)
    denom=monic(lcm(tuple(den)))
    B=(denom*A).applyfunc(cancel)
    return B,denom


    
def op_gauss(Amat,s):
#realiza una operacion entre renglones
    #if s=='nada':
    #    return Amat.ultop
    s=s.lower()
    #print(s)
    def interpretaRenglon(s1):
        s=s1.replace(' ','')
        #print("interpretando "+s)
        d=s.find("r")
        if d==-1:
            raise ValueError("fala la 'r'. Error en "+s)
        elif d==0:
            k=1
        else:
            try:
                k=str2num(s[:d])
            except ValueError as err:
                raise ValueError("antes de 'r' sOlo debe haber un entero. Error en "+s+'. '+str(err))
        #a1=s[d+1:]
        #if not a1.isdigit():
        #print ("coef ="+str(k))
        try:
            a=int(s[d+1:])#-1
        except ValueError as err:
            raise ValueError("despuEs de 'r' sOlo debe haber un dIgito. Error en "+s+'. '+str(err))
        #a=int(a1)
        return (k,a)
            
    #print (str(k)+", "+str(a))
    (size,z)=Amat.shape#size()
    m=eye(size)#matriz.identidad(size,size,"no_mostrar")
    d=s.find("<->")
    if d!=-1:
        (k1,a1)=interpretaRenglon(s[:d])
        (k2,a2)=interpretaRenglon(s[d+3:])
        if (k1 != 1) or (k2 != 1):
            raise ValueError("al intercambiar renglones no se puede multiplicar. Error en "+s)
        r="R"+str(a1)+" <-> R"+str(a2)
        m[a1,a1]=0    
        m[a2,a2]=0    
        m[a1,a2]=1    
        m[a2,a1]=1    
        #print(str(m))
    else:
        d=s.find("->")
        if d==-1:
            raise ValueError("no se encontrO ni '->' ni '<->'. Error en "+s)
        else:
            (k2,a2)=interpretaRenglon(s[d+2:])
            e=s[:d].find("+")
            f=s[:d].rfind("-")
            if e!=-1:
                (k11,a11)=interpretaRenglon(s[:e])
                (k12,a12)=interpretaRenglon(s[e+1:d])
                if (a11==a2) and (a12==a2):
                    raise ValueError("en este caso es mejor multiplicar el renglOn por "+str(k11+k12)+". Error en "+s)
                elif (a11==a2):
                    #if (k11!=1):
                        #raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                    r=str(k12)+"R"+str(a12)+"+"+str(k11)+"R"+str(a2)+" -> R"+str(a2)
                    m[a2,a12]=k12
                    m[a2,a11]=k11
                    #print(str(m))
                elif (a12==a2):
                    #if (k12!=1):
                        #raise ValueError("el renglOn destino no se multiplica por "+str(k12)+". Error en "+s)
                    r=str(k11)+"R"+str(a11)+"+"+str(k12)+"R"+str(a2)+" -> R"+str(a2)
                    m[a2,a11]=k11
                    m[a2,a12]=k12
                    #print(str(m))
                else:#if (a11!=a2) and (a12!=a2):
                    raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
            elif f!=-1:
                c=s[:d].count('r')
                if c==0:
                    raise ValueError("faltan 'R' en "+s[:d])
                elif c==2:
                    (k11,a11)=interpretaRenglon(s[:f])
                    (k12,a12)=interpretaRenglon(s[f+1:d])
                    if (a11==a2) and (a12==a2):
                        raise ValueError("en este caso es mejor multiplicar el renglOn. Error en "+s)
                    elif (a11==a2):
                        #if (k11!=1):
                            #raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                            
                        r=str(-k12)+"R"+str(a12)+"+"+str(k11)+"R"+str(a2)+" -> R"+str(a2)
                        m[a2,a12]=-k12
                        m[a2,a11]=k11
                        #print(str(m))
                    elif (a12==a2):
                        #if (k12!=1):
                            #raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                        r=str(-k11)+"R"+str(a11)+"+"+str(k12)+"R"+str(a2)+" -> R"+str(a2)
                        m[a2,a11]=-k11
                        m[a2,a12]=k12
                        #print(str(m))
#                        raise ValueError("el renglOn destino no se multiplica por "+str(-k12)+". Error en "+s)
                    else:#if (a11!=a2) and (a12!=a2):
                        raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
                elif c==1:
                    (k1,a1)=interpretaRenglon(s[:d])
                    if a1 != a2 :
                        raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
                    r=str(k1)+"R"+str(a1)+" -> R"+str(a2)
                    m[a2,a2]=k1
                    #print(str(m))
                
                else:
                    raise ValueError("se operan mAximo dos renglones. Error en "+s)
            else:
                (k1,a1)=interpretaRenglon(s[:d])
                if a1 != a2 :
                    raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
                r=str(k1)+"R"+str(a1)+" -> R"+str(a2)
                m[a2,a2]=k1
                #print(str(m))
    #print("La matriz elemental asociada es \n"+str(m))
    print(r)
    #print(m)
    return m*Amat
    #sympy.pprint(m*Amat)

def plot_mat(A,x0,y0,x1,y1):
    plt.figure()
    f, axes = plt.subplots(1, 1)
    axes.plot(A.T.col(0),A.T.col(1),'o-')
    axes.set_xlim(x0,x1)
    axes.set_ylim(y0,y1)
    plt.show()

def plot_mat2(A,B,x0,y0,x1,y1):
    plt.figure()
    f, axes = plt.subplots(1, 2)
    axes[0].plot(A.T.col(0),A.T.col(1),'o-')
    axes[0].set_xlim(x0,x1)
    axes[0].set_ylim(y0,y1)
    axes[1].plot(B.T.col(0),B.T.col(1),'o-')
    axes[1].set_xlim(x0,x1)
    axes[1].set_ylim(y0,y1)
    plt.show()
    
def row_op_gauss(A,i,j,k=0):
#si k=0, Ri <-> Rj
#si i=j, kRi -> Ri
#otros   kRi+Rj -> Rj
    r,c=A.shape
    E=eye(r)
    if k==0:
        E[i,i]=0
        E[j,j]=0
        E[i,j]=1
        E[j,i]=1        
    else:
        E[i,j]=k
    D=E*A
    #sympy.pprint(D)
    return D


def sonar(f1,framerate = 44100):
    from sympy.abc import t
    f1n = lambdify(t, f1, "numpy")
    tiempo = np.linspace(0,5,framerate*5)
    data = f1n(tiempo)
    return IPython.display.Audio(data,rate=framerate)
    
def str2num(s):#falta convertir / en Rational y usar luego eval. / por Clase que izq en num y der en den
               #falta que convierta las variables en símbolos
#convierte una string en un numero 
    if s.find('.')!=-1:
        return float(s)
    elif s.find('/')!=-1:
        return Rational(s)
    elif s.strip()=="-":
        return -1
    elif s.lstrip('+-').isdigit():
        return int(s)    
    else:
        return eval(s)
    
    