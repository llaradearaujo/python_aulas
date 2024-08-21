import os
os.system("cls || clear")

#declarando variaveis
login_salvo = "email"
senha_salva = "1234"

#solicitando dados
login = input("digite o login:")
senha = input("digite a senha:")

#verificar
if login == login_salvo and senha == senha_salva:
    print("bem vindo!")
else:
    print("login ou senha invalidos")
 