#Ejercicio 16
#Hecho por Mariano Palliser 
#Escribe un programa que escriba en pantalla los 30 primeros números naturales, así como su media aritmética.
numeroInicial = 1
numeroFinal = 30
lista = []

while(numeroInicial<=numeroFinal):
    lista.append(numeroInicial)
    numeroInicial += 1
media = len(lista)
print("La media es " + str(sum(lista)/media))

#Casos Test
#Test 1
# 30 primeros numeros
# media 15.5

#Test 2
# 100 primeros numeros
#media 50,5