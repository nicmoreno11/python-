#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
#Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

def ListaTeclado():
	cadena = []
	for i in range(0,5):
		t = input('Ingrese un texto: ')
		cadena.append(t)
	#copiar la cadena desde el primer elemento hasta el ultimo elemento, la cadena2 copia el contenido de la cadena1 
	cadena2 = cadena[:]
	cadena2.reverse()
	print(cadena)
	print(cadena2)
ListaTeclado()