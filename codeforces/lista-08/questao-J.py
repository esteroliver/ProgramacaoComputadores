iram, voltaram = map(int,input().split())
lista_voltaram = list(map(int,input().split()))
lista_iram = []

for i in range(iram):
    lista_iram.append(i+1)

for j in range(voltaram):
    lista_iram.remove(lista_voltaram[j])

lista_iram.sort()

if len(lista_iram) == 0:
    print("*")

else:
    print(*lista_iram,"")