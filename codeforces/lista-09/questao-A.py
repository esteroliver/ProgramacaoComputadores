def maior_ind(lista):
    maior = lista[0]
    indice = 0
    for i in range(len(lista)):
        if maior <= lista[i]:
            maior = lista[i]
            indice = i
    return indice+1

jogadores, rodadas = map(int,input().split())
pontos = list(map(int,input().split()))
quant = len(pontos)

for i in range(jogadores):
    for j in range(1,rodadas):
        pontos[i] += pontos[i+j*jogadores]

print(maior_ind(pontos))
