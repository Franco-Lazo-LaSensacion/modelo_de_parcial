# 1 -Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

# def get_number():
    # '''
    # pedir un número

    # devolver el mismo
    # '''
    # number = input("Ingrese un número: ")
    # number = int(number)

    # return number

# 2 -Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def get_float():
    # '''
    # pedir un número flotante

    # devolver el mismo
    # '''
    # number = input("Ingrese un número: ")
    # number = float(number)

    # return number

# 3 -Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

# def get_text():
    # '''
    # pedir un texto

    # devolverlo
    # '''
    # texto = input("Ingrese una cadena de texto: ")
    # texto = str(texto)

    # return texto

# 4 -Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

# def calcular_area():
    # '''
    # pedir base y altura de un rectangulo

    # devolver el area
    # '''
    # base = input("Ingrese base del rectángulo: ")
    # base = float(base)

    # altura = input("Ingrese altura del rectángulo: ")
    # altura = float(altura)

    
    # resultado = base * altura

    # return resultado

# print("el área es:", calcular_area())

# 5 -Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# def calcular_area():
#   '''
#   pedir base y altura de un circulo

#   devolver el area
#   '''
#   radio = input("Ingrese radio del círculo: ")
#   radio = float(radio)

#   resultado = (radio ** 2) * 3.14159

#   return resultado

# print("el área es:", calcular_area())

# 6 -Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

# def chequear_numero() -> str:

    # '''
    # Detecta si un número es par o impar

    # Recibe un número

    # Devuelve un string
    # '''

    # number = input("Ingrese un número: ")
    # number = int(number)

    # if number % 2 == 0:
        # estado: str = "Par"
        # print(f"El {number} es {estado}.")

    # else:
        # estado: str = "Impar"
        # print(f"El {number} es {estado}.")

    # return estado

# chequear_numero()

# 7 -Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

# def chequear_numero() -> bool:
#   '''
#   Detecta si un número es par o impar

#   Recibe un número

#   Devuelve un string
#   '''
#   number = input("Ingrese un número para saber si es par o impar: ")
#   number = int(number)

#   if number % 2 == 0:
    #   estado: bool = True
    #   print(f"{estado}.")
#   else:
    #   estado: bool = False
    #   print(f"{estado}")

#   return estado

# chequear_numero()

# 8 -Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# def buscar_maximo(n1: int, n2: int, n3: int) -> int:

    # '''
    # busca el maximo de tres numeros

    # recibe 3 enteros

    # devuelve 1 entero
    
    # '''
    # if n1 > n2 and n1 > n3:
        # return n1
    # elif n2 > n1 and n2 > n3:
        # return n2
    # else:
        # return n3    
    
# 9 -Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# def calcular_potencia(base: int, exponente: int) -> int:

    # return base ** exponente

# 10 -Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

# def get_number(n1: int) -> int:
    
    # for i in range(2, n1):
        # if (n1 % i) == 0:
            # return False
        # else:
            # return True
        
# print(get_number(4))

# 11 -Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
# muestre todos los números primos comprendidos entre la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

# def buscar_primos(n: int) -> int:
    # '''
    # Retorna la cantidad de números primos encontrados.

    # Pide un entero por función modularizada.

    # Devuelve un entero.
    # '''
    # counter = 0
    
    # for i in range(1, n):

        # numero_primo = True
        # limite = (i // 2) + 1

        # for j in range(2, limite):
            # if (i % j) == 0:
                # numero_primo = False
                # break
    
        # if numero_primo == True:
            # print(i)
            # counter += 1
    
    # print(f"son {counter} números primos encontrados" 
        #   + " entre la unidad y el ingresado")

    # return i

# buscar_primos(5)

# 12 -Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. 
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. 
# Por defecto es del 1 al 10.

# def tabla_multiplicar (num_ingresado:int ) -> int:
#     '''
#     Esta funcion es una tabla de multiplicar.
#     De base el multiplicador es 10, pero si el usuario
#     desea, puede modificar el mismo.
#     '''
#     if modificar == "S" or modificar == "s":
#         multiplicando_modif = int(input("Pone la cantidad de veces que queres multiplicar tu numero (el multiplicador)"))
#         for multiplicando_modif in range (1, multiplicando_modif + 1): #aca se ejecuta hasta el numero que ponga el usuario
#             multiplo = num_ingresado * multiplicando_modif 
#             print(f"{multiplicando_modif} x {num_ingresado} = {multiplo}"); 
                       
#     else:
#         for i in range (1, 11): #aca se ejecuta hasta x 10
#                 multiplo = num_ingresado * i
#                 print(f"{i} x {num_ingresado} = {multiplo}");
#     # no utilizo return dado que ya me devuelve un print en ambas condiciones.

# print("Bienvenidx. Esto es una tabla de multiplicar.")
# print("Hay 2 valores para ingresar.")
# print("Primero, el  mutiplicando")
# print("Segundo, el multiplicador")
# num_ingresado = int(input("Por favor ingresa el numero a multiplicar (multiplicando): "))
# modificar = input("Queres modificar el multiplicador (por defecto es 10) ? S/N: ")
# tabla_multiplicar(num_ingresado)

# Ejercicio 13
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. 
# Agregar validaciones.

# def obtener_datos() -> int|float|None:

    # dato = input("Tipee que tipo de dato va a ingresar:" \
    # " entero, flotante o un texto: ")

    # match dato:
        # case "entero":
            # dato = int(input("Ingrese el número entero: "))
        # case "flotante":
            # dato = float(input("Ingrese el número flotante: "))
        # case "texto":
            # dato = str(input("Ingrese la cadena de texto: "))
            
    # return dato

# obtener_datos()
