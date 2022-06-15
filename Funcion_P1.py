#9- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las
#funciones anteriores
from funcion_suma import funcion_suma
from producto import producto

def funcion_P1 (num1, num2, num3):

	suma  = funcion_suma(num1,num2)
	operacion = producto(suma)

return operacion