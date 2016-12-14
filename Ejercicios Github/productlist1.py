# Mariano Palliser
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(lista):
    resultado = 1
    for elemento in lista:
        resultado = elemento * resultado
    return resultado




#Caso test 1:
print (product_list([9]))
#>>> 9
#Caso test 2:
print (product_list([1,2,3,4]))
#>>> 24
#Caso test 3:
print (product_list([]))
#>>> 1