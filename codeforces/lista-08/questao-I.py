fim = False
caso = 1

while not fim:
    try:
        digitos = int(input())
        teclas_ol = list(map(float,input().split()))
        senha = ""

        for x in range(digitos):
            indice_maior = teclas_ol.index(max(teclas_ol))
            senha = senha + str(indice_maior)
            teclas_ol[indice_maior] = 0
        print("Caso {}: {}".format(caso,senha))
        caso += 1
    except EOFError:
        fim = True