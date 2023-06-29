def contar(lista_num):
    if len(lista_num) == 0:
        return 0
    else:
        lista_num.pop()
        quant = 1 + contar(lista_num)
    return quant
        
def contar_algorismos(num):
    lista_num = list(str(num))
    return contar(lista_num)    

