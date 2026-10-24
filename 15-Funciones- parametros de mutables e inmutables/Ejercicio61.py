'''Confeccionar un programa que contenga las siguientes
funciones:
- Carga de una lista de 5 nombres.
- Ordenar alfabéticamente la lista.
- Imprimir la lista de nombres'''


def cargar_lista() -> list[str]:
    return [input(f"Ingrese nombre {i +1}/5 ")for i in range (5)]

nombres = cargar_lista()

def ordenar_alfabeticamente(nombres:list[str])-> None:
    # Key=str.lower asegura que la ordenación no se vea afectada por el orden ASCII
    nombres.sort(key=str.lower)

ordenar_alfabeticamente(nombres)


def imprimir_nombres(nombres: list[str]) -> None:
    print("\n--Lista de nombres--")
    for i, nombre in enumerate(nombres, start=1):
        print(f"{i}. {nombre}")


imprimir_nombres(nombres)