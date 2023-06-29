num1 = int(input())
num2 = int(input())
div = 0

if (num1 > num2):
    if(num1%num2 == 0):
        print("Multiplos")
    else: 
        print("Nao multiplos")

else:
    if(num2%num1 == 0):
        print("Multiplos")
    else: 
        print("Nao multiplos")
    
