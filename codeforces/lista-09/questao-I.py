while True:
    teste = int(input())
    pontos_xy = []
    pontos_uv = []
    resultado = True

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
            print('Y')
        else:
            print('N')