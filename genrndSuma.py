import random as r
def genrnd ():
    my_list= []
 
    for i in range (50):
        my_list.append( r.randint (0,100))
   
    return my_list + r