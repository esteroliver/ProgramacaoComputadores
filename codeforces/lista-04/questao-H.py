cap = int(input())
alunos = int(input())
viagens = 1

while ((cap-1) < alunos):
    viagens += 1
    alunos -= (cap-1)

print(viagens)