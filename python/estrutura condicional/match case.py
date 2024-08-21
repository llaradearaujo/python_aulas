import os
os.system("cls || clear")
#mostrar opções
print(""" 
1 - cadastrar usuário
2 - excluir usuário
3 - sair do sistema
""")
#coletar opção desejada(declarar variável opção)
opcao = int(input("digite uma opção"))

#definir opções MATCH: abre comando de opções CASE: registro de opções possíveis
match(opcao):
    case 1:
        print("opção de cadastrar usuário")
    case 2:
        print("opção de excluir usuário")
    case 3:
        print("opção de sair do sistema")
    case _:
        print("opção inválida")