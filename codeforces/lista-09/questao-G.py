tautograma = list(map(str,input().split()))
verdadeiro = False

while tautograma[0] != '*':
    letra = (tautograma[0])[0].upper()
    for palavra in tautograma:
        primeira_letra = palavra[0].upper()
        if primeira_letra == letra:
            verdadeiro = True
        else:
            verdadeiro = False
            break
    if verdadeiro:
        print('Y')
    else:
        print('N')
    tautograma = list(map(str,input().split()))