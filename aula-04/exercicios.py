#questão 07
num1_7 = int(input())
num2_7 = int(input())
if num1_7>num2_7:
    print(num1_7)
else:
    print(num2_7)

#questão 08
num1_8 = int(input())
num2_8 = int(input())
num3_8 = int(input())
if (num1_8 < num2_7 and num1_8 < num3_8):
    print(num1_8)
elif (num2_8 < num1_8 and num2_8 < num3_8):
    print(num2_8)
elif (num3_8 < num1_8 and num3_8 < num2_8):
    print(num3_8)

#questão 09
num_9 = int(input())
if (num_9%2 == 0):
    print("Par")
else:
    print("Ímpar")

#questão 10
num1_10 = int(input())
num2_10 = int(input())
num3_10 = int(input())
num4_10 = int(input())
num5_10 = int(input())
maior = num1_10
if (maior <= num2_10):
    maior = num2_10
if (maior <= num3_10):
    maior = num3_10
if (maior <= num4_10):
    maior = num4_10
if (maior <= num5_10):
    maior = num5_10
print(maior)

#questão 11
num1_11 = int(input())
num2_11 = int(input())
num3_11 = int(input())
maior = num1_11

if (num2_11 > maior):
    maior = num2_11
if (num3_11 > maior):
    maior = num3_11

if (num1_11 < maior and num2_11 < maior):
    soma = num1_11 + num2_11
    if (soma > maior):
        print("Maior")
    else:
        print("Não maior")
elif (num2_11 < maior and num3_11 < maior):
    soma = num3_11 + num2_11
    if (soma > maior):
        print("Maior")
    else:
        print("Não maior")
elif (num1_11 < maior and num3_11 < maior):
    soma = num3_11 + num1_11
    if (soma > maior):
        print("Maior")
    else:
        print("Não maior")

#questão 12
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if (lado1 == lado2 and lado2 == lado3):
    print("Equilátero")

elif ((lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado1 == lado3 and lado3 != lado2)):
    print("Isósceles")

elif (lado1 != lado2 and lado2 != lado3):
    print("Escaleno")

else:
    print("Nenhum5")

#questão 13
dia = int(input())
mes = int(input())
ano = int(input())

if (mes <= 12 and mes > 0):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31 and dia > 0):
            print("valida")
        else: 
            print("invalida")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30 and dia > 0):
            print("valida")
        else:
            print("invalida")
    elif (mes == 2):
        if (dia <= 28 and dia > 0):
            print("valida")
        else:
            print("invalida")
else:
    print("invalida")

#questão 14
dia = int(input())
mes = int(input())
ano = int(input())

if (mes <= 12 and mes > 0):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia < 31 and dia > 0):
            print("{}/{}/{}".format(dia+1,mes,ano))
        elif (dia == 31):
            print("01/{}/{}".format(mes+1,ano))
        else:
            print("data invalida")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia < 30 and dia > 0):
            print("{}/{}/{}".format(dia+1,mes,ano))
        elif (dia == 30):
            print("01/{}/{}".format(mes+1,ano))
        else:
            print("data invalida")
    elif (mes == 2):
        if (dia < 28 and dia > 0):
            print("{}/{}/{}".format(dia+1,mes,ano))
        elif (dia == 28):
            print("01/{}/{}".format(mes+1,ano))
        else:
            print("data invalida")
else:
    print("invalida")

#questão 15
a,b = map(int,input().split())
sub = 0
mov = 0

if (a != b):
    if (a > b):
        sub = a - b
        while (a != b):
            if (sub%2 == 0):
                a -= sub
                mov += 1
            else: 
                a -= b
                mov += 1
            if (a < b):
                a += 1
                mov += 1
        print(mov)
    if (a < b):
        while (a != b):
            a += 1
            mov += 1
        print(mov)
elif (a == b):
    print(mov)