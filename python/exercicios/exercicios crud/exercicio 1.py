import os
from dataclasses import dataclass

os.system("cls || clear")

#estrutura de dados
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTES = 4

lista_clientes = []
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input("digite seu nome: "),
        sobrenome = input("digite seu sobrenome: "),
        idade = int(input("digite sua idade: ")),
        peso = float(input("digite seu peso: ")),
        altura = float(input("digite sua altura: "))
    )
    lista_clientes.append(cliente)



#SALVAR EM UM ARQUIVO CHAMADO: carteira_de_clientes.txt
nome_do_arquivo = "carteira_de_clientes.txt"

#abrindo arquivo e definindo que sera feito
with open(nome_do_arquivo, "w") as arquivo_clientes:
    
#percorrendo vetor e escrevendo no arquivo uma linha de cada vez
    for aluno in lista_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.sobrenome}, {cliente.idade}, {cliente.peso}, {cliente.altura}")

arquivo_clientes.close()

#FAZER LEITURA DE DADOS DO ARQUIVO E MOSTRAR NO TERMINAL
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, sobrenome, idade, peso, altura = linha.strip().split(",")
        lista_clientes.append(Cliente(nome = nome, sobrenome = sobrenome, idade = int(idade), peso = float(peso), altura = float(altura)))

arquivo_clientes.close()

for cliente in lista_clientes:
    print(f"cliente.nome")
    print(f"cliente.sobrenome")
    print(f"cliente.idade")
    print(f"cliente.peso")
    print(f"cliente.altura")
        
        