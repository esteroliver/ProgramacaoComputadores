largura = int(input())
comprimento = int(input())
quant_tipo1 = (comprimento*largura) + ((comprimento-1)*(largura-1))
quant_tipo2 = ((largura - 1) + (comprimento - 1)) * 2
print(quant_tipo1)
print(quant_tipo2)