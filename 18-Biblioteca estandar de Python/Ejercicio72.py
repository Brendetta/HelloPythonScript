'''Desarrollar un programa que cargue una lista con 10 enteros.
Cargar los valores aleatorios con números enteros comprendidos
entre 0 y 1000. Mostrar la lista por pantalla. Luego mezclar
los elementos de la lista y volver a mostrarlo.'''
import random
from random import randint
lista = []

def cargar_lista_aleatoria()-> list[int]:
    for i in range(10):
        lista.append(randint(0,100))
    return lista

def desordenar_lista(lista: list[int]) -> list[int]:
    random.shuffle(lista)
    return lista


print(f"\nLa lista original es: {cargar_lista_aleatoria()} \n"
      f"La lista desordenada es: {desordenar_lista(lista)}")
