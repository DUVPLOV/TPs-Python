# Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

def criar_a_sua_historia():
    print("Bem-vindo à aventura na floresta encantada!")
    print("Você se encontra em uma bifurcação na floresta.")
    
    escolha_1 = input("Você quer seguir o caminho da esquerda (digite 'esquerda') ou o da direita (digite 'direita')? ").strip().lower()
    
    if escolha_1 == "esquerda":
        print("\nVocê escolheu o caminho da esquerda e encontra uma ponte sobre um rio.")
        
        escolha_2 = input("Você atravessa a ponte (digite 'atravessar') ou decide explorar a margem do rio (digite 'explorar')? ").strip().lower()
        
        if escolha_2 == "atravessar":
            print("\nAo atravessar a ponte, você encontra um baú de tesouro!")
            print("Parabéns! Você termina sua aventura com um tesouro valioso.")
        elif escolha_2 == "explorar":
            print("\nVocê explora a margem do rio e encontra um grupo de fadas amigáveis.")
            print("As fadas compartilham suas sabedorias com você. Você termina sua aventura com novos amigos e conhecimentos.")
        else:
            print("\nEscolha inválida. Sua aventura termina sem um final claro.")
    
    elif escolha_1 == "direita":
        print("\nVocê escolheu o caminho da direita e encontra uma caverna escura.")
        
        escolha_2 = input("Você entra na caverna (digite 'entrar') ou decide continuar pela floresta (digite 'continuar')? ").strip().lower()
        
        if escolha_2 == "entrar":
            print("\nDentro da caverna, você encontra um dragão adormecido.")
            print("Você termina sua aventura após ter visto um dragão de perto!")
        elif escolha_2 == "continuar":
            print("\nVocê continua pela floresta e encontra uma vila escondida.")
            print("Os moradores te receberam calorosamente. Você termina sua aventura com novos amigos.")
        else:
            print("\nEscolha inválida. Sua aventura termina sem um final claro.")
    
    else:
        print("\nEscolha inválida. Sua aventura termina antes de começar.")

criar_a_sua_historia()
