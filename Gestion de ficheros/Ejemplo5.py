import os
def explorar_directorio(ruta_base: str) -> None:
# Explora recursivamente un directorio mostrando el tamaño de los ficheros
    print(f"\n--- Explorando: {ruta_base} ---")
    try:
        elementos = os.listdir(ruta_base)
    except PermissionError:
        print(f"Sin permisos para acceder a: {ruta_base}")
        return
for elemento in elementos:
    ruta_completa = os.path.join(ruta_base, elemento)
# Si es un directorio, aplicamos recursividad
    if os.path.isdir(ruta_completa):
        explorar_directorio(ruta_completa)
# Si es un fichero, mostramos su información
    elif os.path.isfile(ruta_completa):
        tamano = os.path.getsize(ruta_completa)
        print(f"Fichero: {elemento} | Tamaño: {tamano} bytes")

# Ejemplo de uso:
explorar_directorio("./home/brenda/Documentos/")