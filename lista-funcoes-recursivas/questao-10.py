def ordenar(lista,indice):
    if indice == -1:
        return True
    else:
        if lista[-2] > lista[-1]:
            return False
        else:
            return ordenar(lista,indice-1)
        
def ordenar_lista(lista):
    return ordenar(lista,len(lista)-1)

