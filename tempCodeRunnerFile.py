genero = input("Ingrese el género del aspirante (mujer/hombre): ").strip().lower()
estado_civil = input("Ingrese el estado civil del aspirante (soltero/casado): ").strip().lower()
estatura = float(input("Ingrese la estatura del aspirante en metros: "))
edad = int(input("Ingrese la edad del aspirante: "))
salida = ""

# Evaluar estado civil
if estado_civil == "soltero":
    if genero == "mujer":
        if estatura > 1.60 and 20 <= edad <= 25:
            salida = "Apto"
        else:
            salida = "No es apto"
    elif genero == "hombre":
        if estatura > 1.65 and 18 <= edad <= 24:
            salida = "Apto"
        else:
            salida = "No es apto"
    else:
        salida = ""
else:
    salida = "No es apto"

# Imprimir resultado
if salida:
    print(f"El aspirante es {salida} para ingresar al ejército.")
else:
    print("Género no válido.")