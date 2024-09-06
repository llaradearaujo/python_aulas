import os
os.system("cls || clear")

login_salvo = "marta"
senha_salva = "123"

for i in range(3):
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    
    if login == login_salvo and senha == senha_salva:
        print("bem vindo!")
        break
    else:
        print("login ou senha inválidos!")