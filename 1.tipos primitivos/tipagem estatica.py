import os

os.system("cls || clear") #limpa o terminal

#tipagem estática
nome : str #cadeia
idade : int #inteiro
altura : float #real

nome = "marta"
idade = 20
altura = 1.80

print("nome: " + nome) #sinal de mais é aceito apenas na variável str
print(f"idade: {idade}") #nas outras deve-se seguirn este padrão
print(f"altura: {altura}")
#print equivale ao comando escreva