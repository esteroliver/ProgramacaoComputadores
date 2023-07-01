while True:
    n, m = map(str,input().split())
    if n == '0' and m =='0':
        break
    else:
        n_list = list(n)
        m_list = list(m)
 
        soma_n = 0
        string_soma_n = ''
 
        soma_m = 0
        string_soma_m = ''
 
        while len(n_list) >= 1:
            n = list(map(int,n_list))
            soma_n = sum(n)
            string_soma_n = str(soma_n)
            n_list = list(string_soma_n)
            if len(n_list) == 1:
                break
 
        while len(m_list) >= 1:
            m = list(map(int,m_list))
            soma_m = sum(m)
            string_soma_m = str(soma_m)
            m_list = list(string_soma_m)
            if len(m_list) == 1:
                break
 
        if soma_n > soma_m:
            print(1)
        elif soma_n < soma_m:
            print(2)
        else:
            print(0)