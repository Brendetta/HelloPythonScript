'''Definir una lista que almacene por asignación los nombres de 5
personas. Contar cuántos de esos nombres tienen 5 o más
caracteres.'''

lista = ["Ana", "Isabel", "Mónica", "Pablo", "Antonio"]

contador = 0

for caracteres in lista:
    if len(lista) > 5:
        contador += 1

print(contador)