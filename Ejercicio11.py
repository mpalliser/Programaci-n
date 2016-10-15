numero_1 = int (input("Introduce el primer numero "))
numero_2 = int (input("Introduce el segundo numero "))
numero_3 = int (input("Introduce el tercer numero "))
if numero_1 + numero_2 == numero_3:
    print ("Se cumple que", numero_3 , "=" ,numero_2  , "+" , numero_1)
elif numero_2 + numero_3 == numero_1:
    print ("Se cumple que", numero_1 , "=" ,numero_2  , "+" , numero_3)
elif numero_3 + numero_1 == numero_2:
    print ("Se cumple que", numero_2 , "=" ,numero_3  , "+" , numero_1)
else:
    print ("Los numeros no cumplen la condicion")