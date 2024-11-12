# Faça um programa que calcule a soma e a média dos números de 1 a 100.
def Media_e_soma_ate_cem():
    soma = 0
    for i in range(1,101):
        soma+= i
    print(f"Soma: {soma}")
    print(f"Média: {soma/100}")

Media_e_soma_ate_cem()