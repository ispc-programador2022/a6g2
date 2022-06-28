import random

def genrnd():
    """Genara una lista con 500000 valores enteros 
    Returns:
        list
    """
    num_rand = []
    for i in range(500000):
        num_rand.append(round(random.uniform(0,100)))
    return num_rand
