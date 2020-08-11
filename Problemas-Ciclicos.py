#!/usr/bin/python3
""" 1 - Calcular el promedio de un alumno que tiene 7 
calificaciones en la materia Laboratorio."""

cantidadCalificaciones = int(input("Ingrese la cantidad de notas: "))
suma = 0
calificaciones = []

for i in range(1, cantidadCalificaciones + 1):
    calificacion = float(input(f"Ingrese la calificacion {i}:"))
    calificaciones.append(calificacion)
    suma += calificacion

promedio = suma / cantidadCalificaciones

print(f"Su promedio es {promedio}")

""" 2 - Leer 20 numeros e imprimir cuantos son positivos, 
cuantos negativos y cuantos son cero."""

def cantidadNumeros():
    cantidad = int(input("Ingrese la cantidad de numeros: "))
    positivos = 0
    negativos = 0
    ceros = 0
    for i in range(1, cantidad + 1):
        numeros = int(input(f"Ingrese el numero {i}: "))
        cantidad += numeros
        if numeros > 0:
            positivos += 1
        elif numeros < 0:
            negativos += 1
        else:
            ceros += 1
    print(
        f"Hay {positivos} numeros Positivos, {negativos} numeros negativos y {ceros} son cero."
    )
    return ceros, negativos, positivos

cantidadNumeros()

""" 3 - Suponga que se tiene un conjunto de calificaciones 
de un grupo de 40 alumnos. Realizar un algoritmo para 
calcular la calificacion media y la calificacion mas baja 
de todo el grupo."""

alumnos = int(input("Ingrese la cantidad de alumnos: "))
suma = 0
calificaciones = []

for alumno in range(1, alumnos + 1):
    calificacion = float(input(f"Ingrese la calificacion {alumno}:"))
    calificaciones.append(calificacion)
    suma += calificacion

calificacionMedia = suma / alumnos
calificacionBaja = min(calificaciones)

print(f"La calificacion media es de {calificacionMedia}")
print(f"La calificacion mas baja es de {calificacionBaja}")

""" 4 - Calcular e imprimir la tabla de multiplicar de un 
numero cualquiera. Imprimir el multiplicando, el 
multiplicador y el producto."""

base = int(input("Ingrese el numero a multiplicar: "))

for i in range(1, 101):
    print(f"{base} x {i} = {i * base}")

""" 5 - En un centro de verificacion de automoviles se 
desea saber el promedio de puntos contaminantes de los 
primeros 25 automoviles que lleguen.
Asimismo se desea saber los puntos contaminantes del carro 
que menos contamino y del que mas contamino."""

def contaminantes():
    promedio = 0
    mas_contaminante = 0
    auto_mas_contaminante = 0
    menos_contaminante = 99999
    auto_menos_contaminante = 0
    for auto in range(1, 26):
        puntos_contaminantes = float(
            input(f"Ingrese los puntos contaminantes del auto {auto}: ")
        )

        promedio += puntos_contaminantes

        if puntos_contaminantes >= mas_contaminante:
            mas_contaminante = puntos_contaminantes

        if puntos_contaminantes <= menos_contaminante:
            menos_contaminante = puntos_contaminantes

    promedio = promedio / 25
    print(
        f"El promedio de contaminacion es de {promedio}, el que mas contamino fue {mas_contaminante} y el que menos contamino fue {menos_contaminante}"
    )

contaminantes()

""" 6 - Un entrenador le ha propuesto a un atleta recorrer 
una ruta de cinco Kilometros durante 10 dias, para 
determinar si es apto para la prueba de 5 Kilometros o debe 
buscar otra especialidad. 
Para considerarlo apto debe cumplir por lo menos una de las 
siguientes condiciones:
* Que en ninguna de las pruebas haga un tiempo mayor a 16 
minutos.
* Que al menos en una de las pruebas realice un tiempo menor 
a 13 minutos.
* Que su promedio de tiempos sea menor o igual a 15 minutos.
"""

veces = 10
veces_mayor_16 = 0
veces_menos_13 = 0
prom = 0
dia_actual = 1

while dia_actual <= veces:
    tiempo_prueba = int(
        input(f"Ingrese el tiempo tardado en la prueba para el dia {dia_actual}: ")
    )
    if tiempo_prueba > 16:
        veces_mayor_16 += 1
    if tiempo_prueba < 13:
        veces_menos_13 += 1

    prom += tiempo_prueba

    dia_actual += 1
prom = prom / veces
if prom <= 15 or veces_mayor_16 == 0 or veces_menos_13 >= 1:
    print(
        f"Es apto para los 5km, su promedio es de {prom}, tiene {veces_mayor_16} veces tiempo mayor a 16 mins y {veces_menos_13} veces tiempo menor a 13 mins."
    )
else:
    print(
        f"Lo lamento, no es apto, su promedio es de {prom}, tiene {veces_mayor_16} veces tiempo mayor a 16 mins y {veces_menos_13} veces tiempo menor a 13 mins."
    )

