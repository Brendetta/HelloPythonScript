'''Confeccionar un programa que almacene en un diccionario como
clave el nombre de un contacto y como valor su número
telefónico:
- Carga de contactos y su número telefónico.
- Permitir modificar el número telefónico. Se ingresa el
nombre del contacto para su búsqueda.
- Imprimir la lista completa de contactos con sus números
telefónicos.'''


def cargar_contactos() -> dict[str,str]:
    agenda_contactos= {}

    for i in range(2):
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese teléfono: ")
        agenda_contactos[nombre] = telefono
    return agenda_contactos


def imprimir_contactos(agenda_contactos: dict[str,str]) -> None:
    print(f"--Lista de contactos")
    for nombre, telefono in agenda_contactos.items():
        print(f"{nombre} {telefono}")

def modificar_telefono(agenda_contactos: dict[str,str]) -> None:
    pass

agenda_contactos = cargar_contactos()
imprimir_contactos(agenda_contactos)
# modificar_telefono(agenda_contactos)
imprimir_contactos(agenda_contactos)