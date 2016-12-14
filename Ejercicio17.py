#Ejercicio 17
#Hecho por Mariano Palliser 
#Introduce dos numeros por teclado y sumalos si son pares o impares por separado.
num_1 = int (input("Introduce el primer numero: "))
num_2 = int (input("Introduce el primer numero: "))
if num_1%2==0 and num_2%2==0:
    suma_pares=num_1+num_2
    print("La suma de los pares es " + str(suma_pares))
elif num_1%2!=0 and num_2%2!=0: 
    suma_impares=num_1+num_2
    print("La suma de los impares es " + str(suma_impares))
else:
    print("Error")