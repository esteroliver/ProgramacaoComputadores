while True:
    a,b,c,d = map(int,input().split())
    horas = 0
    minutos = 0

    if a == 0 and b == 0 and c == 0 and d == 0:
        break

    if a < c:
        horas = (c - a)*60
        minutos = horas + (d-b)
    if a > c or a == c:
        horas = (24-a)+c
        minutos = horas*60 + (d-b)

    print(minutos)
        

    