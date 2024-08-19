mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

def stuff(mi_lista):
    mi_lista = sorted(mi_lista) #sorted() ordena la lista
    lista = ((set(mi_lista))) #set() convierte la lista en un set y debido a sus propiedades elimina los duplicados
    print(list(lista)) # list() lista entra, lista sale.

stuff(mi_lista)