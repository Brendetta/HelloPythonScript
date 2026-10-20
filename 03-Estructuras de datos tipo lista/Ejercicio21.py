'''Cargar por teclado y almacenar en una lista las alturas de 5
personas (valores float). Obtener el promedio de las mismas.
Contar cuántas personas son más altas que el promedio y
cuántas más bajas'''

altura = [float(input("Ingrese altura: "))for _ in range(5)]
promedio = sum(altura)/len(altura)
print(f"El promedio de altura es: {promedio:.2f}")
contador = 0

for altos in altura:
    if altura > promedio:
        contador += 1

print(contador)