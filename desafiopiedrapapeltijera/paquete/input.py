import Cursada.desafioppot.paquete.validate as validate

def get_int (mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    '''
    Obtiene enteros

    Recibe parametros de mensaje, mensaje de error, minimo y maximo de enteros
    y reintentos en caso de error

    Devuelve enteros o nada
    '''
    
    print(mensaje)
    
    numero = int(input("Ingresa un numero entero: "))

    validate.validate_number(numero, mensaje_error, minimo, maximo, reintentos)

    return numero
    
        
        
def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:

    '''
    Obtiene flotantes

    Recibe parametros de mensaje, mensaje de error, minimo y maximo de flotantes
    y reintentos en caso de error

    Devuelve flotantes o nada
    '''

    print(mensaje)

    valor = float(input("Ingresa un numero flotante: "))
       
    validate.validate_number(valor, mensaje_error, minimo, maximo, reintentos)
        
        
def get_string(longitud: int) -> str|None:
    '''
    Obtiene entero de longitud

    Recibe parametros de longitud

    Devuelve cadena de texto si fue validada con su longitud
    '''
    
    texto = input("Ingrese una cadena de texto: ")
    
    return validate.validate_length(texto, longitud)
    
