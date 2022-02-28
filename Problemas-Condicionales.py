#!/usr/bin/python3
""" 1 - En un Supermercado se hace una promocion, mediante la cual el cliente obtiene un 
descuento dependiendo de un numero que se escoge al azar.
* Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra
* Si es mayor o igual a 74 el descuento es del 20%. 
Obtener cuánto dinero se le descuenta."""

import random

numero = random.randint(0,100)
venta = float(input("Ingrese el valor de su compra:"))

if numero < 74:
    desc = (venta * 0.15)
    total = venta - desc
    print (f"Usted tiene un 15% de descuento en su compra. Se le debitaran ${desc}")
else:
    desc = venta - (venta * 0.20)
    total = venta - desc
    print (f"Usted tiene un 20% de descuento en su compra. Se le debitaran ${desc}")
print (f"El total de su factura es {total}")
""" 2 - Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos 
de ejercicio aerobico segun su genero. 
* Si es femenino : pulsaciones = (220 - edad)/10
* Si es masculino: pulsaciones = (210 - edad)/10."""

def Hombre():
    pulsaciones = (210 - edad)/10
    print("Por cada 10 segundos de ejercicio aeróbico sus pulsaciones deben ser de: {pulsaciones}")

def Mujer():
    pulsaciones = (220 - edad)/10
    print("Por cada 10 segundos de ejercicio aeróbico sus pulsaciones deben ser de: {pulsaciones}")

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo: ")
if sexo == "Mujer":
    Mujer()
elif sexo == "Hombre":
    Hombre()

""" 3 - Una compañia de seguros esta abriendo un departamento de finanzas y establecio un 
programa para captar clientes, que consiste en lo siguiente: 
* Si el monto por el que se efectua el seguro es menor que $50000 la cuota a pagar sera 
por el 3% del monto 
* Si el monto es mayor que $50000 la cuota a pagar sera el 2% del monto. 
La aseguradora desea determinar cual sera la cuota que debe pagar un cliente."""

valorAsegurado = int(input("Ingrese el monto de su vehiculo: "))

if valorAsegurado < 50000:
    seguro = valorAsegurado * 0.03
    print ("A Usted le corresponde el 3% del valor del vehiculo. Su cuota es de ${seguro}")
elif valorAsegurado >= 50000:
    seguro = valorAsegurado * 0.02
    print ("A Usted le corresponde el 2% del valor del vehiculo. Su cuota es de ${seguro}")

""" 4 - En una escuela privada la matricula de los alumnos se determina segun el numero de 
materias que cursan. El costo de todas las materias es el mismo. 
Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: 
* Si el promedio obtenido por un alumno en el ultimo periodo es mayor o igual a 9, se le hara
un descuento del 30% sobre la matricula y no se le cobrara el IVA.
* Si el promedio obtenido es menor que 9 debera pagar la matricula completa, la cual incluye 
el 10% de IVA. 
Obtener cuanto debe pagar un alumno."""

materias = int(input("Ingrese la cantidad de materias que desea cursar: "))
promedio = float(input("Ingrese su Promedio: "))
matricula = (materias * 750) * 1.10

if promedio >= 9:
    sinIva = materias * 750
    desc = sinIva * 0.30
    matricula = sinIva - desc
    print(f"Usted tiene un beneficio del 30% sobre el valor final y se le descontara el IVA, su nuevo valor es de {matricula}")
else:
    print(f"Usted debera abonar la matricula completa, su valor asciende a: ${matricula}")

""" 5 - El gobierno ha establecido el programa SAR (Sistema de Ahorro para el Retiro) que 
consiste en que los dueños de la empresa deben obligatoriamente depositar en una cuenta 
bancaria un porcentaje del salario de los trabajadores. 
Adicionalmente los trabajadores pueden solicitar a la empresa que deposite directamente una 
cuota fija o un porcentaje de su salario en la cuenta del SAR, la cual le sera descontada de 
su pago. 
Un trabajador que ha decidido aportar a su cuenta del SAR desea saber la cantidad total de 
dinero que estara depositado en esa cuenta cada mes, y el pago mensual que recibirá."""

