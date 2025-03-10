'''Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.'''
print ("¡Hola Mundo!")

'''Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.'''
s_var="¡Hola Mundo!"
print(s_var)

'''Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido'''
s_name=input("Por favor, introduce tu nombre: ") # Creo una variable
print("¡Hola ",s_name,"!") # Imprimo strings y la variable

'''Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
((3+2)/(2*5))^2'''
f_var=((3+2)/(2*5))**2
print(f_var)

'''Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

i_horas=int(input("¿Cuántas horas as trabajado? "))
f_coste=float(input("¿Cuánto es salario acordado por hora trabajada? "))
f_paga=i_horas*f_coste
print=(f"La paga que corresponde es igual a {f_paga}")

'''Ejercicio 6
Escribir un programa que lea un entero positivo, "n" , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta "n". La suma de los "n"  primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+1) / 2
'''

try:
    numero = int(input("Introduce un número entero: "))
    print("El número introducido es:", numero)
    suma = (numero*(numero+1))/2
    print("La suma de los números primeros enteros es:", numero)
except ValueError:
    print("Error: Debes introducir un número entero válido.")
