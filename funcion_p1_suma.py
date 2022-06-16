#9- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las
#funciones anteriores
from suma import suma
from producto import producto

def funcion_p1_suma (num1, num2, num3):

	suma  = suma(num1,num2)
	operacion = producto(suma, num3)

	return operacion