#!/usr/bin/python3
""" 1 - Leer un precio e imprimir por pantalla el precio final con IVA (21%)"""
precio = int(input("Indique un Numero:"))
precioIva = precio * 1.21

print(f"El precio ingresado es {precioIva}")

""" 2 - Leer tres numeros e imprimir el promedio de los mismos."""

primerNumero = int(input("Indique un Numero:"))
segundoNumero = int(input("Indique un Numero:"))
tercerNumero = int(input("Indique un Numero:"))
promedio = (primerNumero + segundoNumero + tercerNumero)/3
print(f"El Promedio es: {promedio}")

""" 3 - Leer dos numeros e imprimir el mayor de ambos numeros."""

A = int(input("ingrese un numero"))
B = int(input("ingrese otro numero"))
if A == B:
    print(f"{A} y {B} son iguales")
elif A > B:
    print (f"{A} es mayor a {B}")
else:
    print (f"{B} es mayor a {A}")

""" 4 - Leer un numero e imprimir un mensaje que indique si el numero es par o no."""

numero = int(input("Indique un número: "))

if numero % 2 == 0:
    print (f"el {numero} es par")
else:
    print (f"el {numero} es impar")

""" 5 - Generar un algoritmo que pida un numero al usuario hasta que el numero ingresado sea negativo."""

num = int(input("Ingrese un número: "))

while num >= 0:
    num = int(input("Ingrese nuevamente un número: "))
print("Programa terminado")