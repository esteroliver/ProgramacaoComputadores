charr1, metros1, veloc1 = map(int,input().split())
charr2, metros2, veloc2 = map(int,input().split())

tempo1 = metros1/veloc1
tempo2 = metros2/veloc2

if (tempo1<tempo2):
    print(charr1)
else:
    print(charr2)