sueldo = int(input("Ingrese su sueldo: "))
sar = sueldo * 0.05
total = sueldo - sar
aporteExtra = input("Desea adicionar un porcentaje de su salario? ")
if aporteExtra == "Si":
    extra = int(input("Cuanto desea que se le descuente ?"))
    descuento = (total * extra) / 100
    final = total - descuento
    print(f"Se le descontaran ${descuento} extras este mes. El sueldo a cobrar es ${final}")
else:
    print (f"El sueldo a cobrar es ${final}")

""" 6 - El gobierno desea reforestar un bosque que mide determinado numero de hectareas. 
*Si la superficie del terreno excede a 1 millon de metros cuadrados, entonces decidira 
sembrar de la siguiente manera:
70% de la Superficie = Pino
20% de la Superficie = Oyamel
10% de la Superficie = Cedro
*Si la superficie del terreno es menor o igual a 1 millon de metros cuadrados, entonces 
decidira sembrar de la siguiente manera:
50% de la Superficie = Pino
30% de la Superficie = Oyamel
20% de la Superficie = Cedro
El gobierno desea saber el número de pinos, oyameles y cedros que tendra que sembrar en 
el bosque, si se sabe que en 10m2 caben 8 pinos, en 15m2 caben 15 oyameles y en 18m2
caben 10 cedros. Tambien se sabe que una hectarea equivale a 10.000m2."""

superficie = int(input("Ingrese cantidad de hectareas del terreno: "))
superficiePinos = 8000
superficieOyameles = 10000
superficieCedro = 5555.55

if superficie > 100:
    pinos = (superficie * 0.70) * superficiePinos
    oyamel = (superficie * 0.20) * superficieOyameles
    cedro = (superficie * 0.10) * superficieCedro
    print(f"Se Plantaran {pinos} Pinos")
    print(f"Se Plantaran {oyamel} Oyameles")
    print(f"Se Plantaran {cedro} Cedros")
elif superficie <= 100:
    pinos = (superficie * 0.50) * superficiePinos
    oyamel = (superficie * 0.30) * superficieOyameles
    cedro = (superficie * 0.20) * superficieCedro
    print(f"Se Plantaran {pinos} Pinos")
    print(f"Se Plantaran {oyamel} Oyameles")
    print(f"Se Plantaran {cedro} Cedros")

""" 7 - En una fabrica de computadoras se planea ofrecer a los clientes un descuento que 
dependera del numero de computadoras que se compre. 
* Si las computadoras son menos de cinco se les dara un 10% de descuento sobre el total 
de la compra.
* Si el numero de computadoras es mayor o igual a cinco, pero menos de diez, se les 
otorga un 20% de descuento. 
* Si son diez o mas se les da un 40% de descuento.
El precio de cada computadora es de $1.600."""
venta = int(input("Ingrese la cantidad de unidades a vender: "))
valor = 1600
precio_lista = venta * valor

if venta < 5:
    desc = precio_lista * 0.10
    final = precio_lista - desc
    print(f"Se le descontaran ${desc} de la factura, su nuevo importe es {final}")
elif venta >= 5:
    desc = precio_lista * 0.20
    final = precio_lista - desc
    print(f"Se le descontaran ${desc} de la factura, su nuevo importe es {final}")
elif venta >= 10:
    desc = precio_lista * 0.40
    final = precio_lista - desc
    print(f"Se le descontaran ${desc} de la factura, su nuevo importe es {final}")

""" 8 - En un juego de preguntas a las que se responde: 
"Si" o "No" gana quien responda correctamente las tres preguntas. 
Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego.
Las preguntas son:
* ¿Colon descubrio america?
* ¿La independencia de Mexico fue en el año 1810?
* ¿The Doors fue un grupo de rock americano?"""

