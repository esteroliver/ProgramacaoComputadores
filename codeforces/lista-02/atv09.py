compr, ped = map(int,input().split())
valor_compr, valor_ped = map(int,input().split())
quant_ped = compr//ped
total = (valor_compr*compr) + (quant_ped*valor_ped)
print(total)