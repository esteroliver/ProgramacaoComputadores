def maior(lista,indice):
    if indice == -1:
        return 0
    else:
        maior_num = lista[indice]

        maior_num_2 = maior(lista,indice-1)

        if maior_num > maior_num_2:
            return maior_num
        else:
            return maior_num_2

def maior_lista(lista):
    return maior(lista,(len(lista)-1))
