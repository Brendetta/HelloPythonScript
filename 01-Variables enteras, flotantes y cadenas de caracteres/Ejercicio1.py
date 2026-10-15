'''
Realizar la carga por teclado del nombre, edad y altura de dos
personas. Mostrar por pantalla el nombre de la persona con
mayor altura.
'''

nombre1=input("Ingrese el nombre1: ")
edad1=int(input("Ingrese la edad1: "))
altura1=float(input("Ingrese la altura1: "))

nombre2=input("Ingrese el nombre2: ")
edad2=int(input("Ingrese la edad2: "))
altura2=float(input("Ingrese la altura2: "))

if altura1>altura2:
    print(nombre1)
else:
    print(nombre2)