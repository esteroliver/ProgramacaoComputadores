def contar_divisores_div(n,div):
    if div == 1:
        return 1
    quant = 0
    if n%div == 0:
        quant += 1
    quant += contar_divisores_div(n,div-1)
    return quant

def contar_divisores(n):
    return contar_divisores_div(n,n)
