#questão 01
lista = list(map(int,input().split()))
print(lista[0])

#questão 02
lista = list(map(int,input().split()))

reverter = [lista[0],lista[1]]
reverter.reverse()

lista[0] = reverter[0]
lista[1] = reverter[1]

print(*lista, sep=", ")

#questão 03
n1, n2, n3, n4, n5 = map(int,input().split())
numeros = [n1,n2,n3,n4,n5]

print(numeros[0],numeros[4])

#questão 04
n1, n2, n3, n4, n5, n6, n7, n8 = map(int,input().split())
numeros = [n8,n2,n3,n4,n5,n6,n7,n1]
print(*numeros, sep=", ")

#questão 05
numeros = list(map(int,input().split()))
num = int(input())
numeros.append(num)
print(*numeros, sep=", ")

#questão 06
numeros = list(map(int,input().split()))
print(len(numeros))

#questão 07
numeros = list(map(int,input().split()))
quant = len(numeros)
print(quant,numeros[0],numeros[quant-1])

#questão 08
numeros = list(map(int,input().split()))
print(min(numeros),max(numeros))

#questão 09
numeros = list(map(int,input().split()))
soma = sum(numeros)
print(soma)

if soma%2 == 0:
    print('Par')
else:
    print('Ímpar')

#questão 10
numeros = list(map(int,input().split()))
soma = sum(numeros)
quant = len(numeros)

if soma%quant == 0:
    print('Sim')
else:
    print('Não')

#questão 11
numeros = list(map(int,input().split()))
quant = len(numeros)

if quant%2 == 0:
    quant = quant//2
    soma = numeros[quant] + numeros[quant-1]
    print(soma/2)

else:
    quant = quant//2
    print(numeros[quant])

#questão 12
frase = list(input().split())
print(len(frase))