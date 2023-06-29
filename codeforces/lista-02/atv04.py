item = int(input())
quant = int(input())
pagamento = int(input())
total = item*quant
troco = pagamento - total

print("A pagar:",total)
print("Troco  :",troco)