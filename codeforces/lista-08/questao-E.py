num = int(input())

for i in range(num):
    kg = float(input())
    dias = 0
    while kg > 1:
        kg = kg/2
        dias += 1
    print(dias,"dias")