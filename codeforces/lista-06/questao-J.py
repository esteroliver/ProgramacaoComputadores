def sublista_sem_menor(lista):
    lista1 = lista.copy()
    menor = min(lista)
    lista1.remove(menor)
    return lista1
