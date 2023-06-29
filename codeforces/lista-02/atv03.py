nome = input()
salario = float(input())
vendas = float(input())
total = salario + ((vendas/100)*15)

print(nome.capitalize())
print("R$ {:.2f}".format(total))