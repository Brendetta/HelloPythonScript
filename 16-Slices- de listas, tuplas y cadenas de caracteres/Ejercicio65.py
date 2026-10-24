'''Confeccionar una función que reciba una cadena de caracteres y
nos devuelva los tres primeros. En el bloque principal del
programa definir una tupla con los nombres de meses. Mostrar
por pantalla los primeros tres caracteres de cada mes.'''

MESES: tuple[str, ...] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def primeros_caracteres(caracteres: int) ->tuple[str]:
    return tuple(mes[:3] for mes in MESES)

print(primeros_caracteres(3))