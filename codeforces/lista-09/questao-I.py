numero = 1
while True:
    teste = int(input())
    resultado = True
    pontos_xy = []
    pontos_uv = []
    

    if teste == 0:
        break
    else:
        for i in range(teste):
            x, y, u, v = map(int,input().split())
            xy = (x,y)
            uv = (u,v)
            pontos_xy.append(xy)
            pontos_uv.append(uv)

        pontos_xy.sort()
        pontos_uv.sort()

        for j in range(teste):
            try:
                if (pontos_xy[j])[0] > (pontos_uv[j+1])[0]:
                    resultado = False
                if (pontos_xy[j])[1] < (pontos_xy[j+1])[0]:
                    resultado = False
                if (pontos_uv[j])[1] > (pontos_xy[j+1])[1]:
                    resultado = False
            except:
                break

        if resultado:
            inte_uv = min(pontos_uv)
            inte_xy = max(pontos_xy)
            intersecao = [inte_xy[0], inte_xy[1], inte_uv[0],inte_uv[1]]
            print('Teste', numero)
            print(*intersecao)
            print('')
        else:
            print('Teste', numero)
            print('nenhum')
            print('')

    numero += 1