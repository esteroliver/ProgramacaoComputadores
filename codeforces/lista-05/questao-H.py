a = int(input())
b = int(input())
c = int(input())
d = int(input())

amigos = []
amigos.extend([a,b,c,d])
amigos.sort()

dupla1 = amigos[0] + amigos[3]
dupla2 = amigos[1] + amigos[2]

if dupla1 > dupla2:
    print(dupla1-dupla2)
else:
    print(dupla2-dupla1)
