'''
. Realizar la carga de dos nombres de personas distintos.
Mostrar por pantalla luego ordenados en forma alfabética.
'''

# Crear una lista vacía
mi_lista = []

# Bucle para pedir cada elemento
for i in range(2):
  valor = input(f"Ingresa el elemento {i + 1}: ")
  mi_lista.append(valor)

mi_lista.sort()
print(mi_lista)

