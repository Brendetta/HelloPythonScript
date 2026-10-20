'''Crear y cargar una lista con 5 enteros. Implementar un
algortimo que identifique el mayor valor de la lista.'''

# numeros = []
# for i in range(5):
#     valor = int(input("Ingrese un numero entero: "))
#     numeros.append(valor)
#
# mayor = numeros[0]
# for numero in numeros[1:]:
#     if numero > mayor:
#         mayor = numero
# print(f"\nLista de numeros: {numeros}")
# print(f"Mayor valor: {mayor}")

numeros = [int(input("Ingrese un numero enterio: ")) for i in range(5)]
mayor = max(numeros)
print(f"\nLista de números: {numeros}")
print(f"Mayor valor: {mayor}")
