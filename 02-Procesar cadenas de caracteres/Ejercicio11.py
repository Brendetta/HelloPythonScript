'''
Solicitar el ingreso de una clave por teclado y almacenarla en
una cadena de caracteres. Controlar que el string ingresado
tenga entre 10 y 20 caracteres para que sea válido, en caso
contrario mostrar un mensaje de error.
'''

clave = input("Escriba la clave: ")

if 10 <= len(clave) <= 20:
    print("La clave es válida")
else:
    print("La clave no cumple con la norma")