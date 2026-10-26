'''Escribir una función extraccionInfo(*archivos, salidaRuta) que tome
 como parámetro uno o varios archivos de texto. Debe extraer únicamente
 los números de teléfono franceses (con un prefijo +33 seguido de 9 dígitos)
 y las direcciones de correo electrónico de gmail.com. La función debe luego
 escribir todos los datos extraidos en un único archivo de texto con ruta en ‘salidaRuta’.

Requisito: Hay que usar expresiones regulares'''

import re

def extraccionInfo(*archivos: str, salidaRuta: str ) -> None:
#  patrón para teléfono (+33 opcionalmente seguido de espacio y 9 dígitos)
    patron_tlf = r'\+33\s?\d{9}(?!\d)'

# patrón para correos de gmail
# \b\b sirve para considera el email como una palabra, daría error pepe@gmail.com.ar
    patron_email = r'\b[a-zA-Z0-9.%+-]+@gmail\.com\b'

# Expresión regular combinada
    patron = re.compile(f"{patron_tlf}|{patron_email}")
    extraidos: list[str] = []

# Recorrido de cada archivo de entrada
    for ruta in archivos:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                # finditer captura la coincidencia exacta sin importar subgrupos
                for match in patron.finditer(contenido):
                    extraidos.append(match.group())
        except FileNotFoundError:
            print(f"Advertencia: El archivo '{ruta}' no existe")

    with open(salidaRuta, "w", encoding="utf-8") as archivo_salida:
        for registro in extraidos:
            archivo_salida.write(f"{registro}\n")

    print(f"Proceso completado. Se extrajeron {len(extraidos)} en: {salidaRuta}")



# ppal
# archivos de ejemplo para probar la extraccion
doc1 = "archivo_prueba1.txt"
doc2 = "archivo_prueba2.txt"
salida = "contactosExtraidos.txt"

contenido_doc1 = """
Contacto en Paris: +33123456789 (horario laboral)
Correo personal: usuario.prueba@gmail.com
Correo corporativo (se ignora): usuario@empresa.fr
Tlfno español (se ignora): +341234"""
contenido_doc2 = """
Pierre: +33 987654321, mail: pierre@gmail.com
Sophie: shopie@hotmail.com
Jane: +33568521471 / jane@gmail.com
Telefono incompleto (se ignora): +331234"""

# Creacion fisica de los archivos de entrada
with open(doc1, "w", encoding="utf-8") as f1:
    f1.write(contenido_doc1)
with open(doc2, "w", encoding="utf-8") as f2:
    f2.write(contenido_doc2)

# Ejecucion de la funcion
extraccionInfo(doc1, doc2, salidaRuta=salida)

print("...Contenido extraído en el archivo de salida")
with open(salida, "r", encoding="utf_8") as fsalida:
    print(fsalida.read())