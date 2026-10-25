'''Confeccionar una función que reciba una palabra y verifique si
es capicúa (es decir que se lee igual de izquierda a derecha
que de derecha a izquierda)'''


def capicua():
    palabra = input("Comparar palabra: ").lower()
    if palabra[::-1] == palabra:
        print("Es capicúa")
    else:
        print("No es capicúa")

capicua()