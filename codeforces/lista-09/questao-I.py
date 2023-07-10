numero = 1
while True:
    teste = int(input())
    resultado = False
    pontos_x = []
    pontos_y = []
    pontos_u = []
    pontos_v = []

    if teste == 0:
        break
    else:
        for i in range(teste):
            x, y, u, v = map(int,input().split())
            pontos_x.append(x)
            pontos_y.append(y)
            pontos_u.append(u)
            pontos_v.append(v)

        if min(pontos_u) >= max(pontos_x) and min(pontos_y) >= max(pontos_v):
            resultado = True

        if resultado:
            intersecao = [max(pontos_x), min(pontos_y), min(pontos_u), max(pontos_v)]

            print('Teste', numero)
            print(*intersecao)
            print('')

        else:
            print('Teste', numero)
            print('nenhum')
            print('')

    numero += 1