import random as r
def genrnd():
    """retorna una lista con 50 números aleatorios. [0-100]
    """
    my_list= []
 
    for i in range (50):
        my_list.append( r.randint (0,100))
   
    return my_list