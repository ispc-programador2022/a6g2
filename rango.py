"""
función genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.
23- función que calcule el rango del vector obtenido en genrnd.
"""
#mx es una variable que almacena el valor maximo de la lista
#mn es una variable que almacena el valor minimo de la lista

lista=[]

def rango(lista):
    mx=max(lista)
    mn=min(lista)
    
    return mx-mn


