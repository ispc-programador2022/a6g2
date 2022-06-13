# Simulación de funciones necesarias de otros archivos:
# (Una vez creadas por los demás las importo)

# Resta entre 2 parametros
def resta(p1, p2):
    return p1 - p2

# Producto entre 2 parametros
def producto(p1, p2):
    return p1 * p2

# --------------------------------------

def p1(param1, param2, param3):
    """Función que resta los dos primeros parámetros "p1" y "p2" y los
       multipica por el parámetro "p3" usando las funciones externas "resta" y "producto".

    Args:
        p1 (float): Numero tipo float.
        p2 (float): Numero tipo float.
        p3 (float): Numero tipo float.

    Returns:
        float: Resultado final de las operaciones con redondeo a 2 decimales.
    """
    
    op_resta = resta(param1, param2)
    result = round(producto(op_resta, param3), 2)

    return result


# Test en consola de la función "p1"
# print("Test func_p1 01 (Resultado esperado: 74.64):", p1(12.4, 0.4, 6.22))
# print("Test func_p1 02 (Resultado esperado: 80):", p1(30, 10, 4))
# print("Test func_p1 03 (Resultado esperado: -32):", p1(2, 10, 4))
