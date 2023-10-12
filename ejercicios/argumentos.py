from random import randint
def generar_lista():
    # Generar una lista de tamaño aleatorio entre 10 y 100 con números aleatorios entre 0 y 100.
    lista = [randint(10,100) for i in range (10,100)]
    print(lista)
generar_lista()

#codigo de chat-gpt
"""def encontrar_max_min_suma(*listas):
    if not listas:
        return "No se proporcionaron listas."

    max_suma = float('-inf')
    max_lista = None
    max_numero = float('-inf')
    min_numero = float('inf')

    for lista in listas:
        suma_actual = sum(lista)
        numero_max_actual = max(lista)
        numero_min_actual = min(lista)
   
        if suma_actual > max_suma:
            max_suma = suma_actual
            max_lista = lista
        if numero_max_actual > max_numero:
            max_numero = numero_max_actual
        if numero_min_actual < min_numero:
            min_numero = numero_min_actual

    return f"La lista con la suma mayor es {max_lista}, su suma es {max_suma}, el número mayor es {max_numero} y el número menor es {min_numero}."""""

