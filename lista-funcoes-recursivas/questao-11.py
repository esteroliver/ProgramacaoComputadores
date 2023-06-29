def divisores(num,div):
    if div == 1:
        return 1
    quant = 0
    if num%div == 0:
        quant += 1
    quant += divisores(num,div-1)
    return quant

def primos(lista,indice):
    param = lista[indice]
    lista_com_primos = []
    if indice == -1:
        return [0]
    else:
        lista_com_primos = primos(lista,indice-1)
        if divisores(param,param) == 2:
            lista_com_primos.append(param)
        return lista_com_primos
    
def lista_primos(lista):
    indice = len(lista)-1
    return primos(lista,indice)
        
