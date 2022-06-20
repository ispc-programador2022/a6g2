#!/usr/bin/env python
# coding: utf-8

# In[99]:


import genrnd as gen
def fun_varianza(vector = gen.genrnd()):
    """
                               === Funcion de Calculo de Varianza de una problacion ===
    
     INPUT: La funcion tiene un parametro por defecto un vector con 50 datos obtenidos a partir de la funcion genrnd,
            la cual genera una lista con 50 valores enteros aleatorios.
    
    OUTPUT: Esta funcion devuelve (o retorna) la varianza luego de analizar el vector ingresado como parametro de la funcion. 
    
    """  
    # Calculo del Promedio:
    suma = 0
    sum_2 = 0
    for x in vector:
        suma += x
    promedio = suma/len(vector)
    # Calculo de la Varianza de una poblacion:
    for i in vector:
        sum_2 += (i-promedio)**2
    varianza = sum_2/len(vector)
    return varianza

