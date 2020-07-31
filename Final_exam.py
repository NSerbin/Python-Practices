#!/usr/bin/python3
""" 1) Realizar una función que permita la carga de n alumnos
se deberá preguntar el nombre completo y  3 notas.
Las notas deben estar comprendidas entre 0 y 10.
Devolver el listado de alumnos. """

def ingresoNotas():
    alumno = []
    salir = ""

    while salir != "si":
        totalidad = {}
        notas = []
        nota = 0
        totalidad["nombre"] = input("Ingrese el Nombre Completo del alumno: ")
        nota = int(input("Ingrese la Nota del Primer Parcial: "))
        if nota >= 0 and nota <= 10: 
            notas.append(nota)
        else:
            while True: #utilizado para no volver al 1er bucle while
                nota = int(input("Ingrese Nuevamente la nota del Primer Parcial, debe ser del 0 al 10"))
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                    break
        nota = 0
        nota = int(input("Ingrese la nota del Segundo Parcial: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            while True:
                nota = int(input("Ingrese Nuevamente la nota del Segundo Parcial, debe ser del 0 al 10"))
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                    break
        nota = 0
        nota = int(input("Ingrese la nota del Tercer Parcial: "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            while True:
                nota = int(input("Ingrese Nuevamente la nota del Tercer Parcial, debe ser del 0 al 10"))
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                    break
        totalidad["notas"] = notas
        salir = input("Desea terminar de ingresar alumnos? si/no: ")
        alumno.append(totalidad)
    return alumno

alumnos = ingresoNotas()

""" 2) Definir una función que dado un listado de alumnos evalúe 
cuántos aprobaron y cuantos desaprobaron, teniendo en cuenta que 
se aprueba con 4. La nota será el promedio de las 3 notas para 
cada alumno. """
def buscadorNotas (listado):
    aprobados = 0
    desaprobados = 0
    for alumno in listado:
        total = 0
        for nota in alumno["notas"]:
            total += nota
            alumno["promedio"] = total/3
    for alumno in listado:
        if alumno["promedio"] >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    return listado

promIndividual = buscadorNotas(alumnos)

""" 3) Informar el promedio de nota del curso total.  """
from numpy import mean #modulo encargado de hacer promedio

def promedios(listado):
    notas = mean([alumno["notas"] for alumno in alumnos])
    print(f"El curso tiene {notas} de Promedio Total.")
    return notas

promedios(promIndividual)

""" 4) Realizar una función que indique quien tuvo el promedio
más alto y quien tuvo la nota promedio más baja. """

def mayorMenor(listado):
    mayor = listado[0]
    menor = listado[0]
    for alumno in listado:
        if alumno["promedio"] > mayor["promedio"]:
            mayor = alumno
        if alumno["promedio"] < menor["promedio"]:
            menor = alumno
    print(f"El promedio más alto fue {mayor['promedio']} y lo obtuvo {mayor['nombre']}")
    print(f"El promedio mas bajo fue {menor['promedio']} y lo obtuvo {menor['nombre']}")
    return mayor, menor

mayorMenor(promIndividual)

""" 5) Realizar una función que permita buscar un alumno por nombre,
siendo el nombre completo o parcial,  y devuelva una lista con 
los n alumnos que concuerden con ese nombre junto con todos sus 
datos, incluido el promedio de sus notas.
Por ejemplo : 
Entrada: Juan
Salida: [{"nombre": "Juan Perez", "notas": [ 2, 5, 9], "promedio": 5.33},
 {"nombre": "Juana Vega", "notas": [ 5, 5, 6], "promedio": 5.33}] """

def buscadorNombre(listado):
    encontrado = []
    nombreCompleto =  input("Ingrese el nombre del alumno: ")
    for alumno in listado:
        info = alumno["nombre"].split()
        for nombres in info:
            if nombreCompleto == nombres:
                encontrado.append(alumno)
    return encontrado
print (buscadorNombre(promIndividual))















 