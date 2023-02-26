import os

# Lê o arquivo e coloca todas as linhas em um array
with open(os.path.dirname(os.path.abspath(__file__)) + '/entrada.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    pares = [entrada.strip() for entrada in linhas]

#### PARTE 01 ####
quantidade = 0
for entrada in pares:
    entrada1, entrada2 = entrada.split(',')

    # 1 e 2
    inicio_a1, fim_a1 = map(int, entrada1.split('-'))
    inicio_b1, fim_b1 = map(int, entrada2.split('-'))

    # 2 e 1
    inicio_a2, fim_a2 = map(int, entrada2.split('-'))
    inicio_b2, fim_b2 = map(int, entrada1.split('-'))

    if (inicio_b1 <= inicio_a1 and fim_a1 <= fim_b1) or (inicio_b2 <= inicio_a2 and fim_a2 <= fim_b2):
        quantidade += 1

print("Parte 1: "+str(quantidade))

#### PARTE 02 ####
sobreposicao = 0
for entrada in pares:
    entrada1, entrada2 = entrada.split(',')
    inicio_a, fim_a = map(int, entrada1.split('-'))
    inicio_b, fim_b = map(int, entrada2.split('-'))
    if inicio_a in range(inicio_b, fim_b+1) or fim_a in range(inicio_b, fim_b+1) or inicio_b in range(inicio_a, fim_a+1) or fim_b in range(inicio_a, fim_a+1):
        sobreposicao += 1

print("Parte 2: "+str(sobreposicao))
