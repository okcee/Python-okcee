'''
Ejemplo Algoritmo Logarítmico O(log x): Búsqueda binaria
Estos algoritmos indican que el tiempo es menor que el tamaño de los datos de entrada. No importa indicar la base del logaritmo.
Cómo funciona la búsqueda binaria
La búsqueda binaria funciona dividiendo repetidamente el rango de búsqueda por la mitad. Esto es muy eficiente para listas ordenadas, ya que reduce el número de comparaciones necesarias para encontrar un elemento
'''

def busqueda_binaria(a, x, low, high):
    """
    Función que implementa la búsqueda binaria en una lista ordenada.

    Args:
        a: La lista ordenada en la que se busca.
        x: El elemento que se busca.
        low: El índice inferior del rango de búsqueda.
        high: El índice superior del rango de búsqueda.

    Returns:
        El índice del elemento encontrado, o -1 si no se encuentra.
    """
    ans = -1  # Inicializa la respuesta a -1 (no encontrado)

    # Caso base: si el rango de búsqueda está vacío, el elemento no está presente
    if low == high:
        ans = -1
    else:
        # Calcula el índice medio del rango de búsqueda
        mid = (low + ((high - low) // 2))

        # Si el elemento buscado es menor que el elemento medio,
        # busca en la mitad izquierda del rango
        if x < a[mid]:
            ans = busqueda_binaria(a, x, low, mid)
        # Si el elemento buscado es mayor que el elemento medio,
        # busca en la mitad derecha del rango
        elif x > a[mid]:
            ans = busqueda_binaria(a, x, mid + 1, high)
        # Si el elemento buscado es igual al elemento medio,
        # se encontró el elemento
        else:
            ans = mid

    return ans  # Devuelve el índice del elemento encontrado, o -1 si no se encontró

# Ejemplo de uso
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
elemento_buscado = 23
indice = busqueda_binaria(lista_ordenada, elemento_buscado, 0, len(lista_ordenada))
print(f"El elemento {elemento_buscado} se encuentra en el índice {indice}")

# Resultado: El elemento 23 se encuentra en el índice 5

