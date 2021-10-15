import csv
import logging
import re

            # CONFIGURACION DEL MÓDULO LOGGING USADO PARA GENERAR 
            # REPORTES DE LOGS
logging.basicConfig(
    filename= 'register.log', 
    filemode= 'a',
    format= '%(asctime)s | %(levelname)s | %(message)s',
    datefmt= '%d/%m/%Y %I:%M:%S %p',
    level= logging.INFO
    )

            # FUNCION QUE VERIFICA SI UN EMAIL ES VALIDO, 
            # EN CASO DE NO SERLO, CORTA LA EJECUCION DEL 
            # PROGRAMA INFORMANDO EL ERROR
def email_verificator(mail):
    if re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        logging.info(f"Iniciando validación de cantidad de emails")
        pass
    else:
        print("El archivo contiene mails inválidos.")
        logging.error("Mails contienen errores.")
        raise Exception ("El archivo contiene mails inválidos.")

            # FUNCION QUE VERIFICA SI UN DOCUMENTO ES VALIDO, 
            # EN CASO DE NO SERLO, CORTA LA EJECUCION DEL 
            # PROGRAMA INFORMANDO EL ERROR
def validateDocuments(doc):
    if len(doc) >= 7 and len(doc) <= 8:
        logging.info(f"Iniciando comprobación de cantidad de números en el Documento")
        pass
    else:
        print("El archivo contiene Documentos inválidos.")
        logging.error("Documentos contienen errores.")
        raise Exception ("El archivo contiene Documentos inválidos.")

            # FUNCION QUE VERIFICA SI UN PRECIO TIENE 2 DIGITOS, 
            # EN CASO DE NO SERLO, CORTA LA EJECUCION DEL 
            # PROGRAMA INFORMANDO EL ERROR
def validateDecimals(price):
    if re.match(r"^[0-9]+\.[0-9]{2}$", price):
        logging.info(f"Iniciando comprobación de cantidad de Decimales")
        pass
    else:
        print("El archivo contiene Precios inválidos.")
        logging.error("Precios contienen errores.")
        raise Exception ("El archivo contiene Precios inválidos.")

            # FUNCION QUE VERIFICA SI HAY CAMPOS VACIOS EN 
            # NOMBRE, DIRECCION, FECHA DE ALTA O EMPRESA, 
            # EN CASO DE ESTAR VACIOS, CORTA LA EJECUCION
            # DEL PROGRAMA INFORMANDO EL ERROR
def validateEmptyFields(name, adress, begin, company):
    logging.info(f"Iniciando comprobación de caracteres en los campos.")
    if re.match(r'^\Z', name) or re.match(r'^\Z', adress):
        print("El archivo contiene Campos Vacios")
        logging.error("Campos Vacios en el Archivo.")
        raise Exception ("El archivo contiene Campos Vacios")
    elif re.match(r'^\Z', begin) or re.match(r'^\Z', company):
        print("El archivo contiene Campos Vacios")
        logging.error("Campos Vacios en el Archivo.")
        raise Exception ("El archivo contiene Campos Vacios")
    else:
        pass

            # FUNCION QUE VERIFICA SI HAY CAMPOS VACIOS EN 
            # FECHA DEL VIAJE, EN CASO DE ESTAR VACIOS,
            # CORTA LA EJECUCION DEL PROGRAMA INFORMANDO 
            # EL ERROR
def validateEmptyFieldsTravels(begin):
    logging.info(f"Iniciando comprobación de caracteres en los campos.")
    if re.match(r'^\Z', begin):
        print("El archivo contiene Campos Vacios")
        logging.error("Campos Vacios en el Archivo.")
        raise Exception ("El archivo contiene Campos Vacios")
    else:
        pass

def menu():
    logging.info('Inicio del Script...')
    while True:
        print("===================================================================")
        print("RADIO TAXI RECOLETA VIP", "\U0001F600", "\U0001F600", "\U0001F600")
        print("===================================================================")
        print("Bienvenido al Sistema de Facturación.")
        print("===================================================================")
        print("Por favor, ingrese una opción:")
        print("===================================================================")
        print("[*] 1. Para buscar Usuario por Nombre.")
        print("===================================================================")
        print("[*] 2. Para buscar Total de Usuarios por Empresa.")
        print("===================================================================")    
        print("[*] 3. Para buscar el Monto por Empresa.")
        print("===================================================================")
        print("[*] 4. Para buscar Total de Viajes por Número de Documento.")
        print("===================================================================")
        print("[*] 5. Para Salir.")
        print("===================================================================")
        opcion = input("")
        if opcion == '1':
            ClientNameSearch()
            logging.info(f"El usuario eligió {ClientNameSearch} - Opción 1 -")
        elif opcion == '2':
            ClientQtySearch()
            logging.info(f"El usuario eligió {ClientQtySearch} - Opción 2 -")
        elif opcion == '3':
            DebtQtySearch()
            logging.info(f"El usuario eligió {DebtQtySearch} - Opción 3 -")
        elif opcion == '4':
            TotalTripsSearch()
            logging.info(f"El usuario eligió {TotalTripsSearch} - Opción 4 -")
        elif opcion == '5':
            exit()
        else:
            print("Opción Incorrecta \n Por favor elija una opcion válida")
            logging.warning(f"El usuario ingresó {opcion} la cual es una opción inválida.")

