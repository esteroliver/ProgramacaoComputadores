caixas = int(input())
cont = 100
saldo = 100

for i in range(caixas):
    n = int(input())
    cont += n
    if cont > saldo:
        saldo = cont
    
print(saldo)
