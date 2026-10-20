'''Crear una lista por asignación. La lista tiene que tener
cuatro elementos. Cada elemento debe ser una lista de 3
enteros. Imprimir sus elementos accediendo de diferentes
modos.'''

matriz = [[10,20,30],[40,50,60],[70,80,90]]

#Desempaquetado de filar e iteración directa
print("\nIteración directa por filas")
for fila in matriz:
    print(fila)

#Desempaquetado con enumerate() para conservar índice y valores
print ("\nDesempaquetado con enumerate()")
for num_fila, fila in enumerate(matriz):
    print(f"Fila {num_fila}: {fila}")

#Desempaquetado de elementos internos ("unpacking")
print("\nDesempaquetado de elementos de cada sublista")
for a, b , c in matriz:
    print(f"Valores: a={a} b={b} c={c} ")

#Impresión en formato de tabla limpia combinando join()
print("\nRepresentación tabular")
for fila in matriz:
    print(" | ".join(f"{num:3d}" for num in fila))