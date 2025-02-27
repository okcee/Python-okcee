'''Ventajas de utilizar las funciones:
    - Aumentan la reusabilidad de código y minimizan la redundancia (repetición)
    - Permiten la descomposición procedural
    - Permiten polimorfirsmo, es decir, en Python cada tipo de dato sabe cómo comportarse ante una gran variedad de operadores. Esto es directamente aplicable al uso de funciones
    - Es posible crear funciones dentro de funciones (Funciones anidadas)
    - En Python una función puede llamarse a sí misma, generando recursividad. Es importante evitar que esta sea infinita
    - Devolviendo múltiples valores simultáneamente con la sentencia return
    
'''
'''Sintaxis básica de una función en Python. La sintaxis necesaria para declarar una función es la siguiente:
def nombre_de_la_función(arg1, arg2, ...argN):
sentencias
return #El return es opcional'''
# Ejercicio 1: Realiza una función que realice la descomposición en factores de un número. Deberá devolver una lista con los factores de dicho número. Recordad que la descomposición en factores de un número consiste en hallar el conjunto de números primos cuya multiplicación dé dicho número como resultado. Pista: Lo primero que debe hacer la función es hallar todos los números primos inferiores al número en cuestión.
n = input("Introduce un número entero: ")
n = int(n)
def descomposicion_factores_primos(n):
    factores = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores
print("la descomposición en factores de {n} es:", descomposicion_factores_primos(n))

'''Reglas de ámbito:
Cuando se busca una variable, Python sigue la **regla LEGB**:  
- Local: Ámbito local de la función. *(Function Scope)*  
- Enclosing: Ámbito de las funciones envolventes (no local). *(Enclosing Scope)*  
- Global: Ámbito global del módulo. *(Module Scope)*  
- Built-in: Ámbito de los nombres incorporados'''
# Ejemplo 1: Ámbitos delas variables.
G = 'Esta variable es de ámbito Global'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
    def f3():
        print(E, G, sep = '\n')
    f2()
    f3()
f1()
'''Resultado:
L es local a f2
E también es local a f2
G también es local a f2
Esta variable es local a f1. Enclosing a f2
Esta variable es de ámbito Global'''

'''INMUTABLE = Ejemplo de si pasamos un objeto inmutable a una función que lo modifica internamente, el cambio afecta al exterior de la función'''
def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función.
'''Resultado:
7
5 10
'''


'''MUTABLE = Ejemplo de si pasamos un objeto mutable a una función que lo modifica internamente, el cambio afecta al exterior de la función'''
def minimo (L):
    L[0] = 1000 # Modificamos la lista en el interior
    return min (L)
L = [1, 2, 3]
print (L)
print (minimo (L)) # Modifica la lista aquí
print (L)
'''Resultado:
[1, 2, 3]
2
[1000, 2, 3]
'''