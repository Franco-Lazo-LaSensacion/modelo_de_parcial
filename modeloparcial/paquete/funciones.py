def calcular_cant_fiestas(planilla: list) -> list:

    '''
    Muestra la cantidad de fiestas por cada salon

    Recibe una lista

    Retorna una lista
    '''

    cantidad = [[0], [0], [0]]

    for i in range(len(planilla)):
        
        for j in range (len(planilla)):

            cantidad[i][j] = planilla[i][0] + planilla[i][1] + planilla[i][2] + planilla[i][3]

            break

    return cantidad


def consultar_evento(planilla: list) -> int:

    '''
    Consulta el evento mas realizado en cada salon

    Recibe lista

    Retorna entero
    '''
    mayor = 0
    mayor1 = 0
    mayor2 = 0

    if planilla[0][0] > planilla[0][1] and planilla[0][0] > planilla[0][2] and planilla[0][0] > planilla[0][3]:
        mayor = planilla[0][0]
    elif planilla[0][1] > planilla[0][0] and planilla[0][1] > planilla[0][2] and planilla[0][1] > planilla[0][3]:
        mayor = planilla[0][1]
    elif planilla[0][2] > planilla[0][0] and planilla[0][2] > planilla[0][1] and planilla[0][2] > planilla[0][3]:
        mayor = planilla[0][2]
    elif planilla[0][3] > planilla[0][0] and planilla[0][3] > planilla[0][1] and planilla[0][3] > planilla[0][2]:
        mayor = planilla[0][3]

    if planilla[1][0] > planilla[0][1] and planilla[0][0] > planilla[0][2] and planilla[0][0] > planilla[0][3]:
        mayor1 = planilla[1][0]
    elif planilla[1][1] > planilla[0][0] and planilla[0][1] > planilla[0][2] and planilla[0][1] > planilla[0][3]:
        mayor1 = planilla[1][1]
    elif planilla[1][2] > planilla[0][0] and planilla[0][2] > planilla[0][1] and planilla[0][2] > planilla[0][3]:
        mayor1 = planilla[1][2]
    elif planilla[1][3] > planilla[0][0] and planilla[0][3] > planilla[0][1] and planilla[0][3] > planilla[0][2]:
        mayor1 = planilla[1][3]

    if planilla[2][0] > planilla[0][1] and planilla[0][0] > planilla[0][2] and planilla[0][0] > planilla[0][3]:
        mayor2 = planilla[2][0]
    elif planilla[2][1] > planilla[0][0] and planilla[0][1] > planilla[0][2] and planilla[0][1] > planilla[0][3]:
        mayor2 = planilla[2][1]
    elif planilla[2][2] > planilla[0][0] and planilla[0][2] > planilla[0][1] and planilla[0][2] > planilla[0][3]:
        mayor2 = planilla[2][2]
    elif planilla[2][3] > planilla[0][0] and planilla[0][3] > planilla[0][1] and planilla[0][3] > planilla[0][2]:
        mayor2 = planilla[2][3]

    return mayor, mayor1, mayor2


costos = [33000, 175000, 600000, 1300000]

def calcular_recaudacion(planilla: list) -> list:

    '''
    Calcula la recaudacion de cada salon

    Recibe una lista

    Retorna una lista
    '''

    recaudacion = [[0], [0], [0]]

    for i in range(len(planilla)):

        for j in range(len(planilla) + 1):

            recaudacion[i][j] = costos[0] * planilla[i][j] + costos[1] * planilla[i][j + 1] + costos[2] * planilla[i][j + 2]+ costos[3] * planilla[i][j + 3]

            break

    return recaudacion

def calcular_casamientos(planilla: list) -> int:

    '''
    Calcula la cantidad de salones que superan los 5M de pesos en casamientos

    Recibe una lista

    Retorna un entero
    '''

    contador = 0

    for i in range(len(planilla)):

        for j in range(len(planilla) - 2):

            total = costos[1] * planilla[i][1]
            
            if total > 5000000:
                contador += 1

            break

    return contador


#  6. Calcular el porcentaje de bodas de oro realizadas en cada salón.
#  Mostrar el que haya realizado el mayor porcentaje

def calcular_porcentaje(planilla: list, buscado: str) -> None:

    '''
    Calcula el porcentaje del evento deseado realizado en cada salon

    Recibe una lista

    Retorna None
    '''

    porcentaje1 = (planilla[0][3] * 100) / 100
    porcentaje2 = (planilla[1][3] * 100) / 100
    porcentaje3 = (planilla[2][3] * 100) / 100
    maximo = 0
    salon = ""
    if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
        maximo = porcentaje1
    elif porcentaje2 > porcentaje1 and porcentaje2 > porcentaje3:
        maximo = porcentaje2
    elif porcentaje3 > porcentaje1 and porcentaje3 > porcentaje2:
        maximo = porcentaje3         

    if maximo == porcentaje1:
        salon = "Puerto Madero"
    elif maximo == porcentaje2:
        salon = "Palermo"
    elif maximo == porcentaje3:
        salon = "San Telmo"

    mensaje = f"El mayor porcentaje de {buscado} entre los 3 salones es el de: %{maximo} en el salon de {salon}."
            
    return mensaje

salones = [["Puerto Madero"],
              ["Palermo"],
             ["San Telmo"]]

def generar_informe(lista: list) -> list:

    '''
    genera un informe de la recaudacion de los salones (ordenada)

    recibe una lista

    retorna un string
    '''

    if type(lista) != list:
        print("El parametro recibido no es una lista")
        return
    
    n = len(lista)
    
    for i in range(n):

        for j in range(0, n - i - 1):
            
            if lista[j] < lista[j + 1]:

                menor = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = menor

    return lista        

