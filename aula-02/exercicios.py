#questão 01
print("Meu primeiro programa (lá ele)")

#questão 02
print("Avenida Senador Salgado Filho, 1559, \nTirol, Natal-RN, Brasil \nCEP: 59015-000 \ne-mail: ccs.cnat@ifrn.edu.br \nTelefone: 4005-2600")

#questão 03
nome = input()
print("Oi ",nome,", bom dia!",sep="")

#questão 04
num1 = int(input())
num2 = int(input())
soma = num1+num2
print(soma)

#questão 05
num1 = float(input())
num2 = float(input())
media = (num1+num2)/2
print(media)

#questão 06
n1,n2 = input().split()
nota1 = float(n1)
nota2 = float(n2)
media = (nota1*2 + nota2*3)/5
print(media)

#questão 07
num1 = float(input())
num2 = float(input())
num3 = float(input())
produto = num1 * num2 * num3
print(produto)

#questão 08
hora1 = int(input("Minutos do início do evento:"))
hora2 = int(input("Minutos do fim do evento:"))
tempo_h = (hora2 - hora1)//60
tempo_min = (hora2 - hora1)%60
print("{}:{}".format(tempo_h,tempo_min))

#questão 09
tempo = int(input("Quantos dias se passaram?"))
semanas = tempo//7
dias = tempo%7
print("Se passaram {} semana(s) e {} dia(s).".format(semanas,dias))

#questão 10
valor = int(input("Digite o valor do produto. "))
quant = int(input("Digite a quantidade do produto. "))
pag = int(input("Quanto você irá pagar? "))
total = (valor*quant)
troco = pag - total
print("A pagar:",total)
print("Troco  :",troco)

#questão 11
dist = float(input("Qual a distância, em km, da cidade A até a cidade B? "))
veloc = float(input("Qual a velocidade, em km/h, do carro? "))
tempo = dist/veloc
horas = int(tempo//1)
minutos = int((tempo%1)*60)
print("{}:{}".format(horas,minutos))

#questão 12
dist_rua = int(input("Distância da rua (em km) "))
dist_poste = int(input("Distância entre dois postes (em metros) "))
postes = (dist_rua * 1000)//dist_poste 
ults = (dist_rua * 1000)%dist_poste
quant_poste = postes + 1
if ults > 0:
    print("{} postes.\n{} metros".format(quant_poste + 1,ults))
else: 
    print("{} postes.\n{} metros".format(quant_poste,ults))