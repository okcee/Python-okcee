# Operadores
Python sigue reglas de precedencia similares a las matemáticas:
- Paréntesis: Los paréntesis tienen la máxima precedencia. Se evalúa primero lo que está dentro de los paréntesis.
- Potencias: Las potencias (**) se evalúan de derecha a izquierda.
- Multiplicación, división, módulo y división entera: Estos operadores tienen la misma precedencia y se evalúan de izquierda a derecha.
- Suma y resta: Estos operadores tienen la misma precedencia y se evalúan de izquierda a derecha.
- Comparaciones: Operadores como ==, !=, <, >, <=, >= se evalúan después de las operaciones aritméticas.
- Operadores lógicos: and, or y not se evalúan al final.

## Tabla de operadores
Operadores de menor a mayor precedencia (se refiere al orden en que se evalúan las expresiones que contienen múltiples operadores.)
| Operador | Descripción |
|---|---|
| `yield x` | Protocolo de generadores “send” |
| `lambda args: expresión` | Función anónima |
| `x if y else z` | Selección ternaria (retorna x si y es cierta) |
| `x or y` | OR lógico (y es evaluada sólo si x es falsa) |
| `x and y` | AND lógico (y es evaluada sólo si x es verdadera) |
| `not x` | Negación Lógica |
| `x in y, x not in y` | Operadores de membresía |
| `x is y, y is not y` | Operadores de identidad |
| `x < y, x<= y, x > y, x >= y` | Comparación de magnitudes. Set, subset y superset |
| `x == y, x != y` | Operadores de igualdad |
| `x | y` | Bit a bit (bitwise) OR. Unión de sets (conjuntos) |
| `x ^ y` | Bitwise XOR. Diferencia simétrica de sets |
| `x & y` | Bit a bit AND. Intersección de sets (conjuntos) |
| `x << y, x >> y` | Desplazamiento de x en y bits a izquierda y derecha |
| `x + y` | Adición. Concatenación |
| `x - y` | Substración. Diferencia entre sets (conjuntos) |
| `x * y` | Multiplicación. Repetición |
| `x % y` | Resto de la división |
| `x / y` | División real (verdadera) |
| `x // y` | División truncada |
| `-x, +x` | Negación. Identidad |
| `~x` | Negación Bit a bit |
| `x ** y` | Potencia (exponenciación) |
| `x[i]` | Indexado (secuencias, mapeados, otros) |
| `x[i:j:k]` | Troceado (slicing) |
| `x(...)` | Llamada (función, método, clase, etc.) |
| `x.attr` | Referencia a un atributo |
| `(...)` | Tupla, expresión, expresión de generador |
| `[...]` | Lista, lista por comprensión |
| `{...}` | Diccionario, Set, comprensión de diccionarios y sets |