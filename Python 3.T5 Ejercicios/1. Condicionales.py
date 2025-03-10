'''Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.'''

try:
    numero = int(input("Introduce un número entero: "))
    print("El número introducido es:", numero)
    suma = (numero*(numero+1))/2
    print("La suma de los números primeros enteros es:", numero)
except ValueError:
    print("Error: Debes introducir un número entero válido.")
