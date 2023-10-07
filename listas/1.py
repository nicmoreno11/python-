#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

from random import randint
def NumerosAleatorios():
	lista = [randint(1,10) for i in range(0,10)]
	print(lista)

	for i in lista:
		#f string son cadenas literales que tienen expresiones dentro de llaves. 
		print(f'{i} Elevado al cuadrado es: {i**2} y elevado al cubo es: {i**3}')
NumerosAleatorios()
