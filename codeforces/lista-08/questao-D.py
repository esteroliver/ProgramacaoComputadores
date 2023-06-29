num = int(input())
num_primo = num+1

def primo(num):
    divs = 0
    for i in range(1,num+1):
        if num%i == 0:
            divs += 1
    if divs == 2:
        return True
    else:
        return False

while not primo(num_primo):
    num_primo += 1

print(num_primo)