from genrnd import*

lista = genrnd()

def sumar (valores):
    for i in range (len(lista)):
        a = lista [i]
        for e in range (len(lista)):
            b = lista [e]
            suma = a+b
            print (suma)

sumar(lista)