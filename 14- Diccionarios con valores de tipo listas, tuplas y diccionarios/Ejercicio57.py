'''Confeccionar un programa que permita cargar un código de
producto como clave en un diccionario. Guardar para dicha
clave el nombre del producto, su precio y cantidad en stock.
Implementar las siguientes actividades:
- Carga de datos en el diccionario.
- Listado completo de productos.
- Consulta de un producto por su clave, mostrar el nombre,
precio y stock.
- Listado de todos los productos que tengan un stock con
valor cero.'''

# Bloque ppal
InfoProducto = tuple[str, float,int]

def cargar_productos()-> dict[str, InfoProducto]:
    cantidad = int(input("Ingrese la cantidad de productos que desea cargar: "))
    productos = {}

    for i in range (cantidad):
        codigo = input("Ingrese el codigo del producto: ").strip()
        nombre = input("Ingrese el nombre del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        productos[codigo] = (nombre, precio, stock)

    return productos


def listar_productos(productos: dict[str, InfoProducto]) -> None:
    print("--Listado completo de productos--")
    for codigo,(nombre, precio, stock) in productos.items():
        print(f"Codigo: {codigo:<8} | Nombre: {nombre:<8} | Precio: {precio:,.2f} | Stock: {stock} ")


def consultar_productos(productos: dict[str, InfoProducto]):
    print("--Consulta de productos--")
    codigo = input("Ingrese el codigo del producto a consultar: ").strip()
    if info := productos.get(codigo):
        nombre, precio, stock = info
        print(f"Datos del producto: \n Nombre: {nombre} \n Precio: {precio} \n Stock: {stock}")
    else:
        print("No existe producto con ese codigo")




def listar_stock_cero(productos: dict[str, InfoProducto]):
    print("-- Productos con stock 0 --")
    sin_stock = [
        (cod, nom, pre) for cod, (nom, pre, stock) in productos.items()if stock == 0
    ]
    if sin_stock:
        for cod, nom, pre in sin_stock:
            print(f"Codigo: {cod:<8} | Nombre: {nom:<8} | Precio: {pre:,.2f}")
        else:
            print("No hay ningún producto sin stock")

dicc_productos = cargar_productos()
listar_productos(dicc_productos)
consultar_productos(dicc_productos)
listar_stock_cero(dicc_productos)