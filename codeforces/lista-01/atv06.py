valor1,valor2 = map(int,input().split())
peso1,peso2 = map(int,input().split())

mp = int((valor1*peso1 + valor2*peso2)/(peso1+peso2))

print(mp)