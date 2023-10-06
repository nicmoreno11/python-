#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos 
#es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, 
#y devuelve si el primero es múltiplo del segundo.
def EsMultiplo(numero1,numero2):
	if numero1 % numero2 == 0:
		print('El',numero1,'es multiplo de',numero2)
	
	elif numero2 % numero1 == 0:
		print('El',numero2,'es multiplo de',numero1)
	else:
		print('Ninguno es multiplo ¡¡ERROR!!')
numero1 = int(input('Digite el primer numero:'))
numero2 = int(input('Digite el segundo numero:'))
EsMultiplo(numero1,numero2)