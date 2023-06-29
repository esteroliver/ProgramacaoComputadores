pulo, quant = map(int,input().split())
canos = list(map(int,input().split()))
ganhou = True

for i in range (quant):
    try:
        if abs(canos[i] - canos[i+1]) > pulo:
            ganhou = False
    except:
        break

if ganhou:
    print('YOU WIN')

else:
    print('GAME OVER') 