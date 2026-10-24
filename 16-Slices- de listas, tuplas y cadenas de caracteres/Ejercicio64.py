'''Confeccionar una función que le enviemos un número de mes como
parámetro y nos retorna una tupla con todos los nombres de
meses que faltan hasta fin de año.'''

MESES: tuple[str, ...] = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                          "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")



def meses_faltantes(numero_mes: int)->tuple[int, ...]:
    return MESES[numero_mes:]


mes_actual = int(input("Introduzca mes actual (1 a 12): "))
if 1<=mes_actual<=12:
    restantes = meses_faltantes(mes_actual)
    print(f"\nMeses faltantes {len(restantes)}): {', '.join(restantes)if restantes else 'Ya es diciembre'}")
    print(f"Tupla retornada: {restantes}")
else:
    print("Número de mes incorrecto")