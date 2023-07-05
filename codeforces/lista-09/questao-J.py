def verificar_empates(lista):
    empates = 0
    empates += lista.count(max(lista))
    return empates

jogadores = int(input())
minimo_compet = int(input())
vencedores = 0
pontos = []

for i in range(jogadores):
    ponto_jogador = int(input())
    pontos.append(ponto_jogador)

while vencedores <= minimo_compet:
    maior = max(pontos)
    vencedores += verificar_empates(pontos)
    while pontos.count(maior) > 0:
        pontos.remove(maior)
    
print(vencedores)