import os
os.system("cls||clear")

gasto_total = 0
orcamento = float(input("digite seu orcamento mensal: "))

while True:
    gastos_mensais = float(input("digite o valor gasto: "))
    gasto_total = gasto_total +gastos_mensais
    
    if gasto_total >= orcamento:
        break
        

excedente = gasto_total - orcamento
print(f"seu gasto final foi um total de R${gasto_total}")
print(f"o seu excedente de gastos foi de R${excedente}")