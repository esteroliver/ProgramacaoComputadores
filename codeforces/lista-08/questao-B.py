seg, massa = map(int,input().split())
segundos = seg
while massa >= 0.5:
    massa = massa//2
    seg += segundos

segundos = seg%60
minutos = (seg//60)%60
horas = ((seg//60)//60)%24
dias = ((seg//60)//60)//24


print('{} dias {:02d}:{:02d}:{:02d}'.format(dias,horas,minutos,segundos))