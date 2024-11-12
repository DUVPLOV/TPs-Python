# Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
import random
personagens = ["astronauta", "princesa", "dragão", "robô", "detetive"]
acoes = ["encontrou um tesouro", "salvou o dia", "descobriu um segredo", "foi teletransportado", "perdeu seu chapéu"]
locais = ["na lua", "em um castelo encantado", "no fundo do mar", "em uma cidade futurista", "em uma ilha misteriosa"]

def criar_historia(personagens,acoes,locais):
    personagem = random.choice(personagens)
    acao = random.choice(acoes)
    local = random.choice(locais)
    
    historia = f"Era uma vez um {personagem} que {acao} {local}."
    return historia

print("História Gerada:")
print(criar_historia(personagens,acoes,locais))
