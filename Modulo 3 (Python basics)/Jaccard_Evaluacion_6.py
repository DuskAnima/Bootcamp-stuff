n = 2,5,7,8,3,6,3

def numberSorter(n):
    n = sorted(n, reverse=True) # La  propiedade reverse = True de sorted() invirte el enlistamiento
    print(n)

numberSorter(n)


def nSHardcoding(n):
    nList = list(n) # n Es entregado como tupla, entonces es necesario darle formato de lista
    sortedList = []
    while nList: # Mientras la lista posea valores*
        mxN = max(nList) # Buscar el numero mayor de la lista de numeros
        sortedList.append(mxN) # Ese numero debe ser reservado en otra lista para el resultado
        nList.remove(mxN) # Se descarta el mismo número de la lista original para evitar repeticiones
    print(sortedList)

nSHardcoding(n)