def ClientNameSearch():
    logging.info(f"Iniciando la Búsqueda de Usuario por Nombre.")
    CLIENTS = input("Ingrese el nombre del Registro de Clientes: ") + ".csv"
    logging.info(f"El usuario ingresó {CLIENTS} como nombre del Archivo de Clientes.")

            # SI ARCHIVO CLIENTS EXISTE, INICIA LA APERTURA DEL MISMO
    try:
        with open(CLIENTS, 'r', newline='') as file:
            read_csv = csv.DictReader(file, delimiter=',')
            clientList = read_csv.fieldnames
            clientName = input("Ingrese el nombre del cliente: ")
            logging.info(f"El usuario ingresó {clientName} como nombre de usuario a buscar.")

            # INICIO BUCLE BUSQUEDA DE NOMBRES DE USUARIOS EN ARCHIVO CLIENTS
            for line in read_csv:
                name = line[clientList[0]]
                adress = line[clientList[1]]
                doc = line[clientList[2]]
                begin = line[clientList[3]]
                mail = line[clientList[4]]
                company = line[clientList[5]]
                validateDocuments(doc)
                logging.info(f"Comprobación de Documentos en {CLIENTS} Exitosa.")
                email_verificator(mail)
                logging.info(f"Comprobación de email en {CLIENTS} Exitosa.")
                validateEmptyFields (name, adress, begin, company)
                logging.info(f"Comprobación de Nombre, Dirección, Fecha de Alta y Nombre de Empresa en {CLIENTS} Exitosa.")
            
                if clientName in line[clientList[0]]:
                    print("==================================================")
                    print(f" Nombre: {line[clientList[0]]} \n Dirección: {line[clientList[1]]} \n Documento: {line[clientList[2]]} \n Fecha de Alta: {line[clientList[3]]} \n Correo Electrónico: {line[clientList[4]]} \n Empresa: {line[clientList[5]]}")
                    logging.info(f"Usuario {clientName} encontrado en {CLIENTS} con Éxito.")
    except IOError:
        print(f"Lo sentimos, el Archivo {CLIENTS} no existe.")
        logging.error("El usuario ingresó {CLIENTS} como nombre de Archivo de Clientes, el cual NO EXISTE.")

def ClientQtySearch():
    logging.info(f"Iniciando la Búsqueda del Total de Usuarios por Empresa.")
    CLIENTS = input("Ingrese el nombre del Registro de Clientes: ") + ".csv"
    logging.info(f"El usuario ingresó {CLIENTS} como nombre del Archivo de Clientes.")

            # SI ARCHIVO CLIENTS EXISTE, INICIA LA APERTURA DEL MISMO
    try:
        with open(CLIENTS, 'r', newline='') as file:
            read_csv = csv.DictReader(file, delimiter=',')
            qtyList = read_csv.fieldnames
            count = 0
            company = input("Ingrese el nombre de la Empresa: ")
            logging.info(f"El usuario ingresó {company} como nombre de empresa a buscar.")

            # INICIO BUCLE BUSQUEDA DE NOMBRE DE EMPRESA EN ARCHIVO CLIENTS  
            # EN CASO DE ENCONTRAR GUARDA UN CONTADOR DE USUARIOS DE LA 
            # EMPRESA
            for line in read_csv:
                name = line[qtyList[0]]
                adress = line[qtyList[1]]
                doc = line[qtyList[2]]
                begin = line[qtyList[3]]
                mail = line[qtyList[4]]
                company = line[qtyList[5]]
                validateDocuments(doc)
                logging.info(f"Comprobación de Documentos en {CLIENTS} Exitosa.")
                email_verificator(mail)
                logging.info(f"Comprobación de email en {CLIENTS} Exitosa.")
                validateEmptyFields (name, adress, begin, company)
                logging.info(f"Comprobación de Nombre, Dirección, Fecha de Alta y Nombre de Empresa en {CLIENTS} Exitosa.")
                if company in line[qtyList[5]]:
                    count += 1
                    companyName = line[qtyList[5]]
                       
            print("=================================================================")
            print(f" Empresa: {companyName} \n Tiene {count} Usuarios")
            logging.info(f"Empresa {company} como nombre de empresa a buscar.")
            file.seek(0)

            # INICIO BUCLE BUSQUEDA DE USUARIOS DE LA EMPRESA. POSTERIORMENTE 
            # SE IMPRIME TODO EL LISTADO DETALLADO
            for line in read_csv:
                if company in line[qtyList[5]]:
                    print("=================================================================")
                    print(f" Nombre: {line[qtyList[0]]} \n Dirección: {line[qtyList[1]]} \n Documento: {line[qtyList[2]]} \n Fecha de Alta: {line[qtyList[3]]} \n Correo Electrónico: {line[qtyList[4]]} \n Empresa: {line[qtyList[5]]}")
    except IOError:
        print(f"Lo sentimos, el Archivo {CLIENTS} no existe.")
        logging.error("El usuario ingresó {CLIENTS} como nombre de Archivo de Clientes, el cual NO EXISTE.")

