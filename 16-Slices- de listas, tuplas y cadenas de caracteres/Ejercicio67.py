'''Cargar una cadena por teclado luego:
Imprimir los dos primeros caracteres
imprimir los dos últimos
Imprimir todos menos el primero y el último'''

def procesar_texto(cadena:str):
    if len(cadena) < 2:
        print("El texto debe ser mayor que 2")
        return
    print(f"Los dos primeros caracteres son {cadena[:2]}")
    print(f"Los dos últimos caracteres son {cadena[:-2]}")
    print(f"Sin el primero y el último {cadena[1:-1]}")

texto= input("Ingrese texto:").strip()
procesar_texto(texto)
