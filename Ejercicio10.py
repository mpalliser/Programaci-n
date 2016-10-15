primer_numero = int (input("Introduce el primer numero "))
segundo_numero = int (input("Introduce el segundo numero "))
if primer_numero >=0 and segundo_numero >= 0:
    suma = primer_numero + segundo_numero
    print ("La suma de los numeros es " + str(suma))
elif primer_numero <=0 and segundo_numero >=0:
    print ("El primer numero es negativo")
elif primer_numero >=0 and segundo_numero <=0:
    print ("El segundo numero es negativo")
else:
    print ("Los dos numeros son negativos")
