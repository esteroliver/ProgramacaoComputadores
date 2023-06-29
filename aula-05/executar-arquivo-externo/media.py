'''
NO TERMINAL:
cmd
cd aula-05/executar-arquivo-externo
media.py < notas.txt
'''
notas = list(map(int,input().split()))
media = sum(notas)/len(notas)
print(media)