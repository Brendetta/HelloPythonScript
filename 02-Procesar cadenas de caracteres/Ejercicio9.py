'''
Cargar una oración por teclado. Mostrar luego cuantos espacios
en blanco se ingresaron. Tener en cuenta que un espacio en
blanco es igual a " ", en cambio una cadena vacía es ""
'''

frase= input("frase: ")
espacios = frase.count(" ")
print(espacios)