""" 1) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla."""

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print (materias)

""" 2) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la 
lista.""" 

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materia in materias:
    print(f"Yo estudio {materia}")

""" 3) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario."""

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for materia in materias:
    nota = int(input(f"Ingrese la nota de {materia}: "))
    notas.append(nota)
for i in range(len(materias)):
    print("en", materias[i], "Has sacado", notas[i])

""" 4) Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y 
los muestre por pantalla ordenados de menor a mayor."""

loteria = []
for i in range(8):
    loteria.append(int(input("Ingrese los numeros ganadores: ")))
loteria.sort()
print(f"Los números ganadores son {loteria}")

""" 5) Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados 
por comas."""

lista = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    print(f"{(lista[-i])}", end=",")

""" 6) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final 
el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(materias)-1, -1, -1):
    nota = float(input(f"Ingrese la nota de {(materias[i])}: "))
    if nota >= 6:
        materias.pop(i)
print(f"Tienes que repetir {materias}")

""" 7) Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos 
de 3, y muestre por pantalla la lista resultante."""

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        alfabeto.pop(i -1)
print (alfabeto)

""" 8) Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

palabra = input("Ingrese una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
for vocal in vocales:
    contador = 0
    for letra in palabra:
        if letra == vocal:
            contador += 1
    print(f"La vocal {vocal} aparece {contador} veces.")