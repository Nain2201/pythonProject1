def buscar_valor(matriz, valor_a_buscar):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor_a_buscar:
                return True, fila, columna
    return False, None, None

# Definir una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 5  # Cambia este valor por el que desees buscar

encontrado, fila_encontrada, columna_encontrada = buscar_valor(matriz, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila_encontrada}, {columna_encontrada}).")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
