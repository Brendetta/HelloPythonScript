'''Crear un diccionario que permita almacenar 5 artículos,
utilizar como clave el nombre de productos y como valor el
precio del mismo.
Desarrollar además las funciones de:
- Imprimir en forma completa el diccionario
- Imprimir solo los artículos con precio superior a 100.'''

# Bloque ppal

def cargar_productos()-> dict[str,float]:
    return {
        input(f"Ingrese nombre del producto {i+1}"):float(input("Ingrese precio")) for i in range(5)
    }

def imprimir_diccionario(productos: dict[str,float])-> None:
    for producto, precio in productos.items():
        print(f"Producto: {producto:<15} | precio: {precio:,.2f}")

def imprimir_mayores_100(productos: dict[str,float])-> None:
    print("\nProductos con precio mayor que 100.")
    superiores = {prod: prec for prod, prec in productos.items() if prec >100}

    if superiores:
        for producto, precio in superiores.items():
            print(f"Producto: {producto:<15} | precio: {precio:,.2f}")
        else:
            print("no se encontraron artículos superiores a 100")


dicc_productos= cargar_productos()
imprimir_diccionario(dicc_productos)
imprimir_mayores_100(dicc_productos)