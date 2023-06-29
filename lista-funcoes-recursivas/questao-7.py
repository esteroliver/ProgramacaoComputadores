def divisores(num,div):
    if div == 1:
        return [1]
    else:
        divs = divisores(num,div-1)
        if num%div == 0:
            divs.append(div)
        return divs