def DebtQtySearch():
    logging.info(f"Iniciando la Búsqueda del Monto por Empresa.")
    CLIENTS = input("Ingrese el nombre del Registro de Clientes: ") + ".csv"
    logging.info(f"El usuario ingresó {CLIENTS} como nombre del Archivo de Clientes.")
    TRAVELS = input("Ingrese el nombre del Registro de Viajes: ") + ".csv"
    logging.info(f"El usuario ingresó {TRAVELS} como nombre del Archivo de Viajes.")

            # SI ARCHIVOS CLIENTS y TRAVELS EXISTEN, INICIA LA APERTURA DE  
            # LOS MISMOS
    try:
        with open(CLIENTS, 'r', newline='') as fileOne, open(TRAVELS, 'r', newline='') as fileTwo:
            read_csv_one = csv.DictReader(fileOne, delimiter=',')
            companyList = read_csv_one.fieldnames
            read_csv_two = csv.DictReader(fileTwo, delimiter=',')
            qtyTravels = read_csv_two.fieldnames
            documentList = []
            company_input = input("Ingrese el nombre de la Empresa: ")
            logging.info(f"El usuario ingresó {company_input} como Empresa a buscar.")
            money = 0

            # INICIO BUCLE BUSQUEDA NOMBRE DE EMPRESA EN ARCHIVO CLIENTS, 
            # LUEGO GUARDA LISTADO DE TODOS LOS DOCUMENTOS DE LOS USUARIOS 
            # DE DICHA EMPRESA 
            for line in read_csv_one:
                name = line[companyList[0]]
                adress = line[companyList[1]]
                doc = line[companyList[2]]
                begin = line[companyList[3]]
                mail = line[companyList[4]]
                company = line[companyList[5]]
                validateDocuments(doc)
                logging.info(f"Comprobación de Documentos en {CLIENTS} Exitosa.")
                email_verificator(mail)
                logging.info(f"Comprobación de email en {CLIENTS} Exitosa.")
                validateEmptyFields (name, adress, begin, company)
                logging.info(f"Comprobación de Nombre, Dirección, Fecha de Alta y Nombre de Empresa en {CLIENTS} Exitosa.")
                if company_input in line[companyList[5]]:
                    documentList.append(line[companyList[2]])
                    companyName = line[companyList[5]]
                    logging.info(f"Empresa {company_input} encontrada como {companyName} en {CLIENTS}")
                
            # INICIO BUCLE BUSQUEDA DE DOCUMENTOS DE LOS USUARIOS DE LA 
            # EMPRESA EN ARCHIVO TRAVELS
            for line in read_csv_two:
                begin = line[qtyTravels[1]]
                price = line[qtyTravels[2]]
                validateDecimals(price)
                logging.info(f"Comprobación de Decimales en {TRAVELS} Exitosa.")
                validateEmptyFieldsTravels(begin)
                logging.info(f"Comprobación de Fecha en {TRAVELS} Exitosa.")
                for docs in documentList:
                    if docs in line[qtyTravels[0]]:
                        money += float(line[qtyTravels[2]])
                        logging.info(f"Se informa Cantidad de Usuarios de Empresa: {companyName} encontrados en {TRAVELS}")
            print(f" Empresa: {companyName} \n Deuda: ${money}")
            logging.info(f"Se informa Deuda NO Registrada de {companyName}")
    except IOError as e:
        print(f"Lo sentimos, el Archivo no existe. \n {e}")
        logging.error("El usuario ingresó el nombre del Archivo de Clientes y/o del Archivo de Viajes INCORRECTO.")

