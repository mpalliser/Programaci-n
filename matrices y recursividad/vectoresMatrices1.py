def verificarDNI(dni):
    """
    Verifica que los 8 primeros carácteres son numeros y el noveno es una letra
    """
    assert len(dni) == 9, "el DNI debe tener 9 caracteres"
    #chequeamos 8 primeros numeros
    for i in dni[:-1]:
        try:
            int(i)
        except ValueError:
            print("Los 8 primeros caracteres deben ser numeros")
    assert dni[-1].isalpha()==True, "El ultimo caracter debe ser una letra"
    #chequeamos letra




if __name__ == '__main__':
    #Casos test
    
    caso1 = "11111111A" #ok
    caso2 = "1111111AA" #falta un numero
    caso3 = "a"         #peta
    caso4 = "a11111111" #peta
    caso5 = []          #peta
    verificarDNI(caso5)
    #dniIntroducido = input("Introduce un DNI: ")
    #verificarDNI(dniIntroducido)
