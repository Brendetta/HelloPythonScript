'''Se tiene la siguiente lista:
lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
1. Imprimir la lista. Luego fijar con el valor cero todos
los elementos mayores a 50 del primer elemento de
"lista". Volver a imprimir la lista.
2. Imprimir la lista. Luego fijar con el valor cero todos
los elementos mayores a 10 contenidos en todos los
elementos de la variable "lista". Volver a imprimir la
lista.'''

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print(lista)
lista = [[0 if x > 50 else x for x in lista]]
print(f"Lista modificada 1 : \n{lista}")

# resultado = [[0 if x > 50 else x for x in sublista] for sublista in lista]


