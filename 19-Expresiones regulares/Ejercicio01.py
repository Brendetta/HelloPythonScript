'''Escribir una función verifCaracCadenas(cadena) que tome
como entrada una cadena de caracteres cadena y
verifique si esta última contiene únicamente
letras minúsculas, números, signos de puntuación (?/,/!/.)
o un apóstrofo (‘). La función devuelve True si la cadena cumple
con los requisitos mencionados anteriormente y False en caso contrario.

Requisito: Hay que usar expresiones regulares'''
import re

def verifCaracCadenas(cadena: str) -> bool:
    patron = r"^[a-záéíóú0-9?,!.\'/]+$"
    return re.fullmatch(patron,cadena) is not None

print(verifCaracCadenas("hola123?!."))
print(verifCaracCadenas("c'est!"))
print(verifCaracCadenas("Hola123?!."))
print(verifCaracCadenas("texto con espacios"))
print(verifCaracCadenas("test#123"))