""" 1--- 
"""
# jugador = int(input("Ingrese su altura en centímetros (ej: 175): "))
# posicion_del_jugador = "Indefinido"

# if jugador < 160:
    # posicion_del_jugador = "Base"
# elif jugador <= 179:
    # posicion_del_jugador = "Escolta"
# elif jugador <= 180: 
    # posicion_del_jugador = "Alero"
# else:
    # posicion_del_jugador = "Ala-Pívot o Pívot"

# print(f"Tu posición en cancha es: {posicion_del_jugador}.")

""" 2---
"""

# nota = int(input("Ingrese una nota aleatoria del 1 al 10 inclusive: "))

# if nota > 10 or nota < 1:
    # print("Ingrese una nota válida.")
# elif nota >= 6:
    # print(f"Promoción directa, la nota es...{nota}.")
# elif nota == 4 or nota == 5:
    # print(f"Aprobado, la nota es...{nota}.")
# else: 
    # print(f"Desaprobado, la nota es...{nota}.")

""" 1 
    (Match)
"""

# lugar_de_viaje = input("¿Cuál es la estación del año que prefiere si quisiera viajar?: ")

# match lugar_de_viaje:
    # case "invierno":
        # print("¡Se viaja! En invierno usted puede ir a Bariloche.")
    # case "verano":
        # print("¡Se viaja! En verano usted puede ir a Mar del Plata y Cataratas.")
    # case "otoño":
        # print("¡Se viaja! En otoño puede ir a todos los lugares.")
    # case "primavera":
        # print("¡Se viaja! En primavera usted puede ir a todos los lugares, excepto Bariloche.")
    # case _: 
        # print("¡No se viaja!")

""" Desafío
        Gotita S.A.
 """

# metros_consumidos = int(input("Ingrese aquí la cantidad de metros consumidos: "))
# tipo_cliente = str(input("Ingrese aquí que tipo de cliente es (Residencial, Comercial o Industrial): "))

# cargo_fijo = 7000 #Impuesto
# costo_m3 = 200 #Costo por metro, agua
# bonificacion = 0
# recargo = 0


# subtotal = (metros_consumidos * costo_m3) #Cálculo

# match tipo_cliente:   
    # case "Residencial":
        # if metros_consumidos < 30:
            # bonificacion = 0.10
        # elif metros_consumidos > 80:
            # recargo = 0.15
        # if subtotal < 35000: #Se necesita aprox. 150 metros consumidos para llegar a ese subtotal sin imp. ni bonif.
            # bonificacion = 0.05
    # case "Comercial":
        # if metros_consumidos > 150:
            # bonificacion = 0.08
        # elif metros_consumidos > 300:
            # bonificacion = 0.12
        # else:
            # metros_consumidos < 50
            # recargo = 0.05
    # case "Industrial":
        # if metros_consumidos > 500:
            # bonificacion = 0.20
        # elif metros_consumidos > 1000:
            # bonificacion = 0.30
        # else:
            # metros_consumidos < 200
            # recargo = 0.10

# bonificaciones = (bonificacion * subtotal) #Cálculo bonif.
# recargos = (recargo * subtotal) #Cálculo recargo.
# subtotal_dos = (subtotal - bonificaciones + recargos + cargo_fijo) #Subtotal todo incluido.
# iva = (subtotal_dos * 0.21) #Cálculo iva
# total = (subtotal_dos + iva) #Total, suma de todo

# print(f"Subtotal de consumo: ${subtotal}")
# print(f"Bonificación: ${bonificaciones}")
# print(f"Recargo: ${recargos}")
# print(f"Subtotal de consumo con recargos y bonificaciones: ${subtotal_dos}")
# print(f"IVA aplicado: ${iva}")
# print(f"Total final a saldar: ${total}")

