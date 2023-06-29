a, b = map(int,input().split())
divs = []

for i in range (a,b+1):
    if i%a == 0:
        divs.append(i)

print(*divs)