""" 7 - Una compañia de seguros tiene contratados a n 
vendedores. Cada uno hace tres ventas a la semana. Su 
politica de pagos es que un vendedor recibe un sueldo base, 
y un 10% extra por comisiones de sus ventas. 
El gerente de su compañia desea saber cuanto dinero obtendra 
en la semana cada vendedor por concepto de comisiones por 
las tres ventas realizadas, y cuanto tomando en cuenta su 
sueldo base y sus comisiones."""

sueldo = int(input("Ingrese el sueldo base del vendedor: "))
ventas = int(input("Ingrese la cantidad de ventas: "))
comisiones = (ventas * 0.10) * sueldo
total = sueldo + comisiones
print(f"Usted vendio {ventas} unidades, su comision es de {comisiones}")
print(f"El Saldo final a retirar es {total}")

""" 8 - Determinar cuantos hombres y cuantas mujeres se 
encuentra en un grupo de n personas, suponiendo que los datos 
son extraidos alumno por alumno."""

def agregar():
    cantidadPersonas = int(input("Ingrese la cantidad de personas: "))
    hombres = 0
    mujeres = 0
    for i in range(1, cantidadPersonas + 1):
        sexo = input(f"Ingrese el sexo de la persona numero {i}: ")
        if sexo == "hombre":
            hombres += 1
        elif sexo == "mujer":
            mujeres += 1
        cantidadPersonas += 1
    print (f"Hay {mujeres} Mujeres y {hombres} Hombres")

agregar ()

""" 9 - El departamento de seguridad publica y transito del 
D.F. desea saber, de los n autos que entran a la ciudad de 
Mexico, cuantos entran con calcomania de cada color. 
Conociendo el ultimo digito de la placa de cada automovil se 
puede determinar el color de la calcomania utilizando la 
siguiente relacion:
* Dígito 1 o 2 = Color Amarilla
* Dígito 3 o 4 = Color Rosa
* Dígito 5 o 6 = Color Roja
* Dígito 7 o 8 = Color Verde
* Dígito 9 o 0 = Color Azul
"""

autos = int(input("Ingrese la cantidad de autos: "))
suma = 0
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
total = 0
for i in range(1, autos +1):
    digito = int(input(f"Ingrese el ultimo dígito de la patente del vehiculo {i}:"))
    if digito == 1 or digito == 2:
        amarillo += 1
    elif digito == 3 or digito == 4:
        rosa += 1
    elif digito == 5 or digito == 6:
        roja += 1
    elif digito == 7 or digito == 8:
        verde += 1
    elif digito == 9 or digito == 0:
        azul += 1
    total += autos
print (f"Entraron a la ciudad {amarillo} Autos con Calcomanía Amarilla")
print (f"Entraron a la ciudad {azul} Autos con Calcomanía Azul")
print (f"Entraron a la ciudad {roja} Autos con Calcomanía Roja")
print (f"Entraron a la ciudad {rosa} Autos con Calcomanía Rosa")
print (f"Entraron a la ciudad {verde} Autos con Calcomanía Verde")

""" 10 - Obtener el promedio de calificaciones de un grupo 
de n alumnos."""

cantidadAlumnos = int(input("Ingrese la cantidad de Alumnos: "))
suma = 0
calificaciones = []

for i in range(1, cantidadCalificaciones + 1):
    calificacion = float(input(f"Ingrese la calificacion {i}:"))
    calificaciones.append(calificacion)
    suma += calificacion

promedio = suma / cantidadAlumnos

print(f"El promedio de calificaciones de los alumnos es {promedio}")

""" 11 - Calcular el factorial de un numero ingresado."""

from math import factorial
numero = int(input("Ingrese el número deseado: "))

print (f" El número factorial de {numero} es {factorial(numero)}")

""" 12 - Una persona desea invertir su dinero en un banco, 
el cual le otorga un 2% de interes.
¿Cual sera la cantidad de dinero que esta persona tendra al 
cabo de un año si la ganancia de cada mes es reinvertida?"""

from math import pow 

capital = int(input("Ingrese el capital a invertir: "))
interes = 0.02
total = capital * (pow( (1 + interes), 12))

print (f"El total al cabo de un año es de: ${total}")

""" 13 - Encontrar el menor valor de un conjunto de n 
números dados."""

conjuntoNumeros = int(input("Ingrese la cantidad de numeros: "))
total = []
for i in range(1, conjuntoNumeros + 1):
    numero = int(input(f"Ingrese el valor numero {i}: "))
    conjuntoNumeros += 1
    total.append(numero)

menor = min(total)

print (menor)

""" 14 - Encontrar el mayor valor de un conjunto de n
numeros dados."""

conjuntoNumeros = int(input("Ingrese la cantidad de numeros: "))
total = []
for i in range(0, conjuntoNumeros):
    numero = int(input(f"Ingrese el valor del numero {i}: "))
    conjuntoNumeros += 1
    total.append(numero)

mayor = max(total)

print (mayor)
