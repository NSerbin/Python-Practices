""" 1) Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
diccionario. """


divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Ingrese una divisa: ")
print(divisas.get(divisa.title(), "La divisa no está."))

""" 2) Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un 
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y 
su número de teléfono es <teléfono>. """

nombre = input("Ingrese su Nombre: ")
edad = int(input("Ingrese su Edad: "))
direccion = input("Ingrese su Dirección: ")
telefono = int(input("Ingrese su teléfono: "))
datos = {'nombre': nombre, 'edad': edad, 'dir': direccion, 'tel': telefono}
print("se llama", datos['nombre'], "tiene", datos['edad'], "vive en", datos['dir'], "y su telefono es", datos['tel'])

""" 3) Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello. 
_________________________
| Fruta	    |    Precio |
| Plátano	|    1.35   |
| Manzana	|    0.80   |
| Pera	    |    0.85   |
| Naranja   |    0.70   |
-------------------------"""

ventas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
frutas = input("Cuál fruta deseas?").title()
kilos = float(input("Cuántos Kilogramos deseas?"))
if frutas in ventas:
    print(f"{kilos} Kg de {frutas} valen {ventas[frutas]*kilos}")
else:
    print(f"Lo siento, la fruta {frutas} solicitada no está disponible.")

""" 4) Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma 
fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes. """

meses = {1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'}
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/")
print(f"{fecha[0]} de  {meses[int(fecha[1])]} de {fecha[2]}")

""" 5) Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las 
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de 
créditos del curso. """

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos_totales = 0
for materia, creditos in curso.items():
    print(f"La {materia} tiene {creditos} Creditos")
    creditos_totales += creditos
print (f"El número total de Créditos del curso es: {creditos_totales}")

""" 6) Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una 
persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. """

datos = {}
continuar = "si"
while continuar == "si":
    tipo = input("Qué dato desea agregar? ")
    valor = input(f'{tipo} : ')
    datos[tipo] = valor
    print(datos)
    continuar = input("Desea continuar? ")

""" 7) Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.
________________________
|Lista de la compra	    |
|Artículo 1	  |  Precio |
|Artículo 2	  |  Precio |
|Artículo 3	  |  Precio |
|   …	      |      …  |
|Total	      |  Coste  |
-------------------------"""

lista = {}
continuar = "si"

while continuar == "si":
    articulo = input("Introduzca el articulo que desea comprar: ")
    precio = float(input(f"Ingrese el valor de {articulo}: "))
    lista[articulo] = precio
    continuar = input("Desea continuar? ")
costo = 0
print("Lista de la compra")
for articulo, precio in lista.items():
    print(f"{articulo} \t {precio}")
    costo += precio
print(f"El coste total es de {costo}")

""" 8) Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se 
almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la 
factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada 
operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

facturas = {}
facturas_pagas = 0
sin_cobrar = 0
continuar = ""

while continuar != "T":
    if continuar == "A":
        factura = int(input("Ingrese el número de factura: "))
        costo = float(input("Ingrese el costo de la factura: "))
        facturas[factura] = costo
        sin_cobrar += costo
    elif continuar == "P":
        factura = int(input("Ingrese el número de factura: "))
        costo = facturas.pop(factura, 0)
        facturas_pagas += costo
        sin_cobrar -= costo
    print(f"Se recaudaron {facturas_pagas} Facturas.")
    print(f"Faltan cobrar {sin_cobrar} Facturas.")
    continuar = input("Para añadir una nueva factura digite A, Para pagar una nueva factura digite P, de lo contrario digite T para terminar.")

""" 9) Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se 
guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con 
los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si 
se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente 
(2) Eliminar cliente
(3) Mostrar cliente
(4) Listar todos los clientes
(5) Listar clientes preferentes 
(6) Terminar 
En función de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa."""

clientes = {}
opcion = ""

while opcion != 6:
    if opcion == 1:
        nif = input("Ingrese el NIF del cliente: ")
        nombre = input("Ingrese el Nombre del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        email = input("Ingrese el email del cliente: ")
        vip = input("Es un cliente preferente?")
        cliente = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'email': email, 'vip': vip =='S'}
        clientes[nif] = cliente
    elif opcion == 2:
        nif = input("Ingrese el NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print(f"No existe el cliente con ese {nif}.")
    elif opcion == 3:
        nif = input("Ingrese el NIF del cliente: ")
        if nif in clientes:
            print(f"El NIF es: {nif}")
            for key, value in clientes[nif].items():
                print(f'{key.title()}:', value)
        else:
            print("No existe ningun cliente con el nif solicitado.")
    elif opcion == 4:
        print("La lista de clientes es: ")
        for key, value in clientes.items():
            print(key, value[nombre])
    elif opcion == 5:
        print("La lista de clientes preferentes es: ")
        for key, value in clientes.items():
            if value["vip"]:
                print(key, value["nombre"])
    opcion = input("Menu: \n 1) Añadir cliente \n 2) Eliminar cliente \n 3) Mostrar cliente \n 4) Listar todos los clientes \n 5) Listar clientes preferentes \n 6) Terminar ")