'''Confeccionar un programa con las siguientes funciones:
a. Cargar el nombre de un empleado y su sueldo. Retornar una
tupla con dichos valores
b. Una función que reciba como parámetro dos tuplas con los
nombres y sueldos de empleados y muestre el nombre del
empleado con sueldo mayor.
c. En el bloque principal del programa llamar dos veces a la
función de carga y seguidamente llamar a la función que
muestra el nombre de empleado con sueldo mayor.'''

# Bloque ppal
def cargar_empleado():
    nombre = input("Ingrese su nombre: ")
    sueldo = float(input("Ingrese su sueldo: "))
    return nombre, sueldo


def mostrar_mayor_sueldo(emp1: tuple[str, float],emp2: tuple[str, float]):
    nombre1, sueldo1 = emp1
    nombre2, sueldo2 = emp2

    if sueldo1 == sueldo2:
        print("Los empleados ganan lo mismo")
    else:
        nombre_mayor, sueldo_mayor = max(emp1,emp2,key=lambda x: x[1])
        print(f"El empleado con sueldo mayor es {nombre_mayor} con sueldo {sueldo_mayor}")


empleado1 = cargar_empleado()
empleado2 = cargar_empleado()
mostrar_mayor_sueldo(empleado1,empleado2)