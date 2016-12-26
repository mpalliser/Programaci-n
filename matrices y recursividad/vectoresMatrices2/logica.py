def obtenerLetraDni(numerosDni):
    """
    A partir de un numero de 8 digitos devuelve el numero y la letra de un DNI
    """
    try:
        isinstance(numerosDni, str)
        if not len(numerosDni) == 8:
            raise SyntaxError
    except SyntaxError:
        print ("El dni debe tener 8 digitos")
        return "dni no valido"
    except ValueError:
        print ("los 8 primeros digitos deben ser numeros")
        return "dni no valido"
    tablaAsignacion = {
        0:"t",1:"r", 2:"w", 3:"a", 4:"g", 5:"m", 
        6:"y", 7:"f", 8:"p", 9:"d", 10:"x", 11:"b", 
        12:"n", 13:"j", 14:"z", 15:"s", 16:"q", 17:"v",
        18:"h", 19:"l", 20:"c", 21:"k", 22:"e"}
    try:
        numerosDni = int(numerosDni)
    except ValueError:
        print ("los 8 primeros digitos deben ser numeros.")
        return "dni no valido"
    keyLetraDni = numerosDni % 23
    dni = str(numerosDni) + tablaAsignacion[keyLetraDni]
    return dni


