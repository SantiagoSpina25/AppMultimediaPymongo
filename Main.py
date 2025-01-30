from ControladorBd import *

eleccion = 0

while (eleccion != 6):
    eleccion = int(input("\nQue desea realizar \n1.INSERT \n2.SELECT \n3.UPDATE \n4.DELETE \n5.CREAR COLECCION \n6.SALIR \n"))
    if eleccion == 1:
        realizarInsert()
    elif eleccion == 2:
        realizarSelect()
    elif eleccion == 3:
        realizarUpdate()
    elif eleccion == 4:
        realizarDelete()
    elif eleccion == 5:
        crearColeccion()
    elif eleccion == 6:
        print("Saliendo...")
    else:
        print("Elegí un numero del 1 al 6")
        print("\n")

# Cierro la conexion
conexion.close()