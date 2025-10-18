def mostrar_positivos_o_negativos(lista: list) -> str:

    '''
    Busca los positivos dentro de una lista

    Recibe una lista

    Retorna un string
    '''

    cantidad_de_positivos = 0
    cantidad_de_negativos = 0

    for i in range(len(lista)):
        
        if lista[i] > 0:
            cantidad_de_positivos += 1
        elif lista[i] < 0:
            cantidad_de_negativos += 1

    mensaje = "Numeros positivos ingresados son:", cantidad_de_positivos, "Numeros negativos ingresados son:", cantidad_de_negativos

    return mensaje

def mostrar_valores_en_indices_impares(lista: list) -> str:

    '''
    Busca los numeros posicionados en indices impares

    Recibe una lista

    Devuelve un string
    '''

    valores = []

    for i in range(len(lista)):

        if (i % 2) != 0:
            valor = lista[i]

            valores += [valor]
    
    mensaje = f"Los numeros posicionados en indices impares son: {valores}"
            
        
    return mensaje

def buscar_mayor_impar(lista: list) -> str:

    '''
    Identifica y muestra el mayor numero impar ingresador

    Recibe una lista

    Retorna un string   
    '''

    flag = True

    for i in range(len(lista)):
        
        if flag:

            if lista[i] % 2 != 0:

                maximo = lista[i]
                flag = False

        if (lista[i] % 2 != 0) and (lista[i] > maximo):
            maximo = lista[i]

    mensaje = f"El mayor de los numeros impares de la lista es: {maximo}"

    return mensaje
