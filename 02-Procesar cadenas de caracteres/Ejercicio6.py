'''
Solicitar la carga del nombre de una persona en minúsculas.
Mostrar un mensaje si comienza con vocal dicho nombre.
'''

nombre=input("Ingrese nombre: ")
print("El nombre ", end="")
if nombre[0] in "aeiouAEIOU":
    print("comienza ",end="")
else:
    print("no comienza ",end="")
print("por vocal")