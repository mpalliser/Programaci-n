# Mariano Palliser.
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(lista):

    if lista == []:
        return 0
    else:
        resultado = lista[0]
        for elemento in lista:
            if resultado < elemento:
                resultado = elemento
    return resultado


print (greatest([4,23,1]))
#>>> 23
print (greatest([]))
#>>> 0
print (greatest([1,12,45,20])) 
# Devuelve 45