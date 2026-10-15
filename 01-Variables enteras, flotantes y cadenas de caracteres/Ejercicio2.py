'''
Realizar la carga de dos nombres por teclado. Mostrar cuál de
los dos es mayor alfabéticamente o si son iguales.
'''

nombre1 = input("Nombre1: ")
nombre2 = input("Nombre2: ")

if nombre1==nombre2:
    print("El nombre es igual")
else:
    if nombre1>nombre2:
        print(f"{nombre1} es mayor que {nombre2}")
    else:
        print(f"{nombre2} es mayor que {nombre1}")