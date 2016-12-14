def esPalindromo(string):
    alreves = ""
    longitudString = len(string)
    contador = 1
    while len(alreves) < len(string):
        alreves = alreves + string[longitudString-contador]
        contador +=1
    if string == alreves:
        return True
    else:
        return False

print (esPalindromo("PalolaP"))