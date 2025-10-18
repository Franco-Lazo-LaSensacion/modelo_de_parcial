from paquete import *

#Menu
ejecutar = True

while ejecutar:
    eleccion = int(input("🔹 Bienvenido 🔹\n🔹 Opciones del Menú 🔹\n🔹 Vas a realizar distintas operaciones con un conjunto de números 🔹" \
"\n🔹 [1] Cargar datos 🔹" \
"\n🔹 [2] Cantidad de positivos y negativos 🔹" \
"\n🔹 [3] Suma de los números pares 🔹" \
"\n🔹 [4] Mayor número impar 🔹" \
"\n🔹 [5] Listar los números ingresados 🔹" \
"\n🔹 [6] Listar los números pares 🔹" \
"\n🔹 [7] Listar los números en posiciones impares 🔹" \
"\n🔹 [8] Salir del programa 🔹" \
"\n🔹[Ingrese numero de opcion]: "))

    if eleccion != 1:
        print("ERR0R. Sin ingresar datos el programa no puede iniciar.")
    elif eleccion == 1:
        datos = obtener_datos()
        break


eleccion = int(input("🔹 Bienvenido 🔹\n🔹 Opciones del Menú 🔹\n🔹 Vas a realizar distintas operaciones con un conjunto de números 🔹" \
"\n🔹 [1] Cargar datos 🔹" \
"\n🔹 [2] Cantidad de positivos y negativos 🔹" \
"\n🔹 [3] Suma de los números pares 🔹" \
"\n🔹 [4] Mayor número impar 🔹" \
"\n🔹 [5] Listar los números ingresados 🔹" \
"\n🔹 [6] Listar los números pares 🔹" \
"\n🔹 [7] Listar los números en posiciones impares 🔹" \
"\n🔹 [8] Salir del programa 🔹" \
"\n🔹[Ingrese numero de opcion]: "))

match eleccion:
    case 2:
        print(mostrar_positivos_o_negativos(datos))
    case 3:
        print(sumar_pares(datos))
    case 4:
        print(buscar_mayor_impar(datos))
    case 5:
        print(listar_lista(datos))
    case 6:
        print(listar_numeros_pares(datos))
    case 7:
        print(mostrar_valores_en_indices_impares(datos))
    case 8:
        print("🔹Abandonando programa...🔹")