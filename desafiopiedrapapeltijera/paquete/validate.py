
def validate_number(valor: float|int, mensaje_error:str, minimo:int|float, maximo:int|float, reintentos:int) -> None:
    '''
    Valida enteros y^o flotantes

    Recibe valor enteros o flotantes

    Retorna nada
    '''
    
    x = 0
    
    if type(valor) ==  int:
    
        while x < reintentos:
            #x += 1
            if minimo <= valor and maximo >= valor:
                print("Tu numero fue aceptado.")
                break
            else:
                print(mensaje_error)
                valor = int(input("Ingresa un numero: "))
                x += 1            

        if x == reintentos:
            print("Llegaste al limite de reintentos")
            return None
            
    if type(valor) ==  float:
    
        while x < reintentos:
            x += 1
            if minimo <= valor and maximo >= valor:
                print("Tu numero fue aceptado.")
                break
            else:
                print(mensaje_error)            
                valor = float(input("Ingresa un numero: "))

        if x == reintentos:
            print("Llegaste al limite de reintentos")


def validate_length(texto:str, longitud:int) -> None:

    '''
    Esta funcion valida la longitud de 
    una cadena de texto.

    Recibe texto y longitud en medida de enteros

    Retorna nada
    '''
    
    bandera = True
    
    while bandera:
        if len(texto) <= longitud:
            bandera = False 
            return texto                  
        else:
            print("ER#0R_*")
            texto = input("Ingrese una cadena de texto: ")