mensagem = list(input())
crib = list(input())
pas = 0

while True:
    letras = 0
    for y in range(len(crib)):
        if crib[y] != mensagem[y]:
            letras += 1
    if letras == len(crib):
        pas += 1
    del(mensagem[0])
    if len(mensagem) < len(crib):
        break

print(pas)