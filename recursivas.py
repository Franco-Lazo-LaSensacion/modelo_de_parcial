from input import *

# 1 -Realizar una función recursiva que calcule la suma de los primeros números naturales:

# n = get_int("", "E", 1, 10, 2)

# def sumar_naturales(numero: int) -> int:
    
     # if numero == 1:
          # return 1
     # else:
          # return numero + sumar_naturales(numero - 1)

# print(sumar_naturales(n))

#2 -Realizar una función recursiva que calcule la potencia de un número:

# base = get_int("", "E", 1, 100, 2)
# exponente = get_int("", "E", 1, 100, 2)

# def calcular_potencia(base: int, exponente: int) -> int:
     
     # if exponente == 0:
          # return 1
     # else:
          # return base * calcular_potencia(base, (exponente - 1))
     
# print("La potencia es", calcular_potencia(base, exponente))

#3 -Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

# n = get_int("", "E", 1, 1000, 2)

# def sumar_digitos(numero: int) -> int:
    
#     if numero < 10:
     #    return numero
#     else:
     #    return sumar_digitos(numero // 10) + numero % 10

# print(sumar_digitos(n))  

#4 -Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.
#{0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597...}

# numero = get_int("", "E", 1, 10, 1)

# def calcular_fibonacci(numero: int) -> int:
    
#     if numero < 2:
     #    return numero
    
#     return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

# for i in range(numero):
     # print(calcular_fibonacci(i))

# print(calcular_fibonacci(numero))

