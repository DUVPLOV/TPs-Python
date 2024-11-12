# Faça um programa que leia um número do teclado e garanta que ele seja maior ou igual a zero.
# Enquanto a entrada não for válida, o programa deve exibir uma mensagem de erro e pedir uma nova entrada.
# Utilize apenas os comandos ensinados em aula.
def entrar_numero():
    try:
       num = float(input("Digite um número: "))
    except: 
        print("Erro: digite um número"),
    return num
def numero_maior_ou_igual_a_zero():
    num = entrar_numero()
    while(num<0):
        print("Erro: número inválido! Digite um número maior ou igual a zero")
        num = entrar_numero()
    print("Número válidado com sucesso!")
def executar_programa():
    numero_maior_ou_igual_a_zero()
executar_programa()