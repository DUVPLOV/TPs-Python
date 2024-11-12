# Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo

import random
def adivinhar_numero_de_1_a_100():
    numero_aleatorio = random.randint(1, 100)
    palpite = int(input("Adivinhe um número entre 1 e 100: "))
    while palpite != numero_aleatorio:
        if (numero_aleatorio - palpite >=20):
            print("Muito baixo, tente novamente")
        elif (numero_aleatorio > palpite):
            print("Número baixo, tente novamente")
        elif (palpite -20 >= numero_aleatorio):
            print("Muito alto, tente novamente")
        elif (palpite> numero_aleatorio):
            print("Número alto, tente novamente")
        palpite = int(input("Adivinhe um número entre 1 e 100: "))

    print(f"Parabéns, você acertou!\nO número aleatório era {numero_aleatorio}")

adivinhar_numero_de_1_a_100()