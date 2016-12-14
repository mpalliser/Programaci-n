#Mariano Palliser
#Lesson 3 ejercicios opcionales

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.


def checkNumerosEnRango(sudoku):
    rangoValores = len(sudoku)
    for fila in sudoku:
        for casilla in fila:
            if casilla not in range(1, rangoValores+1,1):
                return False

# Casos test
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]
print(checkNumerosEnRango(correcto))
# >>> True
incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [5, 4, 4, 4]]
print(checkNumerosEnRango(incorrecto1))
# >>> False
incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, -1],
               [3, 4, 1, 2]]
print(checkNumerosEnRango(incorrecto2))
# >>> False
incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 4],
               [4, 5, 2, 1, 3],
               [5, 4, 5, 2, 1],
               [5, 2, 4, 3, 2]]
print(checkNumerosEnRango(incorrecto3))
# >>> False
incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]
print(checkNumerosEnRango(incorrecto4))
# >>> False
incorrecto5 = [[1, 1.5],
               [1.5, 1]]
print(checkNumerosEnRango(incorrecto5))
# >>> False
incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]
print(checkNumerosEnRango(incorrecto6))
# >>> False