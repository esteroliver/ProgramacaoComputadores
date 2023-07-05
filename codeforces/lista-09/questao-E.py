palavra = list(input())
mono = 0
for i in range(len(palavra)):
    try:
        if palavra[i] == palavra[i+1]:
            mono += 1
    except:
        break

print(mono)