distancia = int(input())
velocidade = int(input())
tempo = distancia/velocidade
horas = int(tempo//1)
minutos = int((tempo%1)*60)
print("{:02d}:{:02d}".format(horas,minutos))