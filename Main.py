from ControladorBd import *

eleccion = 0

while (eleccion != 6):
    eleccion = int(input("\nQue desea realizar \n1.INSERT \n2.SELECT \n3.UPDATE \n4.DELETE \n5.SALIR \n"))
    if eleccion == 1:
        realizarInsert()
    elif eleccion == 2:
        realizarSelect()
    elif eleccion == 3:
        realizarUpdate()
    elif eleccion == 4:
        realizarDelete()
    elif eleccion == 5:
        print("Saliendo...")
    else:
        print("Elegí un numero del 1 al 5")
        print("\n")

# Cierro la conexion
conexion.close()