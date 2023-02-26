import os

# Lê o arquivo e coloca todas as linhas em um array
with open(os.path.dirname(os.path.abspath(__file__)) + '/entrada.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    mochilas = [entrada.strip() for entrada in linhas]

#### PARTE 01 ####
soma = 0
for mochila in mochilas:
    primeira_metade = set(mochila[:len(mochila)//2])
    segunda_metade = set(mochila[len(mochila)//2:])
    sobreposicao = (primeira_metade.intersection(segunda_metade)).pop()
    if sobreposicao.isupper():
        soma += ord(sobreposicao) - ord('A') + 27
    else:
        soma += ord(sobreposicao) - ord('a') + 1

print("Parte 1: "+str(soma))

#### PARTE 02 ####
soma = 0
while len(mochilas) > 0:
    primeira_mochila = set(mochilas.pop())
    segunda_mochila = set(mochilas.pop())
    terceira_mochila = set(mochilas.pop())
    sobreposicao = ((primeira_mochila.intersection(segunda_mochila)).intersection(terceira_mochila)).pop()
    if sobreposicao.isupper():
        soma += ord(sobreposicao) - ord('A') + 27
    else:
        soma += ord(sobreposicao) - ord('a') + 1

print("Parte 2: "+str(soma))
