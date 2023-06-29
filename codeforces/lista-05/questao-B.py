bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8 = map(int,input().split())
byte = []
byte.extend([bit1,bit2,bit3,bit4,bit5,bit6,bit7,bit8])

condicao = 0

for i in range(0,8):
    if (byte[i] == 0 or byte[i] == 1):
        condicao += 1

if condicao == 8:
    print('S')
else:
    print('F')