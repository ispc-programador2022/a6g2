from genrnd import*

lista = genrnd()

def rango():
    valor_max = None
    valor_min = None
    
    for num in lista:
        if (valor_max is None or num > valor_max):
            valor_max = num
    
        if (valor_min is None or num < valor_min):
            valor_min = num

    rango_Mm = valor_max - valor_min
    print('El rango de la lista es: ',rango_Mm)
    return