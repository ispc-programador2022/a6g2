from genrnd500 import genrnd

def media_genrnd500k():
    """Función que calcule la media del vector obtenido en genrnd500.

    Returns:
        int | float: Resultado final de la media del vector.
    """
        
    num_list = genrnd()
    media = sum(num_list) / len(num_list)
    
    return media


# Test
# print(media_genrnd500k())
