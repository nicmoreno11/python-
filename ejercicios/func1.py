# 1.Función decoradora que recibe como parámetro funciones que trabajan sobre listas. 
# Estas funciones hacen operaciones estadísticas como suma, promedio,moda,mediana, 
# varianza, desviación estandar(Estas funciones uds las han desarrollado en el pasado). La función decoradora analiza que todos los numeros de la lista estén en un rango de 0 a 100. Si hay numeros fuera de ese rango no se ejecuta la función.

def decoradora(funciones):
    print(f'esto es una lista{funciones()}')
    def lista():
        lista = []
        for lista in range(0,10):
            return lista
    return lista