inicio = input("Desea empezar el juego de preguntas?")
if inicio == "Si":
    pregunta_uno = input("¿Colon descubrio america?")
    print("Correcto ! Puede seguir participando")
    if pregunta_uno == "Si":
        pregunta_dos = input("¿La independencia de Mexico fue en el año 1810?")
        print("Correcto ! Puede seguir participando")
        if pregunta_dos == "Si":
            pregunta_tres = input("¿The Doors fue un grupo de rock americano?")
            if pregunta_tres == "No":
                print ("Ganaste !")
            else:
                print("Incorrecto ! Juego Terminado !")
        else:
            print("Incorrecto ! Juego Terminado !")
    else:
        print("Incorrecto ! Juego Terminado !")        
else:
    print("Una lastima ! la proxima sera !")

""" 9 - Un proveedor de estereos ofrece un descuento del 10% sobre el precio sin IVA de 
algun aparato si este cuesta $2.000 o más. 
Ademas, independientemente de esto, ofrece un 5% de descuento si la marca es "YNOS". 
Determinar cuanto pagara, con IVA incluido, un cliente cualquiera por la compra de su 
aparato."""

marca = input("Ingrese la marca elegida: ")
precio = int(input("Ingrese el Precio del producto: "))

if precio >= 2000:
    descuento = precio * 0.10
    print(f"Usted tiene un 10% de descuento con un valor de ${descuento}")
    sinIVA = precio - descuento
    print(f"El Subtotal es: ${sinIVA}")
    precio_final = sinIVA * 1.21
    print(f"El total a pagar es: ${precio_final}, IVA incluido")
    if marca == "YNOS":
        descuento = precio * 0.10
        sinIVA = precio - descuento
        precio_final = sinIVA * 1.21
        YNOS = precio_final * 1.05
        print(f"Como su producto es de marca YNOS obtuvo un beneficio exclusivo, total a pagar: ${YNOS}")
else:
    precio_final = precio * 1.21
    print(f"El total a pagar es: ${precio_final}, IVA incluido")

""" 10 - Una fruteria ofrece las manzanas con descuento segun la siguiente tabla: 
* Si el peso es <= 2, el descuento es 0%
* Si el peso es > 2 y <= 5, el descuento es 10%
* Si el peso es > 5 y <= 10, el descuento es 15%
* Si el peso es > 10, el descuento es 20%
Determinar cuanto pagara una persona que compre manzanas en esa fruteria. """

precio = float(input("Ingrese el valor de las manzanas"))
peso = int(input("Ingrese la cantidad de Kilos a comprar: "))
if peso <= 2:
    total = precio * peso
    print (f"Usted no tiene descuento, el valor de su compra es de: ${total}.")
elif peso > 2 and peso <= 5:
    total = sub_total - (sub_total * 0.10)
    sub_total = (precio * peso)
    print (f"Usted tiene 10% de descuento, el valor de su compra es de: ${total}.")
elif peso > 5 and peso <= 10:
    total = sub_total - (sub_total * 0.15)
    sub_total = (precio * peso)
    print (f"Usted tiene 15% de descuento, el valor de su compra es de: ${total}.")
elif peso > 10:
    total = sub_total - (sub_total * 0.20)
    sub_total = (precio * peso)
    print (f"Usted tiene 20% de descuento, el valor de su compra es de: ${total}.")

