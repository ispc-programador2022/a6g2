#Se importan funciones de "producto" y "suma".
from producto import producto
from funcion_suma import suma

def produmastercer(param1, param2, param3):
  produ = producto(param1, param2) #Retorna el producto de "param1" y "param2", se almacena en "produ". 
  return suma(produ, param3) #Retorna la suma de "produ" y "param3".

#test
""" param1 = int(input("Parametro 1: "))
param2 = int(input("Parametro 2: "))
param3 = int(input("Parametro 3: "))

resultado = produmastercer(param1, param2, param3)
print(resultado) """