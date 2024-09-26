import os
os.system("cls || clear")
from dataclasses import dataclass

#crud
#create
#read
#update 
#delete

#estruturando dados
@dataclass
class Aluno:
    nome: str
    idade: int

quantidade_alunos = 2

lista_alunos = []

print("\nSOLICITANDO DADOS DE ALUNOS")

for i in range(quantidade_alunos):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade: "))
    )
    lista_alunos.append(aluno)

print("\nEXIBINDO DADOS DE ALUNOS")
for aluno in lista_alunos:
    print(f"nome = {aluno.nome}")
    print(f"idade = {aluno.idade}")

#------create-------
#salvando dados do aluno num  arquivo txt

#definindo arquivo para salvar os dados
nome_do_arquivo = "lista_alunos_senai.txt"

#abrindo arquivo e definindo que sera feito
with open(nome_do_arquivo, "w") as arquivo_alunos:
    
#percorrendo vetor e escrevendo no arquivo uma linha de cada vez
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")


#fechar conexao com arquivo
arquivo_alunos.close()


print("\ndados salvos com sucesso!")

lista_alunos = []

#------read-------
#lendo dados de um arquivo
print("\nACESSANDO DADOS DO ARQUIVO")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_alunos.append(Aluno(nome= nome, idade= int(idade)))




#fechando conexão com arquivo
arquivo_alunos.close()

print("\nEXIBINDO DADOS DOS ALUNOS DO ARQUIVO")
for aluno in lista_alunos:
    print(f"nome: {aluno.nome}")
    print(f"idade{aluno.idade}")