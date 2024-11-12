# Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.
import random

def votacao():
    escolha_usuario = input("Escolha um opção entre Paris, Rio de Janeiro e Istambul\nDigite o nome inteiro da cidade: ")
    opcoes = {
        "Paris":0,
        "Rio de janeiro":0,
        "Istambul":0
    }
    match escolha_usuario.lower().replace(" ",""):
        case "paris":
            opcoes["Paris"] +=1
        case "riodejaneiro":
            opcoes["Rio de janeiro"] +=1
        case "istambul":
            opcoes["Istambul"] +=1
        case _:
            print(f"Voto cancelado! A cidade {escolha_usuario} não é válida!")
    lista_de_chaves_de_opcoes = list(opcoes.keys())
    for i in range (4):
        cidade_aleatoria_escolhida = random.choice(lista_de_chaves_de_opcoes)
        opcoes[cidade_aleatoria_escolhida] +=1
    maior_valor = max(opcoes.values())
    cidades_mais_votadas = [k for k, v in opcoes.items() if v == maior_valor]
    if(len(cidades_mais_votadas)==1):
        print(f"A cidade mais votada foi {cidades_mais_votadas[0]} com {maior_valor} votos")
    else:
        print(f"Houve um empate! As cidades mais votadas foram {cidades_mais_votadas[0]} e {cidades_mais_votadas[1]} com {maior_valor} votos")
votacao()