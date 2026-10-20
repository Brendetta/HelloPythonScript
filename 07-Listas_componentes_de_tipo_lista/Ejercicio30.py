'''Crear una lista por asignación. La lista tiene que tener 5
elementos. Cada elemento debe ser una lista, la primera lista
tiene que tener un elemento, la segunda dos elementos, la
tercera tres elementos y así sucesivamente. Sumar todos los
valores de las listas.'''

matriz = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]

# for i, fila in enumerate(matriz,start = 1):
#     print(f"Fila {i} {sum(fila)}")

suma_total = sum(sum(sublista) for sublista in matriz)
print(f"Lista con sublistas: \n {matriz}")
print(f"Suma total: {suma_total}")