def TotalTripsSearch():
    logging.info(f"Iniciando la Búsqueda del Total de Viajes por Número de Documento.")
    CLIENTS = input("Ingrese el nombre del Registro de Clientes: ") + ".csv"
    logging.info(f"El usuario ingresó {CLIENTS} como nombre del Archivo de Clientes.")
    TRAVELS = input("Ingrese el nombre del Registro de Viajes: ") + ".csv"
    logging.info(f"El usuario ingresó {TRAVELS} como nombre del Archivo de Viajes.")

            # SI ARCHIVOS CLIENTS y TRAVELS EXISTEN, INICIA LA APERTURA Y 
            # POSTERIOR LECTURA DE LOS MISMOS
    try:
        with open(CLIENTS, 'r', newline='') as fileOne, open(TRAVELS, 'r', newline='') as fileTwo:
            read_csv_one = csv.DictReader(fileOne, delimiter=',')
            companyList = read_csv_one.fieldnames
            read_csv_two = csv.DictReader(fileTwo, delimiter=',')
            qtyTravels = read_csv_two.fieldnames
            document = input("Ingrese el Documento que desea buscar: ")
            logging.info(f"Se ingresó el Documento {document} para buscar en el archivo {CLIENTS}")
            count = 0
            money = 0

            # INICIO BUCLE BUSQUEDA DOCUMENTO EN ARCHIVO CLIENTS
            for user in read_csv_one:
                name = user[companyList[0]]
                adress = user[companyList[1]]
                doc = user[companyList[2]]
                begin = user[companyList[3]]
                mail = user[companyList[4]]
                company = user[companyList[5]]
                validateDocuments(doc)
                logging.info(f"Comprobación de Documentos en {CLIENTS} Exitosa.")
                email_verificator(mail)
                logging.info(f"Comprobación de email en {CLIENTS} Exitosa.")
                validateEmptyFields (name, adress, begin, company)
                logging.info(f"Comprobación de Nombre, Dirección, Fecha de Alta y Nombre de Empresa en {CLIENTS} Exitosa.")
                if document in user[companyList[2]]:
                    print("=================================================================")
                    print(f" Nombre: {user[companyList[0]]} \n Dirección: {user[companyList[1]]} \n Documento: {user[companyList[2]]} \n Fecha de Alta: {user[companyList[3]]} \n Correo Electrónico: {user[companyList[4]]} \n Empresa: {user[companyList[5]]}")
                    print("=================================================================")
                    logging.info(f"{document} encontrado en {CLIENTS} con éxito.")
                                
            # INICIO BUCLE BUSQUEDA DOCUMENTO EN ARCHIVO TRAVELS    
            for line in read_csv_two:
                logging.info(f"Se inicia la búsqueda del Documento {document} en el archivo {TRAVELS}")
                begin = line[qtyTravels[1]]
                price = line[qtyTravels[2]]
                validateDecimals(price)
                logging.info(f"Comprobación de Decimales en {TRAVELS} Exitosa.")
                validateEmptyFieldsTravels(begin)
                logging.info(f"Comprobación de Fecha en {TRAVELS} Exitosa.")
                if document in line[qtyTravels[0]]:
                    count += 1
                    money += float(line[qtyTravels[2]])
                    logging.info(f"{document} en {TRAVELS} encontrado con éxito.")
            print (f" Cantidad de Viajes: {count}. \n Deuda Total: ${money}")
            print("=================================================================")
            logging.info(f"Se informa Cantidad de viajes de Documento: {document}.")
            fileTwo.seek(0)

            # INICIO BUCLE BUSQUEDA DOCUMENTO EN ARCHIVO TRAVELS PARA
            # IMPRIMIR TODOS LOS VIAJES
            for user in read_csv_two:
                if document in user[qtyTravels[0]]:
                    print (f" Documento: {user[qtyTravels[0]]} \n Fecha: {user[qtyTravels[1]]} \n Monto: ${user[qtyTravels[2]]} ")
                    print("=================================================================")
                    logging.info(f"Se informa los viajes realizados por {document}.")
    except IOError as e:
        print(f"Lo sentimos, el Archivo no existe. \n {e}")
        logging.error("El usuario ingresó el nombre del Archivo de Clientes y/o del Archivo de Viajes INCORRECTO.")
        
menu()