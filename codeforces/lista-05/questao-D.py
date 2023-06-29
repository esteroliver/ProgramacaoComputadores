monica = int(input())
filho1 = int(input())
filho2 = int(input())

filho3 = monica-(filho1+filho2)
filhos_monica = [filho1,filho2,filho3]
filhos_monica.sort()

print(max(filhos_monica))