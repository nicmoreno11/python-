#Escribe un programa que lea una cadena y devuelva un diccionario 
#con la cantidad de apariciones de cada carácter en la cadena.
def Cadena():
	dict = {}
	frase = input('Escriba una frase: ')
	lista_palabras = frase.split(' ')
	for palabra in lista_palabras:
		if palabra in dict:
			dict[palabra] += 1
		else: 
			dict[palabra] = 1
	for campo, valor in dict.items():
		print(campo,'->', valor)
Cadena()