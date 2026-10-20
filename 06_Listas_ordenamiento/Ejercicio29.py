'''Crear una lista por asignación. La lista tiene que tener 2
elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista
principal'''

matriz = [[2,8,7,6,1],[6,8,7,2,9]]

for i, fila in enumerate (matriz, start = 1):
    print(f"Fila {i} {sum(fila)}")