def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

# Definir una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

fila_a_ordenar = 1  # Cambia este valor para elegir la fila a ordenar (0, 1 o 2)

print("Matriz original:")
imprimir_matriz(matriz)

if 0 <= fila_a_ordenar < len(matriz):
    bubble_sort(matriz[fila_a_ordenar])
    print(f"Matriz con la fila {fila_a_ordenar} ordenada:")
    imprimir_matriz(matriz)
else:
    print(f"La fila {fila_a_ordenar} no existe en la matriz.")
