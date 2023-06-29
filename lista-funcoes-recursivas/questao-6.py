#Cnk = (fat(n))/(fat(k))*(fat(n-k))
def fat(num):
    if num == 1:
        return 1
    else:
        return num*(fat(num-1))


def comb(n,k):
    if n == k:
        return 1
    if k == 1:
        return n
    else:
        combinacao = ((fat(n-1))/(fat(k-1))*(fat(n-1)-(k-1))) + (fat(n-1))/(fat(k))*(fat((n-1)-k))
        return combinacao
