nome = input()
horas = int(input())
valor = float(input())
salario = horas * valor

print(nome)
print("R$ {:.2f}".format(salario))