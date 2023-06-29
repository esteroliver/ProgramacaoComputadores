quant = int(input())
lista = list(map(int,input().split()))
soma = 0

for i in lista:
    soma += i
    media = soma/(len(lista))

menores = 0
maiores = 0

for i in lista:
    if i < media:
        menores += 1
    else:
        maiores += 1


print("{:.1f}".format(media))
print(menores)
print(maiores)