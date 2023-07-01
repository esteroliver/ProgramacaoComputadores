quant = int(input())
interruptores = list(map(int,input().split()))
a = 0
b = 0

for i in interruptores:
    if i == 1:
        if a == 0:
            a = 1
        else:
            a = 0
    if i == 2:
        if a == 0:
            a = 1
        else:
            a = 0
        if b == 0:
            b = 1
        else:
            b = 0

print(a)
print(b)