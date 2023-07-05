quant = int(input())
palavra = input()

def ocorrencias_a(seq):
    mono = 0
    pal = []
    pal = seq.split('b')
    for i in pal:
        if len(i) > 1:
            mono += len(i)
    return mono

print(ocorrencias_a(palavra))
