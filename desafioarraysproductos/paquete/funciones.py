#dimension = int(input("Ingrese el total de productos adquiridos: ")) # ppara el main

def cargar_productos(dimension: int) -> list:
    '''
    Carga secuencialmente productos en un array

    Retorna un array
    '''
    array = ["Text"] * dimension

    for i in range(len(array)):

        producto = str(input("Ingrese el producto adquirido: "))
        array[i] = producto

    return array


def buscar_interseccion(lista1: list, lista2: list) -> str:

    '''
    Busca la interseccion entre dos listas, es decir, lo que comparten ambas

    Recibe dos listas

    Retorna un mensaje
    '''

    lista_retorno = []

    for i in range(len(lista1)):

        for j in range(len(lista2)):

            if lista1[i] == lista2[j]:
                lista_retorno += [lista1[i]]
                break

    mensaje = f"Los productos que han comprado ambos usuarios son: {lista_retorno}"

    return mensaje

#print(buscar_interseccion(["Pan", "Sonrisas", "Queso"], 
                          #["Lechuga", "Pan", "Queso", "Papas"]))

def buscar_diferencia(lista1: list, lista2: list) -> str:

    '''
    Busca la diferencia entre dos listas, es decir, lo que esta en uno que no esta en otro

    Recibe dos listas

    Retorna un mensaje
    
    '''

    #setear limite por que da error de indexacion cuando hay una lista mas chica en elementos para comparar
    
    no_adquirido = []

    for i in range(len(lista2)):
        
        if lista2[i] != lista1[i]:
            no_adquirido += [lista1[i]]

    mensaje = f"El primer cliente compro: {lista1}, el segundo cliente no adquirio: {no_adquirido}"

    return mensaje

print(buscar_diferencia(["Pan", "Sonrisas", "Queso"], 
                          ["Lechuga", "Pan", "Queso", "Papas"]))