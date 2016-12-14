#Ejercicio 16
#Hecho por Mariano Palliser
#Escribe un programa que visualize los n-primeros multiplos de 2, siendo un valor leido por teclado.
def rangoNumeros(numeroIntroducido):
    lista = range(1,(numeroIntroducido*numeroIntroducido),1)
    nMultiplos = []
    if numeroIntroducido == 0 or numeroIntroducido ==1:
        print (0)
    elif numeroIntroducido == 2:
        print([2, 4])
    else:
        for numero in lista:
            if numero %2==0 and len(nMultiplos)<numeroIntroducido:
                nMultiplos.append(numero)
            elif len(nMultiplos)==numeroIntroducido:
                return print (nMultiplos)


rangoNumeros(int(input("Introduce un numero: ")))