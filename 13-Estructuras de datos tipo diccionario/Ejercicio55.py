'''Desarrollar una aplicación que nos permita crear un
diccionario inglés/castellano. La clave es la palabra en
inglés y el valor es la palabra en castellano. Crear las
siguientes funciones:
- Cargar el diccionario.
- Listado completo del diccionario.
- Ingresar por teclado una palabra en inglés y si existe en
el diccionario mostrar su traducción.'''


def cargar_diccionario()-> dict[str,str]:
    # 1. Creamos el diccionario vacío (la "cajonera")
    diccionario = {}

    # 2. Hacemos un bucle que se repita exactamente 4 veces
    for i in range(2):
        print(f"--- Palabra {i + 1} de 2 ---")

        # Pedimos los dos datos
        ingles = input("Introduce la palabra en inglés: ").strip().lower()
        castellano = input("Introduce la traducción en castellano: ").strip().lower()

        # Guardamos en la etiqueta [ingles] el valor castellano
        diccionario[ingles] = castellano
        print("¡Guardada!\n")

    # 3. Muy importante: devolver el diccionario lleno
    return diccionario

def listado_dicc(diccionario:dict[str,str]) -> None:
    print("Listado diccionario")
    for clave, valor in diccionario.items():
        print(f"Inglés: {clave:<8} | Español: {valor}")

def consultar_palabra(diccionario: dict[str, str]) -> None:
    palabra = input("¿Qué palabra quieres buscar?: ").strip().lower()
    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es '{diccionario[palabra]}'.")
    else:
        print(f"Lo siento, '{palabra}' no existe en el diccionario.")


diccionario = cargar_diccionario()
listado_dicc(diccionario)
consultar_palabra(diccionario)

