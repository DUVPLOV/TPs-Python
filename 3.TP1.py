# Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

def nome_combinado(nome1,nome2):
    if(len(nome1.split(" "))>=2):
        nome_criativo = (nome2 +" "+ nome1.split(" ")[1]).capitalize()
    elif((len(nome2.split(" "))>=2)):
        nome_criativo = (nome1 +" "+ nome2.split(" ")[1]).capitalize()
    else:
        metade1 = nome1[:len(nome1) // 2]
        metade2 = nome2[len(nome2) // 2:]
        nome_criativo = metade1 + metade2

    return nome_criativo.capitalize()

nome1 = input("Digite um nome de usuário: ")
nome2 = input("Digite outro nome de usuário: ")
print(f"Uma possível combinação dos é {nome_combinado(nome1,nome2)}")