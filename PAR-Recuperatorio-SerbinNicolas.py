# Usted ha sido contratado para desarrollar una solución que le permita al dpto.
# De RRHH obtener de manera ágil el estado de los gastos por viáticos. 
# La empresa tiene los datos de viáticos del mes en un archivo csv. 
# El sistema deberá :

#A) Tener un menú de acciones 
import csv
import os.path

def menu():
    ARCHIVO_DOS = ""
    ARCHIVO = ""
    CAMPOS = ['Legajo', 'Apellido', 'Nombre']
    while True:
        print ("Bienvenido a Workday....")
        print("Elija una opcion: \n 1.Para Guardar datos \n 2.Para ver Gastos \n 3.Para Salir ")
        opcion = input("")
        if opcion == "1":
            guardar(ARCHIVO, CAMPOS)
        elif opcion == "2":
            gastos(ARCHIVO, ARCHIVO_DOS)
        elif opcion == "3":
            exit()
        else:
            print("Opción Incorrecta \n Por favor elija una opcion valida")

# B) Permitir la carga de datos del legajo completo (legajo, apellido, nombre) y
# guardarlos en un archivo csv cuyo nombre será dado por el usuario. Si el 
# archivo ya existe deberá preguntar si se desea agregar o sobreescribirlo. 
# sólo validar que Legajo  sea un entero
def guardar(archivo, campos):
    guardar = "Si"
    lista_empleados = []
    while guardar == "Si":
        empleado = {}
        for campo in campos:
            if campo == campos[0]:
                valor = input(f"Ingrese {campo} del empleado: ")
                empleado[campo]= verific_int(campo, valor)
            else:
                empleado[campo] = input(f"Ingrese {campo} del empleado: ")
        lista_empleados.append(empleado)
        guardar = input("Desea seguir agregando empleados? Si/No: ")
    try:
        archivo = input("Ingrese el nombre del archivo: ") + ".csv"
        if os.path.isfile(archivo) == True:
            TipoDeGuardado= int(input("Para modificar el archivo, 1... Para sobrescribirlo, 2"))
            if TipoDeGuardado == 1:
                with open(archivo, 'a', newline='') as file:
                        
                    file_guarda = csv.DictWriter(file, fieldnames=campos, delimiter=';')
                                            
                    file_guarda.writerows(lista_empleados)
                    print("Se guardo correctamente")
                    return
            elif TipoDeGuardado == 2:
                with open(archivo, 'w+', newline='') as file:
                    file_guarda = csv.DictWriter(file, fieldnames=campos, delimiter=';')
                    file_guarda.writerows(lista_empleados)
                    print("Se guardo correctamente")
                    return
        else:
            with open (archivo, 'w', newline='') as file:
                file_guarda = csv.DictWriter(file, fieldnames=campos, delimiter=';')
                file_guarda.writeheader()
                file_guarda.writerows(lista_empleados)
    except IOError:
        print("Ocurrio un error con el archivo")

def verific_int(campo, valor):
    while not valor.isdigit():
        valor=input(f'\n No es un valor valido, colocar un {campo}')
    print(valor)
    return valor

# C) Dado el número de legajo de un empleado calcular e informar en pantalla los
# gastos que hizo hasta el momento,  junto con el resto de sus datos. Si superó 
# los $5000 indicar que se ha pasado del presupuesto y por cuanto. 
# Por ejemplo "Legajo 1 : Laura Estebanez, gastó $9000 y se ha pasado del 
# presupuesto por $4000" Caso contrario solo mostrar:  
# "Legajo 1 : Laura Estebanez, gastó $488" 
def gastos(archivo, archivo_dos):
    archivo = input("Ingrese el nombre del Registro de Legajos: ") + ".csv"
    archivo_dos = input("Ingrese el nombre del Registro de Gastos: ") + ".csv"
    if os.path.isfile(archivo) and os.path.isfile(archivo_dos) == True:
        try:
            with open(archivo, 'r', newline='') as fileOne,open (archivo_dos, 'r', newline='') as fileTwo:
                lectura_csv_one = csv.DictReader(fileOne, delimiter=';')
                legajos = lectura_csv_one.fieldnames
                lectura_csv_two = csv.DictReader(fileTwo, delimiter=';')
                gastos = lectura_csv_two.fieldnames
                contador = 0  
                ingreso_legajo= input("Ingrese el numero de legajo: ")
                for linea in lectura_csv_two:
                    legajo = linea[gastos[0]]
                    if legajo == ingreso_legajo:
                        contador += int(linea[gastos[1]])
                for linea in lectura_csv_one:
                    if contador < 5000:
                        print(f"Legajo : {linea[legajos[0]]} {linea[legajos[2]]} {linea[legajos[1]]}, gasto ${contador}.")
                    else:
                        print(f"Legajo : {linea[legajos[0]]} {linea[legajos[2]]} {linea[legajos[1]]}, gasto ${contador} y se ha pasado del presupuesto por ${contador-5000}")
        except IOError:
            print("El archivo no existe")
menu()