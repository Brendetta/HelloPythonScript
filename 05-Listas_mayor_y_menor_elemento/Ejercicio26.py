'''Cargar una lista con 5 elementos enteros. Imprimir el mayor y
un mensaje si se repite dentro de la lista (es decir si dicho
valor se encuentra en 2 o más posiciones en la lista)'''

numeros = [int(input("Ingrese un valor entero: "))for _ in range(5)]
mayor = max(numeros)
repeticiones = numeros.count(mayor)
print(f"El número mayor es {mayor}")
print(f"Se repite {repeticiones} {"vez" if repeticiones == 1 else "veces"}")