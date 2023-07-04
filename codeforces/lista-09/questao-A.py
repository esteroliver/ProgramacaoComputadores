jogadores, rodadas = map(int,input().split())
pontos = list(map(int,input().split()))
quant = len(pontos)

while quant != jogadores:
    for i in range(len(pontos)):
        try:
            pontos[i] += pontos[i+jogadores]
            pontos[i+jogadores] = 0
        except:
            break
    quant -= 1

while pontos.count(max(pontos)) > 1: 
    indice = pontos.index(max(pontos))
    pontos[indice] = 0

vencedor = pontos.index(max(pontos)) + 1

print(vencedor)