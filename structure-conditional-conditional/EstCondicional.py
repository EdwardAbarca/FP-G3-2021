def estCondicional01():
  #Definir variables y otros 
  print("Ejemplo estructura Condicional en Python") 
  montoP=0 
  #Datos de entrada 
  cantidadX=int(input("Ingrese la cantidad de lapices:")) 
  #Proceso 
  if cantidadX>=1000: 
    montoP=cantidadX*0.80
  else: 
    montoP=cantidadX*0.90
  #Datos de salida 
  print("El monto a pagar es:", montoP) 
def estCondicional02():
  #Definir variables
  print("Ejercicio 02 EstCondicional")
  #Datos de entrada
  montoP=0
  cantidadx=int(input("Ingrese la cantidad de platos: "))
  #Proceso
  if cantidadx<200:
    montoP=cantidadx*95
  elif cantidadx>200 and cantidadx<=300:
    montoP=cantidadx*85
  else:
    montoP=cantidadx*75
  #Datos de salida
  print("La cantidad a pagar es: ", montoP)
#estCondicional01()
estCondicional02()