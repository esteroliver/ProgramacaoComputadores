frango, bife, massa = map(int,input().split())
req_f, req_b, req_m = map(int,input().split())

sem_refeicao = 0

if req_f > frango:
    sem_refeicao += (req_f - frango)
if req_b > bife:
    sem_refeicao += (req_b - bife)
if req_m > massa:
    sem_refeicao += (req_m - massa)

if sem_refeicao == 0:
    print(0)
else:
    print(sem_refeicao)