'''Realizar la carga de valores enteros por teclado, almacenarlos
en una lista. Finalizar la carga de enteros al ingresar el
cero. Mostrar finalmente el tamaño de la lista'''

numeros = []
valores = int(input("Ingrese un numero entero (0 para finalizar): "))
while valores != 0:
    numeros.append(valores)
    valores = int(input("Ingrese un numero entero (0 para finalizar): "))

print(numeros)
print("número de elementos: ", len(numeros))


#Bucle operador Walrus (:=) para pedir datos y evaluar la condición en el mismo paso
numeros=[]
while (valor := int(input("Ingrese un numero entero: "))) != 0:
    numeros.append(valor)
print(numeros)
print("número de elementos: ", len(numeros))