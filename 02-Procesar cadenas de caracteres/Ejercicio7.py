'''
Ingresar un mail por teclado. Verificar si el string ingresado
contiene solo un caracter "@".
'''

email = input("Email: ")

if email.count("@") == 1:
    print("El email contiene un solo @")
else:
    print("El email contiene más de un @")


