num = int(input())
numeros = list(map(int,input().split()))
escadinhas = 1

if len(numeros) <= 2:
    escadinhas = 1
    
else:
    for i in range(1, len(numeros)-1):
        if abs(numeros[i-1] - numeros[i]) != abs(numeros[i] - numeros[i+1]):
            escadinhas += 1

print(escadinhas)