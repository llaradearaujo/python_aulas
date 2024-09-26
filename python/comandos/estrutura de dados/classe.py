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

print("SOLICITANDO DADOS DE ALUNOS")

for i in range(quantidade_alunos):
    aluno = Aluno(
        nome = input("digite seu nome: "),
        idade = int(input("digite sua idade: "))
    )
    lista_alunos.append(aluno)

print("EXIBINDO DADOS DE ALUNOS")
for aluno in lista_alunos:
    print(f"nome = {aluno.nome}")
    print(f"idade = {aluno.idade}")


#salvando dados do aluno num  arquivo txt

#definindo arquivo para salvar os dados
nome_do_arquivo = "lista_alunos_senai.txt"

#abrindo arquivo e definindo que sera feito
with open(nome_do_arquivo, "w") as arquivo_alunos:
    
#percorrendo vetor e escrevendo no arquivo uma linha de cada vez
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")



print("dados salvos com sucesso!")