'''                        UNIVERSIDAD DE CUENCA        '''
'''Integrantes: 
                Astudillo Palacio Bernardo Josue
                Chimbo V�lez Edgar Fernando
                Guncay Carchipulla Valeria Paola 
                Pe�aranda Criollo Myriam Viviana
                
             
    '''
    
#Importaci�n de las librerias apropiadas
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
#Valores iniciales de las variables (b) y (k)
valorb=0 
valork=0
#Bucle para el intervalo que se dar� a (b)
n=0 
while n<1:  
   b=float(input("Elegir el valor de b (1-4]: "))
   print("POR DEFECTO--Los valores de K van a variar de [0-1]")
   if b>1 and b <=4:
       n+=1
#Funci�n que contiene las condiciones inciales  as� como las ecuaciones iniciales
def ode(x,t):
    """
    Evaluaci�n de las ecuaciones diferenciales

    Parameters
    ----------
    x : vector
        x = evaluaci�n de los resultados ODE
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
    #Asignaci�n del elemento vectorial a cada elemento de la ecuaci�n diferencial
    s=x[0] #primer elemento de x
    i=x[1] #segundo elemento de x
    #Ecuaciones diferenciales en funci�n del tiempo
    dsdt=-b*s*i
    didt=b*s*i-k*i
    drdt=k*i
    return [dsdt, didt, drdt]
#Condiciones inciales para cada una de las funciones s(t),i(t) y r(t) que se graficar� y resolver�
x0 = [1, 1.23e-6, 0]

#Establecemos la gr�fica
fig=plt.figure()     #objeto figura 
camera = Camera(fig) #determinaci�n de la animaci�n
ax=fig.subplots()  
lstb=list(np.arange(0,b,b*0.01))     #evaluaci�n de los valores de b
lstb = [ round(i, 3) for i in lstb ] #redondeo de los valores de b

#Evaluci�n de los valores a variar de (b)
for i in range(len(lstb)):
    valorb=lstb[i]            #valores de b
    valork=i/100              #valores de k
    t = np.arange(0,140,0.5)  #Declaramos el arreglo de tiempo[D�as]
    
    x = odeint(ode,x0,t)      #Evaluamos los resultados de la funci�n ODE en cada punto de tiempo. 
    '''odeint: resuleve el problema de valor incial para ODAs de primer orden.
       ode: funci�n de las ecuaciones diferenciales 
       x0=Es una matriz (o lista) de valores inciales
       t= Serie de puntos de tiempo en los que desea obtener una soluci�n al problema 
    '''
#Utilizamos la notacion de dos puntos (:) para acceder a todas las filas como primer �ndice, 
#..como segundo �ndice indicamos la columna a obtener.
    s = x[:,0]                #Funci�n (1) de los Susceptibles
    i = x[:,1]                #Funci�n (2) de los Infectados
    r = x[:,2]                #Funci�n (3) de los Recuperados
  
    ##gr�ficaci�n de la Funci�n (1), (2), (3)
    ax.plot(t,s,color="blue",label="Susceptibles",ls="solid")            
    ax.plot(t,i,color="red",label="Infectados",ls="dashed")             
    ax.plot(t,r,color="green",label="Recuperados",ls="dashdot")   
      
    #Cuadro de texto para los valores(variados) de (b) y (k)
    plt.text(120, 0.70, "b = "+ str(valorb), fontsize=15, color="black")        
    plt.text(120, 0.60, "k = "+ str(valork), fontsize=15, color="black")
    plt.legend(["Susceptibles" ,"Infectados","Recuperados"],loc = 'upper right')
    camera.snap()  
#T�tulos de los ejes x e y    
plt.xlabel("Tiempo[D�as]")           
plt.ylabel("Poblaci�n[Proporci�n] ") 

#T�tulo principal de la gr�fica
plt.title("Modelo SIR Cuenca",fontdict = {'family': 'serif', 
        'color' : 'teal',
        'weight': 'bold',
        'size': 15})

plt.grid() #representaci�n de cuadr�cula
animation = camera.animate() #delimitaci�n del objeto animaci�n

#Formato del archivo a guardar tipo gif
animation.save('celluloid_legends.gif', writer = 'imagemagick')
plt.show()
