#Explique el uso de argumentos de tipo posicionales (*args) y argumentos clave (**kwargs). 
#Escriba dos ejemplos con el código comentariado con la explicación

#1 Si a es multiplo de b. 
def EsMultiplo(a,b): #definimos una funcion con argumentos posicionales  los cuales son a y b. 
	if a % b == 0: #hacemos una condicion para verificar si a es multiplo de b. 
		print(a,'es multiplo de',b) #imprime si la condicion se cumple. 
	elif b % a == 0: #usamos la condicion elif por si b es multiplo a. 
		print(b,'es multiplo de',a) #imprime si esta condicion se cumple. 
	else:
		print('Ninguno es multiplo ¡ERROR!') #si ninguna de las condiciones se cumple imprime ¡ERROR! en la consola.
EsMultiplo(4,2) #llamamos la funcion y pasamos los dos argumento que a=4 y b=2, los dos son multiplos asi que no hay nigun error. 

#2 pasar varios datos a **kargs. 
def imprimir_datos(**kargs): #definimos la funcion imprimir_datos como argumento **kargs que puede recibir canidad de argumentos. 
	for clave, valor in kargs.items(): #el for establece una variable = clave para almacenar el (nombre del argumento) para almacenar el valor. 
		print(f'{clave}: {valor}') #imprime la clave y valor en la consola 
imprimir_datos(nombre = "Nicolas", edad=19, ciudad="Bogota") #llamamos la funcion imprmir_datos con argumentos kargs
# el bucle for iterara a traves de los elemtos del diccionario.
