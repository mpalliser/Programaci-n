# Programa que comprueba si un sudoku introducido por el usuario
# es correcto o no.
#
# Para ello deberá cumplir los siguientes requisitos:
#
# a) La Matriz dada es cuadrada
# b) La Matriz debe contener números Válidos:
#   · Los números han de ser enteros
#   · Tiene que haber tantos números como longuitud tenga la columna
#   · El número no puede ser más grande que la longuitud del sudoku
# d) No se pueden repetir números en cada fila
# e) No se pueden repetir números en cada columna

def check_sudoku(sudoku):
    if esCuadrado(sudoku) and checkNumerosValidos(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku):
        return True
    else:
        return False

def esCuadrado(sudoku):
    numeroFilas = len(sudoku)   
    for fila in sudoku:
        if len(fila) != numeroFilas:
            return False
    return True

def checkNumerosValidos(sudoku):
    rangoNumeros = range(1,len(sudoku)+1,1)
    for fila in sudoku:
        for casilla  in fila:
            if casilla not in rangoNumeros:
                return False	
    return True	

def checkFilas(sudoku):
    for filas in range(0,len(sudoku)):
        for elemento in range(0,len(sudoku)):
            if sudoku[filas].count(elemento+1) != 1:
                return False
    return True

def checkColumnas(sudoku):
    filaActual = 0
    columnaActual = 0
    while filaActual < len(sudoku) - 1:
    	for elemento in sudoku[filaActual]:
    		filaPorChequear = filaActual + 1
    		while filaPorChequear < len(sudoku):
    			if elemento == sudoku[filaPorChequear][columnaActual]:
    				return False
    			filaPorChequear = filaPorChequear + 1
    		columnaActual = columnaActual +1
    	filaActual = filaActual + 1
    	columnaActual = 0
    return True
	 
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]
incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]
incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]
incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]
incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]
incorrecto5 = [[1, 1.5],
               [1.5, 1]]
incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

# Casos test
print(check_sudoku(correcto))
# >>> True
print(check_sudoku(incorrecto1))
# >>> False
print(check_sudoku(incorrecto2))
# >>> False
print(check_sudoku(incorrecto3))
# >>> False
print(check_sudoku(incorrecto4))
# >>> False
print(check_sudoku(incorrecto5))
# >>> False
print(check_sudoku(incorrecto6))
# >>> False