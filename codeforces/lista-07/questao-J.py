quant = int(input())
numeros = []
result = 1

for i in range(quant):
    num = int(input())
    numeros.append(num)

for x in range(quant):
    try:
        if numeros[x] != numeros[x+1]:
            result += 1
    except:
        break

print(result)