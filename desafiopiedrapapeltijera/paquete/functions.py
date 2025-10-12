#FUNCTIONS

def mostrar_elemento(eleccion: int) -> str:


    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"
        
def verificar_ganador_ronda(jugador: int, maquina: int) -> str:

    resultado = "Empate"

    if jugador == 1 and maquina == 3:
        resultado = "Ganador > Jugador"
    elif jugador == 2 and maquina == 1:
        resultado = "Ganador > Jugador"
    elif jugador == 3 and maquina == 2:
        resultado = "Ganador > Jugador"

    elif jugador == maquina:
        resultado = "Empate"

    else:
        resultado = "Te gano la Maquina!"
    
    return resultado

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:

    

    if aciertos_jugador == 2:
        return False
    elif aciertos_maquina == 2:
        return False
    elif ronda_actual == 3:
        return False
    else:
        return True
