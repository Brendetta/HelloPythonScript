'''Cargar una lista de 5 enteros.
a. Retornar el mayor y menor valor de la lista mediante una
tupla.
b. Desempaquetar la tupla en el bloque principal y mostrar
el mayor y menor.'''

# Bloque ppal
def cargar_lista() -> list[int]:
    lista = [int(input(f"Ingrese un entero: {i + 1}")) for i in range(5)]
    return lista


def obtener_mayor_menor(lista:list[int]) -> tuple[int, int]:
    pass


numeros = cargar_lista()
mayor_val, menor_val = obtener_mayor_menor(numeros)