# Desenvolva um programa que aplique descontos progressivos com base no valor da compra: 
# desconto de 10% para compras acima de R$100, 
# 15% para compras acima de R$200, seguindo a projeção até R$500,
#  para valores maiores do que esse, o desconto é fixado em 25%.

def calcular_desconto(valor_compra):
    if valor_compra > 100 and valor_compra<= 200:
        print(f"Com um desconto de R$ {valor_compra*0.1:.2f} (10%), o valor final do item é R$ {valor_compra*0.90:.2f}")
    elif valor_compra > 200 and valor_compra <= 500:
        print(f"Com um desconto de R$ {valor_compra*0.15:.2f} (15%), o valor final do item é R$ {valor_compra*0.85:.2f}")
    elif valor_compra>500:
        print(f"Com um desconto de R$ {valor_compra*0.25:.2f} (25%), o valor final do item é R$ {valor_compra*0.75:.2f}")
    else:
        print(f"Valor baixo, não possui desconto. Continua sendo R${valor_compra}")
valor_compra = float(input("Digite o valor da compra em R$: "))
calcular_desconto(valor_compra)