'''
Realizar la carga de enteros por teclado. Preguntar después
que ingresa el valor si desea cargar otro valor debiendo el
operador ingresar la cadena 'si' o 'no' por teclado.
'''

opcion="si"
suma = 0
while opcion == "si":
    valor=int(input("Valor: "))
    suma = suma+valor
    opcion = input("(si/no)")
    print (f"La suma de los valores ingresado es {suma}")