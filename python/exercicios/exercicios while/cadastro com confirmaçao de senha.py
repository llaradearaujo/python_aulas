import os
os.system("cls || clear")

while True:
    senha = input("digite sua nova senha: ")
    confirmacao_senha = input("confirme sua senha: ")
    if senha == confirmacao_senha:
        print("nova senha criada com sucesso!")
        break
    else:
        print("senhas não coincidem.")
        print("tente novamente!")