# Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

def calssificar_palavras(palavras):
    for palavra in palavras.split(" "):
        if(len(palavra)<5):
            print(f"A palavra {palavra} é curta.")
        elif(len(palavra)>=5):
            print(f"A palavra {palavra} é longa.")

palavras = input("Digite uma frase para classificar todas as palavras: ")
calssificar_palavras(palavras)