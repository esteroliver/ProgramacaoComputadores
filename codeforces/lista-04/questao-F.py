prova1_1, prova2_1 = map(int,input().split())
prova1_2, prova2_2 = map(int,input().split())
peso1, peso2 = map(int,input().split())

media1 = ((prova1_1 * peso1) + (prova2_1 * peso2))//(peso1 + peso2)

media2 = ((prova1_2 * peso1) + (prova2_2 * peso2))//(peso1 + peso2)

if (media1 > media2):
    print(1)

elif (media1 == media2):
    print(1)

else:
    print(2)