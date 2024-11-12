# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.
minutos_totais = int(input("Digite o número de minutos: "))

def minutos_para_horas_e_minutos(minutos_totais):
    horas = minutos_totais // 60
    minutos = minutos_totais-(horas *60)
    resultado = {
        "horas": horas,
        "minutos":minutos
    }
    return resultado

def horas_e_minutos_para_minutos(horas,minutos):
    minutos_totais  =horas*60 + minutos
    return minutos_totais

horas_e_minutos = minutos_para_horas_e_minutos(minutos_totais)
print(f"{minutos_totais} minutos são equivalentes a {horas_e_minutos["horas"]} horas e {horas_e_minutos["minutos"]} minutos.")

minutos= int(input("Digite o número de minutos: "))
horas = int(input("Digite o número de horas: "))
print(f"O total em minutos é de {horas_e_minutos_para_minutos(horas,minutos)}")