""" 11 - El dueño de una empresa desea planificar las decisiones financieras que 
tomara en el siguiente año.
La manera de planificarlas depende de lo siguiente:
* Si actualmente su capital se encuentra con saldo negativo, pedira un prestamo 
bancario para que su nuevo saldo sea de $10.000.
* Si su capital tiene actualmente un saldo positivo pedira un prestamo bancario 
para tener un nuevo saldo de $20.000.
* Si su capital tiene actualmente un saldo superior a los $20.000, no pedira 
ningun prestamo.
Posteriormente repartira su presupuesto de la siguiente manera:
* $5.000 para computadoras
* $2.000 para mobiliario
* El resto, la mitad sera para la compra de insumos y la otra para otorgar 
incentivos al personal.
Desplegar que cantidades se destniaran para la compra de insumos e incentivos al 
personal y, en caso de que fuera necesario, a cuanto ascenderia la cantidad que 
se pediria al banco."""

capital = float(input("Ingrese su capital actual: "))

if capital < 0:
    prestamo = (capital * -1) + 10000
    print(f"Se le prestaron {prestamo} su nuevo saldo es de $10000")
elif capital > 0 and capital <20000:
    prestamo = 20000 - capital
    final = 20000
    print(f"Se le prestaron {prestamo} su nuevo saldo es de ${final}")
elif capital >= 20000:
    print("No es necesario pedir un prestamo.")
    computadoras = 5000
    mobiliario = 2000
    capital = capital - mobiliario - computadoras
    resto = capital / 2
    print (f"Se descontaran ${computadoras} para Computadoras del Capital.")
    print (f"Se descontaran ${mobiliario} para Mobiliario del Capital.")
    print (f"Su saldo final es de ${capital}")
    print (f"Se destinaran ${resto} para Insumos y ${resto} para Incentivos")

""" 12 - Tomando como base los resultados obtenidos en un laboratorio de analisis
clinicos, un medico determina si una persona tiene anemia o no, lo cual depende 
de su nivel de hemoglobina en la sangre, de su edad y de su sexo.
Si el nivel de hemoglobina que tiene una persona es menor que el rango que le 
corresponde, se determina su resultado como positivo y en caso contrario, 
como negativo. 
La tabla en la que el medico se basa para obtener el resultado es la siguiente:
* EDAD:   0 -      1 Mes   |  Hemoglobina: 13   - 26 g%
* EDAD: > 1 -  <=  6 Meses |  Hemoglobina: 10   - 18 g%
* EDAD: > 6 -  <= 12 Meses |  Hemoglobina: 11   - 15 g%
* EDAD: > 1 -  <=  5 Años  |  Hemoglobina: 11,5 - 15 g%
* EDAD: > 5 -  <= 10 Años  |  Hemoglobina: 12,6 - 15,5 g%
* EDAD: > 10 - <= 15 Años  |  Hemoglobina: 13   - 15,5 g%
* Mujeres       > 15 Años  |  Hemoglobina: 12   - 16 g%
* Hombres       > 15 Años  |  Hemoglobina: 14   - 18 g% """

hemoglobina = float(input("Ingrese la cantidad de Hemoglobina: "))
sexo = input("Ingrese el sexo: ")
edad = int(input("Es menor a 1 año ? "))
if edad == "Si":
    edad = int(input("Ingrese cuantos meses tiene: "))
    if edad == 0 and edad < 1:
        if hemoglobina < 13:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    elif edad > 1 and edad < 6:
        if hemoglobina < 10:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    if edad > 6 and edad < 12:
        if hemoglobina < 11:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
elif edad == "No":
    edad = int(input("Ingrese los años: "))
    if edad > 1 and edad < 5:
        if hemoglobina < 11.5:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    elif edad > 5 and edad < 10:
        if hemoglobina < 12.6:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    elif edad > 10 and edad < 15:
        if hemoglobina < 13:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    elif edad > 15 and sexo == "Mujer":
        if hemoglobina < 12:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")
    elif edad > 15 and sexo == "Hombre":
        if hemoglobina < 14:
            print("Su resultado es Positivo a Anemia.")
        else:
            print("Su resultado es Negativo a Anemia.")            

