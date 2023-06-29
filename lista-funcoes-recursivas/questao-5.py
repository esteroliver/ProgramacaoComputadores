def binario(num):
    if num == 1:
        return '1'
    else:
        numero = binario(num//2) + str(num%2)
    return numero

def quant_alg(num):
    quant = 0
    if num == 1 or num == 0:
        return 1
    elif num//2 > 0:
        quant += 1
    quant += quant_alg(num//2)
    return quant
