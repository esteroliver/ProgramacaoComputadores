num = int(input())
 
for i in range(num):
    troco = []
    troco_elemento = 0
    dinheiro, marcas = map(int,input().split())
    precos = list(map(float,input().split()))
 
    for x in precos:
        preco_fixo = x
 
        while dinheiro >= x:
            x = x + preco_fixo
 
        troco_elemento = dinheiro - (x - preco_fixo)
        
        if troco_elemento == dinheiro:
            troco.append(0)
        else:
            troco.append(troco_elemento)
 
    print("{:.2f}".format(max(troco)))

