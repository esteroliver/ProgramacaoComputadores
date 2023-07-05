num = int(input())
medicoes = []
quant = 0

for i in range(num):
    bat = int(input())
    medicoes.append(bat)

media = sum(medicoes) // num

for x in medicoes:
    if x >= int(media * 0.9) and x <= int(media * 1.1):
        quant += 0
    else:
        quant += 1

print(media)
print(quant)
