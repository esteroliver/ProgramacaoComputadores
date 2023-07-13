sequencia = list(input())
a = sequencia.count("A")
c = sequencia.count("C")
g = sequencia.count("G")
t = sequencia.count("T")
quantidade = [a,c,g,t]
print(max(quantidade))