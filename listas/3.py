#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, 
#la nota media, la nota más alta que ha sacado y la menor.
from random import randint
def NotaAlumno():
	notas = []
	for i in range(0,11):
		n = int(input('Ingrese un texto: '))
		notas.append(n)
	print(f'La nota media es: {sum,{notas}/5}')
	print(f'La nota mas alta es: {max,{notas}}')
	print(f'La nota mas baja es: {min,{notas}}')
	print(notas)
NotaAlumno()
