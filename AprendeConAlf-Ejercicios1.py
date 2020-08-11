""" 1) Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por 
pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. """

name = input("Ingrese su nombre: ")
n = int(input("Ingrese la cantidad de veces que desea mostrar su nombre: "))

for nombre in range(1, n+1):
    print(name)

""" 2) Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
mayúsculas y <n> es el número de letras que tienen el nombre. """

nombre = input("Ingrese su nombre: ")
print (f"{nombre} tiene {len(nombre)} letras")

""" 3) Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los 
payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el 
peso total del paquete que será enviado."""

peso_payasos = 112
peso_muñecas = 75
cantidad_payasos = int(input("Ingrese la cantidad de Payasos a enviar: "))
cantidad_muñecas = int(input("Ingrese la cantidad de Muñecas a enviar: "))
envio = (peso_muñecas * cantidad_muñecas) + (peso_payasos * cantidad_payasos)
print (f" El peso total del envio es: {envio} gr, de los cuales {peso_muñecas*cantidad_muñecas} gr son de Muñecas  y {peso_payasos*cantidad_payasos} gr son de Payasos.")


""" 4) Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha 
cumplido (desde 1 hasta su edad)."""

edad = int(input("Cuantos años tiene?"))
for i in range(edad):
    print (f"Has cumplido {i} años.")

""" 5) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
los números impares desde 1 hasta ese número separados por comas. """

numero = int(input("Ingrese un numero entero positivo: "))
for i in range (1, numero + 1, 2):
    print(f"{i}")

""" 6) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas. """

numero = int(input("Ingrese un numero entero positivo: "))
for i in range(numero, - 1, -1):
    print(f"{i}")

""" 7) Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura 
la inversión."""

inversion = int(input("Ingrese la cantidad deseada a invertir: "))
años = int(input("Ingrese la cantidad de años: "))
interes = int(input("Ingrese el interes anual: "))
for i in range(años):
    inversion *= 1 + interes /100
    print(f"Capital tras {años} años: {round(inversion,2)}")

""" 8) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido."""

n = int(input("Ingrese la altura del triangulo: "))
for i in range(n):
    print("*" *(i+1))

""" 9) Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

for i in range(1,11):
    for j in range(1,11):
        print (i*j, end="\t")
    print("")

""" 10) Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo con numeros."""

altura = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, altura +1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

""" 11) Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
número primo o no."""

numero = int(input("Ingrese un numero positivo mayor a 2: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(f"el {numero} es Primo")
else:
    print (f"El {numero} no es Primo")

""" 12) Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una 
las letras de la palabra introducida empezando por la última."""

palabra = input("Ingrese una palabra: ")
for i in range(-1, -1, -1):
    print(palabra[i])

""" 13) Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre 
por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Ingrese una Frase: ")
letra = input("Ingrese una Letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(f"La letra {letra} aparece {i} veces en la frase {frase}")
