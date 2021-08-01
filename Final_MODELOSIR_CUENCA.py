'''                        UNIVERSIDAD DE CUENCA        '''
'''Integrantes: 
                Astudillo Palacio Bernardo Josue
                Chimbo Vélez Edgar Fernando
                Guncay Carchipulla Valeria Paola 
                Peñaranda Criollo Myriam Viviana
                
             
    '''
    
#Importación de las librerias apropiadas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
#Valores iniciales de las variables (b) y (k)
valorb=0 
valork=0
#Bucle para el intervalo que se dará a (b)
n=0 
while n<1:  
   b=float(input("Elegir el valor de b (1-4]: "))
   print("POR DEFECTO--Los valores de K van a variar de [0-1]")
   if b>1 and b <=4:
       n+=1
#Función que contiene las condiciones inciales  así como las ecuaciones iniciales
def ode(x,t):
    """
    Evaluación de las ecuaciones diferenciales

    Parameters
    ----------
    x : vector
        x = evaluación de los resultados ODE
    t : int
        t = representa datos del tiempo.

    Returns
    -------
    list
        Devuelve las ecuaciones diferenciales.

    """
    b=valorb
    k=valork
    #Constantes asociadas a las ecuaciones inciales
    N=810000
    I=1
    S=N-I
    s=S/N
    i=I/N
    #Asignación del elemento vectorial a cada elemento de la ecuación diferencial
    s=x[0] #primer elemento de x
    i=x[1] #segundo elemento de x
    #Ecuaciones diferenciales en función del tiempo
    dsdt=-b*s*i
    didt=b*s*i-k*i
    drdt=k*i
    return [dsdt, didt, drdt]
#Condiciones inciales para cada una de las funciones s(t),i(t) y r(t) que se graficará y resolverá
x0 = [1, 1.23e-6, 0]

#Establecemos la gráfica
fig=plt.figure()     #objeto figura 
camera = Camera(fig) #determinación de la animación
ax=fig.subplots()  
lstb=list(np.arange(0,b,b*0.01))     #evaluación de los valores de b
lstb = [ round(i, 3) for i in lstb ] #redondeo de los valores de b

#Evalución de los valores a variar de (b)
for i in range(len(lstb)):
    valorb=lstb[i]            #valores de b
    valork=i/100              #valores de k
    t = np.arange(0,140,0.5)  #Declaramos el arreglo de tiempo[Días]
    
    x = odeint(ode,x0,t)      #Evaluamos los resultados de la función ODE en cada punto de tiempo. 
    '''odeint: resuleve el problema de valor incial para ODAs de primer orden.
       ode: función de las ecuaciones diferenciales 
       x0=Es una matriz (o lista) de valores inciales
       t= Serie de puntos de tiempo en los que desea obtener una solución al problema 
    '''
#Utilizamos la notacion de dos puntos (:) para acceder a todas las filas como primer índice, 
#..como segundo índice indicamos la columna a obtener.
    s = x[:,0]                #Función (1) de los Susceptibles
    i = x[:,1]                #Función (2) de los Infectados
    r = x[:,2]                #Función (3) de los Recuperados
  
    ##gráficación de la Función (1), (2), (3)
    ax.plot(t,s,color="blue",label="Susceptibles",ls="solid")            
    ax.plot(t,i,color="red",label="Infectados",ls="dashed")             
    ax.plot(t,r,color="green",label="Recuperados",ls="dashdot")   
      
    #Cuadro de texto para los valores(variados) de (b) y (k)
    plt.text(120, 0.70, "b = "+ str(valorb), fontsize=15, color="black")        
    plt.text(120, 0.60, "k = "+ str(valork), fontsize=15, color="black")
    plt.legend(["Susceptibles" ,"Infectados","Recuperados"],loc = 'upper right')
    camera.snap()  
#Títulos de los ejes x e y    
plt.xlabel("Tiempo[Días]")           
plt.ylabel("Población[Proporción] ") 

#Título principal de la gráfica
plt.title("Modelo SIR Cuenca",fontdict = {'family': 'serif', 
        'color' : 'teal',
        'weight': 'bold',
        'size': 15})

plt.grid() #representación de cuadrícula
animation = camera.animate() #delimitación del objeto animación

#Formato del archivo a guardar tipo gif
animation.save('celluloid_legends.gif', writer = 'imagemagick')
plt.show()
