matriz1 = [[3, 8], 
           [4, 6]]

matriz2 = [[4, 0], 
            [1, -9]]

matriz3 = [[2, 1], 
           [9, -2]]

matriz4 = [[1, 2], 
            [1, -2]]

matriz5 = [[63, 6, 4], 
           [8, 2, 2]]

matriz6 = [[5, 7, 2], 
            [2, -6, 2]]



def verificar_filas(lista1: list) -> int:

    cantidad_fila = 0
    for i in range(len(lista1)):
        cantidad_fila += 1

    return cantidad_fila

def verificar_columnas(lista1: list) -> int:

    cantidad_columnas = 0
    for i in range(len(lista1)):
        cantidad_columnas += 1
    
    return cantidad_columnas

def inicializar_matriz(n_filas: int,
                       p_columnas: int,
                       valor_por_defecto : any = False)->list:
    '''
    '''

    matriz = []

    for _ in range(n_filas):
        fila = [valor_por_defecto] * p_columnas

        matriz += [fila]

    return matriz

def sumar_matrices(lista1: list, lista2: list) -> list:

    '''
    '''

    if verificar_filas(lista1) == verificar_filas(lista2) and verificar_columnas(lista1) == verificar_columnas(lista2):

        print("Matrices iguales, se realiza la suma.")

        matriz_suma = inicializar_matriz(verificar_filas(matriz1), verificar_columnas(matriz1))

        for i in range(len(lista1)):
                
                for j in range(len(lista1[i])):
                     matriz_suma[i][j] = lista1[i][j] + lista2[i][j]

        return matriz_suma

    else:
        print("Matrices no son iguales, no se puede sumar.")

print(sumar_matrices(matriz5, matriz6))