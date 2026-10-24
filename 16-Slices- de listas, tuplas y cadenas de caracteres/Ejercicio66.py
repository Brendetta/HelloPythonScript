'''Realizar un programa que contenga las siguientes funciones:
- Carga de una lista de 10 enteros.
- Recibir una lista y retornar otra con la primer mitad (se
sabe que siempre llega una lista con una cantidad par de
elementos)
- Imprimir una lista.'''


def cargar_lista()->list[int]:
    enteros = []
    for i in range(10):
        numero = int(input(f"{i +1}: "))
        enteros.append(numero)
    return enteros

def primer_mitad(lista: list[int]) -> list[int]:
    """Retorna una nueva lista con la primera mitad de los elementos recibidos."""
    mitad = len(lista) // 2
    return lista[:mitad]


def imprimir_lista(lista: list[int], mensaje: str = "Lista:") -> None:
    """Muestra los elementos de la lista en pantalla."""
    print(f"\n{mensaje}")
    for elemento in lista:
        print(elemento, end=" ")
    print()


# --- Bloque principal ---
numeros = cargar_lista()
imprimir_lista(numeros, "Lista completa:")

mitad_numeros = primer_mitad(numeros)
imprimir_lista(mitad_numeros, "Primera mitad de la lista:")
