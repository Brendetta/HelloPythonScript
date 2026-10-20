'''Desarrollar una función que solicite la carga del dia, mes y
año y almacene dichos datos en una tupla que luego debe
retornar. La segunda función a implementar debe recibir una
tupla con la fecha y mostrarla por pantalla.'''

# Bloque ppal
def cargar_fecha() -> tuple[int, int, int]:
    dia, mes, anio = (int(input(f"Ingrese el {campo}")) for campo in ("dia", "mes", "año"))
    return dia, mes, anio
# Desempaquetado
def imprimir_fecha(fecha: tuple[int, int, int]):
    dia, mes, anio = fecha
    print(f"Fecha: {dia:02d}/{mes:02d}/{anio:02d}")

fecha_cargada = cargar_fecha()
imprimir_fecha(fecha_cargada)