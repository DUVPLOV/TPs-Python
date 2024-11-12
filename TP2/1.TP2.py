# Faça um programa que leia uma sequência de caracteres terminada por um ponto (.) e mostre o número de vogais digitadas.
# Cada caractere deve ser digitado/lido separadamente.
def Criar_lista_de_caracteres():
    lista_de_caracteres = []
    print("Para finalizar a sua lista/sequência de caracteres digite ponto final (.)")
    caractere = input("Digite um caractere: ")
    while(caractere!="."):
        lista_de_caracteres.append(caractere)
        caractere = input("Digite um caractere: ")
    print("Sequência finalizada!")
    return lista_de_caracteres
def Quantidades_de_vogais_na_lista(lista):
    vogais = 0
    for caractere in lista: 
        if(caractere.lower() in ["a","e","i","o","u"]):
            vogais+=1
    print(f"Existem {vogais} vogais na lista.")

lista = Criar_lista_de_caracteres()
Quantidades_de_vogais_na_lista(lista)