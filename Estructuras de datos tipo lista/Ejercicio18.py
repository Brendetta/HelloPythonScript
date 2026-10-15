'''Definir una lista vacía y luego solicitar la carga de 5
enteros por teclado y añadirlos a la lista. Imprimir la lista
generada.'''

lista = []

# for _ in range(5):
#     lista.append(input("Ingrese un valor entero: "))
#
# print(lista)

numeros = [int(input("Ingrese un valor entero: "))for _ in range(5)]
print(numeros)