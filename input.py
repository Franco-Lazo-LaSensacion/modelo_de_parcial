import validate

def get_int (mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    '''
    '''
    
    print(mensaje)
    
    numero = int(input("Ingresa un numero entero: "))

    validate.validate_number(numero, mensaje_error, minimo, maximo, reintentos)

    return numero
    
        
        
def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:

    '''
    '''

    print(mensaje)

    valor = float(input("Ingresa un numero flotante: "))
       
    validate.validate_number(valor, mensaje_error, minimo, maximo, reintentos)
        
        
def get_string(longitud: int) -> str|None:
    '''
    '''
    
    texto = input("Ingrese una cadena de texto: ")
    
    return validate.validate_length(texto, longitud)
    
