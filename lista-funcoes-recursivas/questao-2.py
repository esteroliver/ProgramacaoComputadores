def calc(num,div):
    if div == 1:
        return 1
    divs = 0
    if num%div == 0:
        divs += 1
    divs += calc(num,div-1)
    return divs

def primo(num):
    num_primo = calc(num,num)
    if num_primo > 2:
        return 'Não Primo'
    else:
        return 'Primo'