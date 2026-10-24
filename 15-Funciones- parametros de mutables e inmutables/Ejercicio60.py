'''Confeccionar un programa que contenga las siguientes
funciones:
- Carga de una lista y retorno al bloque principal.
- Fijar en cero todos los elementos de la lista que tengan
un valor menor a 10.
- Imprimir la lista'''


def cargar_lista() -> list[int]:
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    return [int(input(f"Ingrese el elemento {i+1} de {cantidad}: "))for i in range(cantidad)]

numeros = cargar_lista()

def fijar_ceros_menores_10(numeros: list[int]) ->None:
    #lista [:] muta la lista existente en lugar de crear una variable local
    numeros[:] = [val if val >= 10 else 0 for val in numeros]
    '''
    Escribir numeros = [val if...] crearía una nueva variable local perdiendo
    la referencia con la lista del bloque ppal
    '''

fijar_ceros_menores_10(numeros)

def imprimir_lista(numeros: list[int]) -> None:
    print(f"Lista procesada: {numeros}")

imprimir_lista(numeros)
