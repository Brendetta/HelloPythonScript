# Escritura de un fichero estructurado línea a línea
lineas = ["Primer registro\n", "Segundo registro\n", "Tercer registro\n"]
with open("registros.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)
    
    # Lectura segura utilizando iteración directa
with open("registros.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip()) # strip() elimina el '\n' sobrante