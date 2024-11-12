# Uma progressão aritmética (PA) é uma sequência numérica onde cada termo, a partir do segundo, é igual à soma do termo anterior com uma constante.
# A constante é a diferença entre o segundo e o primeiro número.
# Faça um programa que receba dois números inteiros e, a partir dessa informação, gere uma sequência em PA.
def Criar_progressao_aritmetica():
    progressao_aritmetica=[]
    num1 = float(input("Digite o primeiro elemento da PA: "))
    num2 = float(input("Digite o segundo elemento da PA: "))
    progressao_aritmetica.extend([num1,num2])
    dif = num2-num1
    for i in range(10):
        num2+=dif
        progressao_aritmetica.append(num2)
    return progressao_aritmetica
print(Criar_progressao_aritmetica())