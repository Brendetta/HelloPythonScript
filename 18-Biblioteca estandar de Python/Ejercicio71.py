'''Confeccionar un programa que simule tirar dos dados y luego
muestre los valores que salieron. Imprimir un mensaje que ganó
si la suma de los mismos es igual a 7.'''

from random import randint

def lanzar_dados() -> tuple[int, int]:
    return randint(1, 6), randint(1, 6)

def evaluar_lanzamiento(dados: tuple[int,int]):
    dado1, dado2 = dados
    suma = dado1 + dado2
    print(dados)
    if suma == 7:
        print("Gano!!!")
    else:
        print("Siga intentando...")

# Bloque ppal
evaluar_lanzamiento(lanzar_dados())