'''Crear y cargar una lista con los nombres de tres alumnos. Cada
alumno tiene dos notas, almacenar las notas en una lista
paralela. Cada componente de la lista paralela debe ser
también una lista con las dos notas. Imprimir luego cada
nombre y sus dos notas.'''

nombres = ["Micaela", "Mariano", "Alegría"]
notas = [[8,6],[5,7],[8,5]]
lista_concatenada = nombres + notas

print(lista_concatenada)

for nombre, (n1, n2) in zip(nombres,notas):
    print(f"Nombre: {nombre:<10} | Notas: {n1:.1f}, {n2:.1f}")