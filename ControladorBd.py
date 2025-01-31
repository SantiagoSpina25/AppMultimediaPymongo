import pymongo

# Creo la conexion y la base de datos
conexion = pymongo.MongoClient("mongodb://localhost:27017/ConexionAppMultimediaPymongo")
bd = conexion["app_multimedia"]

# Si encuentra la base de datos, lo aviso por consola
if "app_multimedia" in conexion.list_database_names():
  print("La base de datos existe")
else:
  print("La base de datos no fue encontrada")


def realizarInsert():
    volver = False

    print("\nEstas son las colecciones disponibles: " + str(bd.list_collection_names()))
    nombreColeccion = input("Que coleccion desea utilizar?\n")

    #Si la coleccion no existe en la bd, la crea
    if nombreColeccion not in bd.list_collection_names():
        eleccionNuevaColeccion = int(input("Esa coleccion no existia, ¿Desea crearla? 1.Si 2.No\n"))
        if eleccionNuevaColeccion == 1:
            print("\nColeccion creada\n")
        elif eleccionNuevaColeccion == 2:
            volver = True
    
    if volver != True:
        insercionDeRegistro(nombreColeccion)
    

def insercionDeRegistro(nombreColeccion):
    #Busco la coleccion en la bd
    coleccion = bd[nombreColeccion]

    # Creo un array para almacenar todos los campos (clave - valor)
    valoresCampos = {}
    valorCampo = ""

    #Busco un documento para mostrar los campos de esa coleccion
    documentoEjemplo = coleccion.find_one()

    #En el caso que la coleccion este vacia
    if not documentoEjemplo:
        print("La coleccion esta vacia, ingrese los campos que quiere ingresar y sus valores")

        #Bucle pidiendo nuevos campos y registros y termina cuando pone uno vacio
        while True:
            nuevoCampo = input("\nIngrese un campo nuevo. Dejar vacio para dejar de agregar\n")

            if nuevoCampo == "":
                break

            nuevoValor = input("\n Ahora ingrese su valor: \n")

            valoresCampos[nuevoCampo] = convertirTipo(nuevoValor)

        #Cuando deje de agregar campos, inserta el nuevo registro
        

    #Caso en el que hay campos existentes en la coleccion
    else:
        #Muestro cada campo y pido un valor. Tambien saltea el campo _id
        for campo in documentoEjemplo.keys():
            if campo != "_id":
                valorCampo = input(campo + ": ")
            #inserto con la clave del campo el valor ingresadoS
            valoresCampos[campo] = convertirTipo(valorCampo)

        #Elimino el id para que se genere automaticamente
        valoresCampos.pop("_id")

    
    #Inserto el registro
    resultadoInsert = coleccion.insert_one(valoresCampos)

    #Muestro el resultado del insert
    if resultadoInsert.inserted_id:
        print("\nEl registro se ha insertado correctamente. ✅\n")
    else:
        print("\nError: No se pudo insertar el registro. ❌\n")


# Metodo que convierte los nuemeros de String a Int
def convertirTipo(valor):
    valorFinal = valor
    if valor.isdigit():
        valorFinal = int(valor)

    return valorFinal  # Si no es número, dejar como string

def realizarSelect():
    print("\nEstas son las colecciones disponibles: " + str(bd.list_collection_names()))
    nombreColeccion = input("Que coleccion desea utilizar?\n")

    # Verifica si existe la coleccion
    if nombreColeccion not in bd.list_collection_names():
        print("\nNo existe una coleccion con ese nombre ❌\n")
    else: # En el caso que exista obtiene todos los documentos y los muestra
        coleccion = bd[nombreColeccion]

        for documento in coleccion.find():
            print(documento)

def realizarUpdate():
    print("\nEstas son las colecciones disponibles: " + str(bd.list_collection_names()))
    nombreColeccion = input("Que coleccion desea utilizar?\n")

    if nombreColeccion not in bd.list_collection_names():
        print("\nNo existe una coleccion con ese nombre ❌\n")
    else: # En el caso que exista pide la condicion para actualizar el documento
        campoCondicion = input("\nIntroduce la condicion para actualizar\n Campo: ")
        valorCondicion = input("\nValor: ")

        campoAModificar = input("\nAhora introduce el campo a actualizar\n Campo: ")
        valorAModificar = input("\nValor a actualizar: ")


        coleccion = bd[nombreColeccion]
        resultado = coleccion.update_one({campoCondicion : valorCondicion}, {"$set": {campoAModificar: valorAModificar}})

        if resultado.modified_count > 0:
            print("El documento se actualizo correctamente ✅")
        else:
            print("No se encontro el documento o no se actualizo ❌")

def realizarDelete():
    print("\nEstas son las colecciones disponibles: " + str(bd.list_collection_names()))
    nombreColeccion = input("Que coleccion desea utilizar?\n")

    # Verifica si existe la coleccion
    if nombreColeccion not in bd.list_collection_names():
        print("\nNo existe una coleccion con ese nombre ❌\n")
    else: # En el caso que exista pide la condicion para eliminar el documento
        campoCondicion = input("\nIntroduce la condicion para borrar\n Campo: ")
        valorCondicion = input("\nValor: ")

        coleccion = bd[nombreColeccion]
        resultado = coleccion.delete_one({campoCondicion : valorCondicion})

        if resultado.deleted_count > 0:
            print("El documento se elimino correctamente ✅")
        else:
            print("No se encontro el documento o no se elimino ❌")

