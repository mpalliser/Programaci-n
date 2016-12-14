primer_numero = int (input("Introduce el primer numero"))
segundo_numero = int (input("Introduce el segundo numero"))
if primer_numero > segundo_numero:
    print ("El primer numero" , primer_numero ,"Es mayor que", segundo_numero)
elif primer_numero == segundo_numero:
    print ("Los numeros son iguales", primer_numero)
else:
    print ("El primer numero", primer_numero , "Es menor que el segundo numero", segundo_numero)