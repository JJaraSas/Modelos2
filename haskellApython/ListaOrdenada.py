def listaOrdenada(lista):
    if lista == []: return True
    if len(lista) == 1: return True
    return (lista[0]<=lista [1] and listaOrdenada(lista[1:]))

print listaOrdenada(['a','b','c','d'])
