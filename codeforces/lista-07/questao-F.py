num = int(input())
divs = 0

for i in range(1,num+1):
    if num%i == 0:
        divs += 1

if divs != 2:
    print('Nao')

else:
    print('Sim')