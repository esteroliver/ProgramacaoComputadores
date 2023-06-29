a, b, c = map(int,input().split())
lados = []
lados.extend([a, b, c])
lados.sort()

if (a+b > c and a+c > b and c+b > a):
    if (lados[2]**2 == lados[0]**2 + lados[1]**2):
        print('r')

    elif (lados[2]**2 > lados[0]**2 + lados[1]**2):
        print('o')

    elif (lados[2]**2 < lados[0]**2 + lados[1]**2):
        print('a')

else:
    print('n')