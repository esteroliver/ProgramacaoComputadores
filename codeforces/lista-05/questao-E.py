agua = int(input())
total = 7
if agua <= 10:
    print(total)
else:
    if agua >= 101:
        for k in range(100,agua):
            total += 5
        for y in range(31,101):
            total += 2
        for z in range(11,31):
            total += 1
    
    elif agua >= 31 and agua <= 100:
        for j in range(30,agua):
            total += 2
        for x in range(11,31):
            total += 1

    elif agua >= 11 and agua <= 30:
        for i in range(10,agua):
            total += 1
    print(total)