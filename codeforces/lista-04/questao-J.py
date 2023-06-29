base = int(input())
topo = int(input())

comprimento = 160
altura = 70

lado_esquerdo = ((base + topo)*altura)/2
lado_direito = (((comprimento-base)+(comprimento-topo))*altura)/2

if (lado_direito > lado_esquerdo):
    print(2)
elif (lado_esquerdo > lado_direito):
    print(1)
else:
    print(0)
