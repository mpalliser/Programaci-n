valor_bruto = int (input("Introduce el valor bruto: "))
if valor_bruto <=20:
    print ("El precio final sera " + str(valor_bruto))
elif valor_bruto >20 and valor_bruto <=100:
    print ("EL precio final sera " + str(valor_bruto*0.95))
else:
    print ("El precio final sera " + str(valor_bruto*0.9))
