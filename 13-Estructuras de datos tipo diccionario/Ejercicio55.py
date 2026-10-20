'''Desarrollar una aplicación que nos permita crear un
diccionario inglés/castellano. La clave es la palabra en
inglés y el valor es la palabra en castellano. Crear las
siguientes funciones:
- Cargar el diccionario.
- Listado completo del diccionario.
- Ingresar por teclado una palabra en inglés y si existe en
el diccionario mostrar su traducción.'''


def cargar_diccionario():
    # 1. Creamos el diccionario vacío (la "cajonera")
    diccionario = {}

    # 2. Hacemos un bucle que se repita exactamente 4 veces
    for i in range(4):
        print(f"--- Palabra {i + 1} de 4 ---")

        # Pedimos los dos datos
        ingles = input("Introduce la palabra en inglés: ")
        castellano = input("Introduce la traducción en castellano: ")

        # Guardamos en la etiqueta [ingles] el valor castellano
        diccionario[ingles] = castellano
        print("¡Guardada!\n")

    # 3. Muy importante: devolver el diccionario lleno
    return diccionario

def listado_dicc():
    pass
