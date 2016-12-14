primer_numero = int (input("Introduce el primer numero "))
segundo_numero = int (input("Introduce el segundo numero "))
if primer_numero >=0 and segundo_numero >= 0:
    suma = primer_numero + segundo_numero
    print ("La suma de los numeros es " + str(suma))
else:
    print ("Alguno de los numeros no es positivo")