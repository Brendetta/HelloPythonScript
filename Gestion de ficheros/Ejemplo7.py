def analizar_fichero(ruta_fichero: str) -> tuple[int, int, int]:
# """Cuenta el número de líneas, palabras y caracteres de un archivo de
# texto."""
    n_lineas = 0
    n_palabras = 0
    n_caracteres = 0
    with open(ruta_fichero, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            n_lineas += 1
        # Normalización quitando el salto de línea final
            linea_limpia = linea.rstrip("\n")
            palabras = linea_limpia.split()
            n_palabras += len(palabras)
            n_caracteres += len(linea_limpia)
    return n_lineas, n_palabras, n_caracteres
        # Ejemplo de ejecución
try:
    lineas, palabras, caracteres = analizar_fichero("el_quijote.txt")
    print(f"Resultados para 'el_quijote.txt':")
    print(f" - Líneas: {lineas}")
    print(f" - Palabras: {palabras}")
    print(f" - Caracteres: {caracteres}")
except FileNotFoundError:
    print("El archivo especificado no existe.")