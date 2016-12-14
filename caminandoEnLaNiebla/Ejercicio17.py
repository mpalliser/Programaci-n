#Ejercicio 17
#Hecho por Mariano Palliser 
#Introduce dos numeros por teclado y suma los numeros comprendidos separando pares e impares:

numeroInicial = int (input("Introduce el primer numero: "))
numeroFinal = int (input("Introduce el segundo numero: "))

totalPar = 0
totalImpar = 0
rangoNumeros = list(range(numeroInicial, numeroFinal+1))
for numero in rangoNumeros:
    if numero %2==0:
        totalPar = totalPar + numero
    else:
        totalImpar = totalImpar + numero

print ("Total de numeros impares: " + str(totalImpar) + ", Total numeros pares: " + str(totalPar))

#Test 1
#primerNumero: 2
#segundoNumero: 4
#totalPar: 2+4+6 = 12
#totalImpar: 3+5= 8

#Test 2
#primerNumero : 0
#segundoNumero : 10
#totalPar : 2+4+6+8+10 = 30
#totalImpar: 1+3+5+7+9= 25