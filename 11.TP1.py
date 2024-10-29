# Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
import random

def jogar_dados(qntd_dados):
    lados_do_dado = [1,2,3,4,5,6]
    resultados = []
    for i in range(qntd_dados):
        resultados.append(random.choice(lados_do_dado))
    print(f"Os números/lados sorteados foram: {resultados}")
    
qntd_de_dados = int(input("Digite a quantidade de dados que deseja jogar: "))
jogar_dados(qntd_de_dados)