while True:
    n, m = map(int,input().split())
    if n == 0 and m ==0:
        break
    else:
        while n >= 10:
            n = (n//10) + (n%10)

        while m >= 10:
            m = (m//10) + (m%10)
            
        if n > m:
            print(1)
        elif n < m:
            print(2)
        else:
            print(0)
    