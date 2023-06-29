v1, v2, v3, v4 = map(int,input().split())

if (v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2):
    print("S")
elif (v2 + v3 > v4 and v2 + v4 > v3 and v3 + v4 > v2):
    print("S")
elif (v1 + v3 > v4 and v3 + v4 > v1 and v1 + v4 > v3):
    print("S")
elif (v1 + v2 > v4 and v1 + v4 > v2 and v2 + v4 > v1):
    print("S")
else:
    print("N")