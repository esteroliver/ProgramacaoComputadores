salto1, salto2, salto3 = map(int,input().split())
saltos = []
saltos.extend([salto1,salto2,salto3])
saltos.sort()

if (salto1 == salto2 or salto1 == salto3 or salto2 == salto3):
    print('S')

elif (saltos[2] == saltos[1] + saltos[0] ):
    print('S')

else:
    print('N')
    