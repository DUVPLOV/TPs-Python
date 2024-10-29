# Desenvolva um programa que verifique se uma palavra ou texto inserida pelo usuário é um palíndromo (lê-se igual de trás para frente)
def palavra_palindromo(texto):
    texto_normalizado = texto.replace(" ", "").lower()     
    if(texto_normalizado == texto_normalizado[::-1]):
        print(f"O texto '{texto}' é um palíndromo.")
    else:
        print(f"O texto '{texto}' não é um palíndromo.")

texto = input("Digite uma palavra ou frase: ")
palavra_palindromo(texto)