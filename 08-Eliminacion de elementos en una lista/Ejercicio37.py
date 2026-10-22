'''Desarrollar un programa que cree una lista de 50 elementos. El
primer elemento es una lista con un elemento entero, el
segundo elemento es una lista de dos elementos etc.

La lista debería tener esta estructura y asignar esos valores
a medida que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]'''

# Crear la lista con la estructura requerida usando comprensión de listas
lista_progresiva = [list(range(1, i + 1)) for i in range(1, 51)]

# Imprimir el resultado para verificar la estructura
print(f"Total de sublistas creadas: {len(lista_progresiva)}")
print("Primeras 5 sublistas:", lista_progresiva[:5])
print("Última sublista (50 elementos):", lista_progresiva[-1])


