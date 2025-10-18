from paquete import funciones


salones = [["Puerto Madero"],
              ["Palermo"],
             ["San Telmo"]]

eventos = ["cumpleaños",
           "casamientos",
           "fiestas de 15",
            "bodas de oro"]

def cargar_eventos() -> list:
    '''
    Carga secuencialmente eventos realizados que contienen un tipo de evento y un salon

    Retorna la planilla
    '''

    planilla = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    ejecutar = True

    while ejecutar:

        for i in range(len(planilla)):

            for j in range(len(planilla) + 1):

                rta = input(f"¿Quiere cargar un evento de ({eventos[j]}) en el salon de {salones[i]}? [Si/No]: ")

                while rta == "Si" or rta == "S" or rta == "SI" or rta == "si" or rta == "s":
                    valor = 1
                    planilla[i][j] = planilla[i][j] + valor
                    break

        seguir = input("Presione ENTER, dejando vacio, para seguir ingresando eventos o '0' para terminar: ")

        if seguir == "0":
            ejecutar = False

    return planilla

planilla = cargar_eventos()

recaudacion = funciones.calcular_recaudacion(planilla)

funciones.calcular_cant_fiestas(planilla)

funciones.consultar_evento(planilla)

funciones.calcular_casamientos(planilla)

print(funciones.calcular_porcentaje(planilla, "bodas de oro"))

print("la recaudacion total de los salones de manera ordenada es: ", funciones.generar_informe(recaudacion))