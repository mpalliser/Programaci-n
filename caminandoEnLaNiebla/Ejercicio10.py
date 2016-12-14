# Mariano Palliser
# Pide dos numeros por pantalla, si uno de los dos o los dos son negativos imprimelo por pantalla mediante una alerta.
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

#Casos test
#primer_numero = 2
#segundo_numero = 2
#print ("La suma de los numeros es 4"

#primer_numero = 0 
#segundo_numero = 0
#print ("La suma de los numeros es 0"

#primer_numero = -1
#segundo_numero = 4
#print ("El primer numero es negativo")
#primer_numero = 5
#segundo_numero = -3
#print ("El segundo numero es negativo")
#primer_numero = -5
#segundo_numero = -3
#print ("Los dos numeros son negativos")