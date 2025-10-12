# -1 Desarrollar una función que permita crear un array de números 
# con la cantidad de elementos que establezca el parámetro recibido.

import random

# def crear_array(cantidad_de_elementos: int) -> list:

#     '''
#     Esta funcion crea un array de numeros con la cantidad de elementos que quiera el usuario

#     Pide un entero

#     Retorna un entero

#     '''
#     array = [False] * cantidad_de_elementos

#     return array

# print(crear_array(10))

# 2 - Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  
# Crear el array con la función del punto 1.

# def crear_array_v2(cantidad_de_elementos: int) -> list:
    
#     '''
#     Crea un array con la cantidad de elementos recibidos por parametro

#     Recibe un entero

#     Retorna un entero
#     '''

#     return crear_array((cantidad_de_elementos))

# print(crear_array_v2(10))

# 3- Escribir una función que reciba una lista de enteros, la misma calculará y 
# devolverá el promedio de todos los números. 

# def calcular_promedio(lista: list) -> float:

#     """
#     Calcula y devuelve el promedio de una lista de enteros.
#     """

#     if len(lista) == 0:
#         return 0 

#     acumulador = 0

#     for numero in lista:

#        acumulador += numero
        

#     return acumulador / len(lista)

# numeros = [5, 10, 15, 3, -10]

# print(f"El promedio es: {calcular_promedio(numeros)}")

# 4- Escribir una función parecida a la anterior, 
# pero la misma deberá calcular y devolver el promedio de los números positivos.


# def calcular_promedio_positivos(lista: list) -> float:

#     """
#     Calcula y devuelve el promedio de una lista de solo positivos.
#     """

#     if len(lista) == 0:
#         return 0 

#     acumulador = 0
#     contador = 0
#     for numero in lista:

#         if numero > 0:
#             acumulador += numero
#             contador += 1

#     return acumulador / contador

# numeros = [5, 10, 15, 3, -10, -5]

# print(f"El promedio es: {calcular_promedio_positivos(numeros)}")

# 5-Escribir una función que calcule y retorne el producto de 
# todos los elementos de la lista que recibe como parámetro.

# def calcular_producto(lista: list) -> int:

#     """
#     Calcula y devuelve el producto de los elementos recibidos.
#     """

#     if len(lista) == 0:
#         return 0 

#     producto = 1

#     for i in lista:

#         producto = producto * i

#     return producto

# numeros = [5, 3, 21, -1]

# print(f"El producto es: {calcular_producto(numeros)}")

#6 -Escribir una función que reciba como parámetros una lista de enteros y 
# retorne la posición del valor máximo encontrado.

# def buscar_maximo(lista1: list) -> int:
#     '''
#     Busca el maximo entre una lista de enteros

#     Recibe una lista

#     Retorna la posicion del maximo
    
#     '''

#     if len(lista1) == 0:
#         return 0 
    
#     maximo = lista1[0]
#     posicion_maximo = 0

#     for i in range(1, len(lista1)):

#         if lista1[i] > maximo:
#             maximo = lista1[i]
#             posicion_maximo = i
        

#     return posicion_maximo


#7 -Escribir una función que reciba como parámetros una lista de enteros 
# y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

# def buscar_maximos(lista: list) -> int:

#     '''
#     Busca el/los maximos

#     Recibe una lista

#     Retorna las posiciones
    
#     '''

#     if len(lista) == 0:
#         return 0 
    
#     maximo = lista[0]
#     posicion_maximo = [0]

#     for i in range(1, len(lista)):

#         if lista[i] > maximo:
#             maximo = lista[i]
#             posicion_maximo = i
#         elif lista[i] == maximo:
#             posicion_maximo = posicion_maximo + [i]

#     return posicion_maximo
   
# lista1 = [6, 4, 2, 5, 6]

# 8 - Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
# Una lista de nombres (lista_nombres).
# Un nombre a buscar en la lista (nombre_antiguo).
# Un nombre de reemplazo (nombre_nuevo).
# La función debe realizar las siguientes acciones:
# Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
# Retornar la cantidad total de reemplazos realizados.

# nombres = ["Pedro", "Daniel", "Tamara", "Lucas", "Carlos", "Pedro", "Romina", "Adrian"]

# def reemplazar_nombres(lista_nombres: list, nombre_antiguo: str, nombre_nuevo: str) -> int:

#     '''
#     Reemplaza el nombre antiguo por el nuevo

#     Recibe un nombre antiguo a reemplazar

#     Retorna la cantidad de reemplazos realizados
#     '''

#     contador = 0

#     for i in range(len(lista_nombres)): #Dejo que haga todas las iteraciones por si el nombre se repite.

#         if nombre_antiguo == lista_nombres[i]:
#             lista_nombres[i] = nombre_nuevo
#             contador += 1

#     return contador


# print("Se realizaron:", reemplazar_nombres(nombres, "Pedro", "Ramon"), "reemplazo/s.")

# 9- Crear una función que reciba como parámetros dos arrays. 
# La función deberá mostrar la intersección de los dos arrays.

# def mostrar_interseccion(lista: list, lista2: list) -> list:

#     '''
#     Cálcula la intersección entre dos arrays

#     Recibe dos arrays

#     Retorna la intersección en forma de lista
#     '''

#     if len(lista) < len(lista2):
#         cantidad_retorno = len(lista)
#     else:
#         cantidad_retorno = len(lista2)

#     interseccion = [False] * cantidad_retorno

#     z = 0

#     for i in range(len(lista)):

#         for j in range(len(lista2)):            

#             if lista[i] == lista2[j]:
#                 interseccion[z] = lista[i]
            
#                 z += 1
#                 break
            
#     return interseccion

# print(mostrar_interseccion([1, 4, "Pedro", 4], [2, 3, "Pedro", 5]))

#10 -Crear una función que reciba como parámetros dos arrays. 
# La función deberá mostrar la unión de los dos arrays.


# def calcular_union(array_1: list,
#                               array_2: list) -> list:
    
#     '''
#     Calcula la union entre dos arrays

#     Recibe dos arrays

#     Retorna una lista nueva
#     '''
#     cantidad = len(array_1) + len(array_2)

#     lista_retorno = [False] * cantidad

#     z = 0

#     for i in range(len(array_1)):
#         lista_retorno[z] = array_1[i]
#         z += 1

#     for i in range(len(array_2)):

#         bandera = False

#         for j in range(len(array_1)):

#             if array_1[j] == array_2[i]:
#                 bandera = True
#                 break
        
#         if bandera == False:
#             lista_retorno[z] = array_2[i]
#             z += 1

#     return lista_retorno

# print(calcular_union([1, 4, "Pedro", 4, 7], [2, 3, "Pedro", 5]))

#11 -Crear una función que reciba como parámetros dos arrays. 
# La función deberá mostrar la diferencia de los dos arrays.

# def calcular_diferencia(array_1: list,
#                         array_2: list) -> list:
    
#     '''
#     Calcula la diferencia entre dos arrays

#     Recibe dos arrays

#     Retorna una lista nueva
#     '''

#     diferencia = [False] * len(array_1)

#     z = 0

#     for i in range(len(array_1)):

#         bandera = True

#         for j in range(len(array_2)):

#             if array_1[i] == array_2[j]:
#                 bandera = False
#                 break
            
#         if bandera == True:
#             diferencia[z] = array_1[i]
#             z += 1

#     return diferencia


# print(calcular_diferencia([1, 2, 3, 4, 5], [2, 3, 4, 5]))
