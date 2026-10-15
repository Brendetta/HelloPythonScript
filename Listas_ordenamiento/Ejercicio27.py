'''Se debe crear y cargar una lista donde almacenar 5 sueldos.
Ordenar de mayor a menor la lista'''

sueldos = [float(input(f"Ingrese sueldos {i+1}: ")) for i in range(5)]
#sueldos.sort()
#sueldos_ordenados = sorted(sueldos)
#print(f"Lista ordenada: ", sueldos_ordenados)
print(sorted(sueldos))