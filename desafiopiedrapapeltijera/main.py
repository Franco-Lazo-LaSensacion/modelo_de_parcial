#MAIN

import random
import Cursada.desafioppot.paquete.functions as functions
import Cursada.desafioppot.paquete.input as input
import Cursada.desafioppot.paquete.validate as validate


def jugar_piedra_papel_tijera() -> str:

    ronda_actual = 0
    flag = True
    aciertos_jugador = 0
    aciertos_maquina = 0

    while functions.verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):

        if flag:
            print("[PIEDRA, PAPEL O TIJERA]")
            print(" [AL MEJOR DE 3 RONDAS]")
            print("    [REGLAS BASICAS]")
            print("...PIEDRA MATA TIJERA...")
            print("...PAPEL MATA PIEDRA...")
            print("...TIJERA MATA PAPEL...")
            flag = False

        jugador = input.get_int("Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera): ", "ERROR.", 1, 3, 2)

        maquina = random.randint(1,3)
        print("La maquina eligio", functions.mostrar_elemento(maquina))

        print("Vos elegiste", functions.mostrar_elemento(jugador))
        print("RESULTADO >", functions.verificar_ganador_ronda(jugador, maquina))
        ronda_actual += 1   

        if functions.verificar_ganador_ronda(jugador, maquina) == "Ganador > Jugador":
            aciertos_jugador += 1   
        elif functions.verificar_ganador_ronda(jugador, maquina) == "Te gano la Maquina!":
            aciertos_maquina += 1
        
jugar_piedra_papel_tijera()
