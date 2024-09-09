import os 
os.system("cls || clear")

def porcentagem(x):
   
    if x < 100:
        desconto = x + (x*0.1)
    else:
        desconto = x + (x*0.2)
    
    return desconto

preco = float(input("digite o preço do produto: "))

preco_final = porcentagem(preco)

print(f"o preço do produto inflacionado é R${preco_final}")