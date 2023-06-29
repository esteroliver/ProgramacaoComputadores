senha = 9842
inserir_senha = int(input())

while inserir_senha != senha:
    print('Senha Invalida!')
    inserir_senha = int(input())

print('Acesso Permitido.')