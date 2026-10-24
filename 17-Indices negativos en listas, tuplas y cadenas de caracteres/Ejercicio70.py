'''Confeccionar un programa con las siguientes funciones:
- Cargar una lista con 5 palabras.
- Intercambiar la primera palabra con la última.
- Imprimir la lista'''

def imprimir_lista(lista: list[str]):
    print("\n")
    for i, palabra in enumerate(lista):
        print(f"Pos: {i}: {palabra}", end='')

def intercambiar_extremos(lista:list[str]):
    if lista:
        lista[0], lista[-1] = lista [-1], lista[0]


lista_palabras = ["pera", "uva", "melón", "sandía", "melocotón"]
imprimir_lista(lista_palabras)
intercambiar_extremos(lista_palabras)
imprimir_lista(lista_palabras)