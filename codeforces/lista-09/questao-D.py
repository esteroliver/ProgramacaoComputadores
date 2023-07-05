mensagem = list(input())
crib = list(input())
pas = 0
quant = len(mensagem) - len(crib) + 1

for i in range (quant):
    letras = 0
    for j in range(len(crib)):
        if crib[j] == mensagem[j]:
            letras += 1
    if letras == 0:
        pas += 1
    mensagem.remove(mensagem[0])
    
print(pas)