""" 13 - Una institucion educativa establecio un programa para estimular a los 
alumnos con buen rendimiento academico que consiste en lo siguiente:
* Si el promedio es de 9,5 o más y el alumno es del primer ciclo, entonces 
este podra cursar 55 unidades y se le hara un 25% de descuento.
* Si el promedio es mayor o igual a 9 pero menor que 9,5, y el alumno es del 
primer ciclo, entonces este podra cursar 50 unidades y se le hara un 10% de 
descuento.
* Si el promedio es mayor que 7 y menor que 9 y el alumno es del primer ciclo, 
este podra cursar 50 unidades y no tendra ningun descuento.
* Si el promedio es de 7 o menor, el numero de materias reprobadas es de hasta 3
y el alumno es del primer ciclo, entonces podra cursar 45 unidades y no tendra 
descuento.
* Si el promedio es de 7 o menor, el numero de materias reprobadas es de 4 o mas 
y el alumno es del primer ciclo, entonces podra cursar 40 unidades y no tendra 
ningun descuento.
* Si el promedio es mayor o igual a 9,5 y el alumno es del segundo ciclo, 
entonces podra cursar 25 unidades y se le hara un 20% de descuento.
* Si el promedio es menor de 9,5 y el alumno es del segundo ciclo, 
entonces podra cursar 25 unidades y no tendra descuento.
Obtener el total que tendrá que pagar un alumno si la matricula para alumnos del 
segundo ciclo es de $300 por cada cinco unidades y para alumnos del primer ciclo 
es de $180 por cada cinco unidades."""

promedio = float(input("Ingrese su Promedio: "))
ciclo = int(input("Ingrese el Ciclo al que pertenece: "))
materias = int(input("Ingrese la cantidad de Materias Reprobadas: "))

if promedio >= 9.5:
    unidades = 55
    descuento = 0.25
    matricula = ((unidades / 5) * 180) * descuento
    total = ((unidades / 5) * 180) - matricula
    print(f"Puede cursar {unidades} unidades")
    print(f"Tiene un 25% de descuento")
    print(f"El total a pagar de la matricula es de ${total}")
elif promedio >= 9 and promedio < 9.5:
    unidades = 50
    descuento = 0.10
    matricula = ((unidades / 5) * 180) * descuento
    total = ((unidades / 5) * 180) - matricula
    print(f"Puede cursar {unidades} unidades")
    print(f"Tiene un 10% de descuento")
    print(f"El total a pagar de la matricula es de ${total}")
elif promedio > 7 and promedio < 9:
    unidades = 50
    matricula = (unidades / 5) * 180
    print(f"Puede cursar {unidades} unidades")
    print(f"No tiene descuento disponible.")
    print(f"El total a pagar de la matricula es de ${matricula}")
elif promedio <= 7 and materias <= 3 and ciclo == 1:
    unidades = 45
    matricula = (unidades / 5) * 180
    print(f"Puede cursar {unidades} unidades")
    print(f"No tiene descuento disponible.")
    print(f"El total a pagar de la matricula es de ${matricula}")
elif promedio <= 7 and materias >= 4 and ciclo == 1:
    unidades = 40
    matricula = (unidades / 5) * 180
    print(f"Puede cursar {unidades} unidades")
    print(f"No tiene descuento disponible.")
    print(f"El total a pagar de la matricula es de ${matricula}")
elif promedio >= 9.5 and ciclo == 2:
    unidades = 25
    descuento = 0.20
    matricula = ((unidades / 5) * 300) * descuento
    total = ((unidades / 5) * 300) - matricula
    print(f"Puede cursar {unidades} unidades")
    print(f"Tiene un 20% de descuento")
    print(f"El total a pagar de la matricula es de ${total}")
elif promedio < 9.5 and ciclo == 2:
    unidades = 25
    total = (unidades / 5) * 300
    print(f"Puede cursar {unidades} unidades")
    print(f"No tiene descuento disponible.")
    print(f"El total a pagar de la matricula es de ${total}")