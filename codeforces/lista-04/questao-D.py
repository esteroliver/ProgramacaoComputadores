cons = int(input())
dist_km = int(input())
litros = int(input())

gasol = (dist_km/cons) - litros

if (gasol < 0):
    print(0.0)
else:
    print("{:.1f}".format(gasol))