import string, random #Libreria letra random
import time #Libreria de tiempo
import pandas as pd #Libreria para dataframe


print("BIENVENIDX")
next = input("¿Estás listx para el juego? (Si/No): ")
#Condicional para iniciar el juego

if next.capitalize() == "No": 
  print (":c... entiendo, ¡nos vemos la proxima!")
  
if next.capitalize () == "Si":
  
#Reglas
  print ()
  print ('''Ahora te explico como funciona nuestro juego: 
  
1.De manera aleatoria te asignaremos una letra del abecedario, con esta deberas escribir una palabra de acuerdo con la categoria asignada.

2.Debes escribir una palabra con la letra dada, si te asignamos una letra en mayuscula, la palabra debe iniciar con esta misma, pero si es en minuscula, la palabra debe iniciar igual.
Ejemplo = C  -  Casa
v  -  vaca

3.Por cada acierto que tengas ganas 50 puntos, así mismo, por cada error que cometas perderás 50 puntos.

4.Puedes escoger las rondas que desees, para hacer la mayor cantidad de puntos, la mayor cantidad de puntos por ronda son 250.''')

  print()
  next2 = input("Presiona s para comenzar: ")
  if next2.lower() == "s":

#Iniciar cantidad de  partidas deseadas
    print()
    a = int(input("cuantas rondas quieres jugar:"))
    print()
    print ("¡¡Preparadx, comencemos!!")
    print()

    
    letraQueIngresan = []
    puntajeT = 0
    tiempo = 0
    listaDelistas = []
     
#Bucle para categorías   
    for i in range (a):
      lista = [] #Iniciar lista vacia
      letraRandom = random.choice(string.ascii_letters)
      print ('Tu letra es: ' + letraRandom)
      print()
      t1=time.time() #Iniciar contador de tiempo 
      
#Ciclo para categorias del juego, en el cual se evalua la palabra, se asigna un puntaje y un mendaje de acuerdo a este.      
      Ciudad = input("ingresa la Ciudad: ")
      if Ciudad[0] == letraRandom[0]:
        puntajeT = puntajeT + 50
        print('¡Sigue así!') 
      elif Ciudad[0] != letraRandom[0]:
        puntajeT = puntajeT - 50 
        print('ohhh que mal, ¡Sigue intentado!')
        print()
        print()
        
      Objeto = input("ingresa el Objeto: ")
      if Objeto[0] == letraRandom[0]:
        puntajeT = puntajeT + 50
        print('¡Sigue así!')   
      elif Objeto[0] != letraRandom[0]:
        puntajeT = puntajeT - 50 
        print('ohhh que mal, ¡Sigue intentado!')
        print()
        print()
        
      Animal = input("ingresa el Animal: ")
      if Animal[0] == letraRandom[0]:
        puntajeT = puntajeT + 50
        print('¡Sigue así!')  
      elif Animal[0] != letraRandom[0]:
        puntajeT = puntajeT - 50 
        print('ohhh que mal, ¡Sigue intentado!') 
        print()
        print()
        
      Color = input("ingresa el Color: ")
      if Color[0] == letraRandom[0]:
        puntajeT = puntajeT + 50
        print('¡Sigue así!')        
      elif Color[0] != letraRandom[0]:
        puntajeT = puntajeT - 50 
        print('ohhh que mal, ¡Sigue intentado!')
        print()
        print()
        
      Comida = input("ingresa la Comida: ")
      if Comida[0] == letraRandom[0]:
        puntajeT = puntajeT + 50
        print('¡Sigue así!')    
      elif Comida[0] != letraRandom[0]:
        puntajeT = puntajeT - 50 
        print('ohhh que mal, ¡Sigue intentado!')
        print()
        print()
#Cierre contador de tiempo       
      t2 = time.time()
      tiempo = t2 - t1  
#Abrir las listas para hacer tablas
      lista.append(Ciudad)
      lista.append(Objeto)
      lista.append(Animal)
      lista.append(Color)
      lista.append(Comida)
      lista.append(puntajeT)
      lista.append(tiempo)
      
       

      
      listaDelistas.append(lista)

#Calcular tiempo total     
      tiempoTotal = 0
      for i in range(a):
        tiempoTotal += tiempo

#Imprimir tabla
df = pd.DataFrame(listaDelistas, columns=['Ciudad', 'Objeto', 'Animal', 'Color', 'Comida', 'puntajeT', 'tiempo', ])
print(df)   

print()
print("Tu puntaje total es: ",puntajeT )
print("Tu tiempo total es: ",tiempoTotal ,"segundos" )

print()
print()
print("Gracias por jugar")