'''Confeccionar un programa que genere un número aleatorio entre
1 y 100 y no se muestre. El operador debe tratar de adivinar
el número ingresado. Cada vez que ingrese un número mostrar un
mensaje "Gano" si es igual al generado o "El número aleatorio
es mayor" o "El número aleatorio es menor". Mostrar cuando
gana el jugador cuantos intentos necesitó.'''

from random import randint


def numero_aleatorio():
    aleatorio = randint(1, 100)
    intentos = 0

    while True:
        resultado = int(input("¿Qué número ha salido?: "))
        intentos += 1

        if aleatorio == resultado:
            print(F"Acertaste, necesitaste {intentos} intentos.")
            break
        elif aleatorio > resultado:
            print("El número es mayor")
        elif aleatorio < resultado:
            print("El número es menor")

numero_aleatorio()