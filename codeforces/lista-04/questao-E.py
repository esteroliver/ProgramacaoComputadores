linhas = int(input())
colunas = int(input())

if ((colunas-linhas)%2 == 0 or (linhas-colunas)%2 == 0 or colunas == linhas):
    print(1)

else:
    print(0)