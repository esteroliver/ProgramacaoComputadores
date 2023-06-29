def lista_troca_menor_primeiro(lista):
    if min(lista) == lista[0]:
        return 0
    else:
        ind_menor = lista.index(min(lista))
        primeiro = lista[0]
        lista[0] = min(lista)
        lista[ind_menor] = primeiro 
        return 1
    