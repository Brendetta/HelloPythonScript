'''Definir por asignación una lista con 8 elementos enteros.
Contar cuántos de dichos valores almacenan un valor superior a 100'''

lista = [8,15,64,82,200,452,625,9]

print(sum(1 for numero in lista if numero > 100))

# contador = 0
#
# for numero in lista:
#     if numero > 100:
#         contador += 1
#
# print(contador)
