cod,quant = map(int,input().split())

lanche1 = 4
lanche2 = 4.5
lanche3 = 5
lanche4 = 2
lanche5 = 1.5

total = 0

if (cod == 1):
    total = lanche1 * quant
elif (cod == 2):
    total = lanche2 * quant
elif (cod == 3):
    total = lanche3 * quant
elif (cod == 4):
    total = lanche4 * quant
elif (cod == 5):
    total = lanche5 * quant

print("Total: R$ {:.2f}".format(total))