'''
Ingresar una oración que puede tener letras tanto en
mayúsculas como minúsculas. Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para
que sea más fácil disponer la condición que verifica que es
una vocal.
'''

oracion = input("Escriba oración: ")
oracion =oracion.lower()
'''
contador = 0
for caracter in oracion:
    if caracter in 'aeiou':
        contador += 1
'''
contador = sum(1 for caracter in oracion if caracter in 'aeiou')
print (oracion)
print("Cantidad de vocales", contador)