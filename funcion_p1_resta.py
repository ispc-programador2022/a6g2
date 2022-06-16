from resta import resta
from producto import producto

def funcion_p1_resta(param1, param2, param3):
    """Función que resta los dos primeros parámetros "p1" y "p2" y los
       multipica por el parámetro "p3" usando las funciones externas "resta" y "producto".
    Args:
        p1 (int | float)
        p2 (int | float)
        p3 (int | float)
    Returns:
        int | float: Resultado final de las operaciones con redondeo de 2 decimales.
    """
    
    op_resta = resta(param1, param2)
    result = producto(op_resta, param3)
    return result


# Test en consola de la función "p1"
# print("Test func_p1 01 (Resultado esperado: 74.64):", p1(12.4, 0.4, 6.22))
# print("Test func_p1 02 (Resultado esperado: 80):", p1(30, 10, 4))
# print("Test func_p1 03 (Resultado esperado: -32):", p1(2, 10, 4))
