primer_numero = int (input("Introduce el primer numero "))
segundo_numero = int (input("Introduce el segundo numero "))
if primer_numero%2 ==0 and segundo_numero%2 ==0 and primer_numero <=50 and segundo_numero >99 and segundo_numero <=501 :
    suma = primer_numero + segundo_numero
    print (suma)
else:
    print ("Error")
    
