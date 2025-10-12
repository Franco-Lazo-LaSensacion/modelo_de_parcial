from paquete import array_generales
from paquete import especificas

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

    while eleccion != 1:
        print("ERR0R. Sin ingresar datos el programa no puede iniciar.")
        break

if eleccion == 1:
    datos = array_generales.obtener_datos()

match eleccion:
    case 2:
        especificas.mostrar_positivos_o_negativos(datos)
    case 3:
        array_generales.sumar_pares(datos)
