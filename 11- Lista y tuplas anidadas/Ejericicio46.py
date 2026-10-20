'''Almacenar en una lista de 5 elementos tuplas que guarden el
nombre de un país y la cantidad de habitantes. Definir tres
funciones, en la primera cargar la lista, en la segunda
imprimirla y en la tercera mostrar el nombre del país con
mayor cantidad de habitantes'''

def carga_paises() -> list[tuple[str,int]]:
    pais, habitantes = ([input(f"Ingrese datos: {campo}")] for campo in ("pais", habitantes))
    return pais, habitantes

# def imprimir_paises(paises: list[tuple[str,int]]) -> None:
#     pass
# def mostrar_mayor_poblacion(paises: list[tuple[str,int]]) -> None:
#     pass
#
# # Bloque ppal
# lista_paises = carga_paises()
# imprimir_paises(lista_paises)
# mostrar_mayor_poblacion(lista_paises)