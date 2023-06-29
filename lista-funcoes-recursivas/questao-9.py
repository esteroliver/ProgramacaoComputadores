def soma_pares(lista,indice):
    soma = 0
    if indice == -1:
        return 0 
    else:
        if lista[indice]%2 == 0:
            soma += lista[indice]
        soma += soma_pares(lista,indice-1)
        return soma

def soma_pares_lista(lista):
    return soma_pares(lista,(len(lista)-1))
