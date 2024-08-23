import os
os.system ("cls || clear")

valor = float(input("digite o valor da  compra: "))
print("forma de pagamento(1-á vista; 2-á prazo)")
pagamento = int(input("digite o número correspondente a forma de pagamento: "))


#pagamento á prazo
if pagamento == 2:
    parcelas = int(input("numero de parcelas: "))



#exibindo dados
print("INFORMAÇÕES DA COMPRA: ")
match pagamento:
    case 1:
        desconto = valor*0.01
        pag_vista = valor-desconto

        print(f"valor do produto: R${valor}")
        print(f"forma de pagamento: á vista")
        print(f"valor do desconto: R${desconto}")
        print(f"total á pagar: R${pag_vista}")

    case 2:

        valor_parcela = valor/parcelas

        print(f"valor do produto: R${valor}")
        print(f"forma de pagamento: á prazo")
        print(f"quantidade de parcelas: {parcelas}")
        print(f"valor por parcela: {valor_parcela:.2f}")
        print(f"total á pagar: R${valor:.2f}")

#2f serve para determinar o numero de casas depois da virgula
