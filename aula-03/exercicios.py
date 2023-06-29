#questão 01
numero = int(input())
print("Próximo: {:03d}".format(numero))

#questão 02
salario = float(input())
reajuste = float(input())
novo_salario = salario + (salario*(reajuste/100))
print("Atual:",salario)
print("Novo : {:.2f}".format(novo_salario))

#questão 03
pi = 3.14159
raio = int(input())
area = pi * (raio**2)

print("{:.4f}".format(area))

#questão 04
valor_final = float(input())
sem_impostos = valor_final/1.4
icms = sem_impostos * (18/100)
ipi = sem_impostos * (13/100)
pis = sem_impostos * (1.4/100)
cofins = sem_impostos * (7.6/100)

print("ICMS: {:.2f}\nIPI: {:.2f}\nPIS: {:.2f}\nCofins: {:.2f}\nValor sem impostos: {:.2f}".format(icms,ipi,pis,cofins,sem_impostos))

