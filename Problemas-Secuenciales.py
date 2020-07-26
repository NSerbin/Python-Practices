#!/usr/bin/python3
""" 1 - Suponga que un individuo desea invertir su capital en un banco y 
desean saber cuanto dinero ganara despues deun mes si el banco paga a razon 
de 2% mensual."""

capital = int(input("Ingrese el monto deseado:"))
interes_mensual = 0.02

def caja(dinero, interes):
    ganancia = dinero * interes
    final = ganancia + capital
    print (f"Las ganancias obtenidas en un mes son ${ganancia}")
    print (f"El total a Retirar es {final}")

caja(capital, interes_mensual)

""" 2 - Un vendedor recibe un sueldo base más un 10% extra por comision de 
sus ventas, el vendedor desea saber cuanto dinero obtendra por concepto de 
comisiones por las tres ventas que realiza en el mes y el total que recibira 
en el mes tomando en cuenta su sueldo base y comisiones."""

sueldo = int(input("Ingrese su Sueldo:"))
ventas = int(input("Ingrese la cantidad de ventas:"))
comision = ventas * (sueldo * 0.10)
final = sueldo + comision
print(f"Usted vendio {ventas} unidades, su comision es de {comision}")
print(f"El Saldo final a retirar es {final}")

""" 3 - Un alumno desea saber cual sera su calificacion final en la materia de 
Laboratorio.
Dicha Calificacion se compone de los siguientes porcentajes:
* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificacion del examen final.
* 15% de la calificacion de un trabajo final."""

calificacion_uno = float(input("Ingrese la Primer Nota del parcial:"))
calificacion_dos = float(input("Ingrese la Segunda Nota del parcial:"))
calificacion_tres = float(input("Ingrese la Tercer Nota del parcial:"))
examen_final = float(input("Ingrese la Nota del Final:"))
tp_final = float(input("Ingrese la Nota del TP Final:"))

def promedio():
    calificaciones = (calificacion_uno + calificacion_dos + calificacion_tres)/3
    tp = tp_final * 0.15
    examen = examen_final * 0.30
    total = tp + examen + calificaciones
    print (f"el 55% del promedio de los tres parciales es {calificaciones}")
    print (f"el 30% del promedio de los tres parciales es {examen}")
    print (f"el 15% del promedio de los tres parciales es {tp}")
    print (f"El promedio final es: {total}")

promedio()

""" 4 - Un profesor desea saber que porcentaje de hombres y que porcentaje de 
mujeres hay en un grupo de estudiantes. Se ingresa como dato el total de mujeres 
y total de hombres."""

estudiantesHombres = int(input("Ingrese la cantidad de Hombres:"))
estudiantesMujeres = int(input("Ingrese la cantidad de Mujeres:"))
total = estudiantesHombres + estudiantesMujeres
porM = (estudiantesMujeres * 100) / total
porH = (estudiantesHombres * 100) / total 
print(f"El porcentaje de Estudiantes Mujeres es: {porM} y el de hombres: {porH}")

""" 5 - Calcular el número de pulsaciones que una persona debe tener por cada 10 
segundos de ejercicio, si la formula es: pulsaciones = (220 - edad)/10."""

edad = int(input("Ingrese su edad:")
pulsaciones = (220 - edad) / 10
print("Sus pulsaciones son {pulsaciones}")

""" 6 - Tres personas deciden invertir su dinero para fundar una empresa. Cada una de 
ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte 
con respecto a la cantidad total invertida."""

personaUno = float(input("Ingrese el monto a invertir:"))
personaDos = float(input("Ingrese el monto a invertir:"))
personaTres = float(input("Ingrese el monto a invertir:"))
total = personaUno + personaDos + personaTres

porcentajeUno = (personaUno * 100) / total
porcentajeDos = (personaDos * 100) / total
porcentajeTres = (personaTres * 100) / total
print(f"El Primer Socio invirtió {personaUno} y su porcentaje es: {porcentajeUno}")
print(f"El Segundo Socio invirtió {personaDos} y su porcentaje es: {porcentajeDos}")
print(f"El Tercer Socio invirtió {personaTres} y su porcentaje es: {porcentajeTres}")

""" 7 - Un alumno desea saber cual sera su promedio general en las tres materias mas 
dificiles que cursa y cual sera el promedio que obtendra en cada una de ellas.
Estas materias se evaluan como se muestra a continuacion:
** La calificacion de Análisis se obtiene de la siguiente manera:
* Examen: 90%
* Promedio de Trabajos Practicos: 10%
* En esta materioa se pidio un total de tres TPs.
** La calificacion de Álgebra se obtiene de la siguiente manera:
* Examen: 80%
* Promedio de Trabajos Practicos: 20%
* En esta materioa se pidio un total de dos TPs.
** La calificacion de Programación se obtiene de la siguiente manera:
* Examen: 85%
* Promedio de Trabajos Practicos: 15%
* En esta materioa se pidio un total de tres TPs."""

def Analisis():
    examen = float(input("Ingrese la nota del examen:"))
    tpUno = float(input("Ingrese la nota del primer TP:"))
    tpDos = float(input("Ingrese la nota del segundo TP:"))
    tpTres = float(input("Ingrese la nota del tercer TP:"))
    promExam = examen * 0.90
    tpFinal = (tpUno + tpDos + tpTres) / 3
    promTP =  tpFinal * 0.10
    final = tpFinal + promTP
    print(f"El 90% de la nota del examen es: {promExam}")
    print(f"El 10% de los TPs es: {promTP}")
    print(f"Su nota final es: {final}")
    return final

def Algebra():
    examen = float(input("Ingrese la nota del examen:"))
    tpUno = float(input("Ingrese la nota del primer TP:"))
    tpDos = float(input("Ingrese la nota del segundo TP:"))
    promExam = examen * 0.80
    tpFinal = (tpUno + tpDos) / 3
    promTP = tpFinal * 0.20
    final = tpFinal + promTP
    print(f"El 80% de la nota del examen es: {promExam}")
    print(f"El 20% de los TPs es: {promTP}")
    print(f"Su nota final es: {final}")
    return final    

def Programacion():
    examen = float(input("Ingrese la nota del examen:"))
    tpUno = float(input("Ingrese la nota del primer TP:"))
    tpDos = float(input("Ingrese la nota del segundo TP:"))
    tpTres = float(input("Ingrese la nota del tercer TP:"))
    promExam = examen * 0.85
    tpFinal = (tpUno + tpDos + tpTres) / 3
    promTP = tpFinal * 0.15
    final = tpFinal + promTP
    print(f"El 85% de la nota del examen es: {promExam}")
    print(f"El 15% de los TPs es: {promTP}")
    print(f"Su nota final es: {final}")
    return final

notaUno = Analisis()
notaDos = Algebra()
notaTres = Programacion()
promedioFinal = (notaUno + notaDos + notaTres) / 3
print (f"Su promedio general es: {promedioFinal}")