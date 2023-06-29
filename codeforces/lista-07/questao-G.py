quant = int(input())
lista = list(map(int,input().split()))
soma = 0

for i in lista:
    soma += i
    media = soma/(len(lista))

abaixo = 0
abaixo_list = []
acima = 0
acima_list = []

for i in lista:
    if i < media:
        abaixo += 1
        abaixo_list.append(i)
    else:
        acima += 1
        acima_list.append(i)

print("{:.1f}".format(media))
print(abaixo,*abaixo_list)
print(acima,*acima_list)