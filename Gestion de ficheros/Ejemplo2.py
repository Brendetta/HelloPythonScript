import os
def mover_seguro(fichero: str, directorio_destino: str) -> None:
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
# os.path.join gestiona la barra ('/' o '\') según el S.O.
        ruta_nueva = os.path.join(directorio_destino, fichero)
        print(ruta_nueva)
        os.replace(fichero, ruta_nueva)

mover_seguro("documento.pdf", "respaldos")