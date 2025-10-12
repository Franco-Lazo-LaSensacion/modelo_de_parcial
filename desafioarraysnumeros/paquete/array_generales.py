def sumar_pares(lista: list) -> str:

    '''
    Suma los numeros pares y los muestra

    Recibe una lista

    Retorna un string
    '''

    acumulador = 0

    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            acumulador += lista[i]
            mensaje = f"La sumatoria de los numeros pares de la lista es: {acumulador}"

    return mensaje

def obtener_datos(dimension: int = 10) -> list:

    '''
    Obtiene datos por parametro

    Recibe enteros en forma de lista

    Devuelve los datos en forma de lista
    '''
    
    numeros = [False] * dimension

    for i in range(len(numeros)):

        numero = int(input("Ingrese un numero (entre -1000 y 1000): "))

        while numero > 1000 or numero < -1000:
            print("ERR0R. Rango excedido.")
            numero = int(input("Ingrese un numero (entre -1000 y 1000): "))

            if numero < 1000 and numero > -1000:
                numeros[i] = numero
                break 

        numeros[i] = numero

    return numeros

def listar_lista(lista: list) -> str:

    '''
    Muestra una lista en la forma que fue ingresada

    Recibe una lista

    Retorna una string
    '''

    guardada = lista

    mensaje = f"Los numeros que ingresaste son: {guardada}"

    return mensaje

def listar_numeros_pares(lista: list) -> str:

    '''
    Lista los numeros pares de una lista

    Recibe una lista

    Retorna un string
    '''

    contador = 0
    valores = []

    for i in range(len(lista)):

        if lista[i] % 2 == 0:
            contador += 1
            valor = lista[i]

            valores += [valor]
    
    mensaje = f"Los numeros pares listados son: {valores}"

    return mensaje

def mostrar_menu() -> str:
    pass