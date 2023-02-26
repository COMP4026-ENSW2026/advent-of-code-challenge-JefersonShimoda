import os

#### PARTE 01 ####

# Lê o arquivo e coloca todas as linhas em um array
with open(os.path.dirname(os.path.abspath(__file__)) + '/entrada.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    calorias = [entrada.strip() for entrada in linhas]
 
# Percorre o array somando as calorias por elfo
elfo = []
soma = 0
for entrada in calorias:
    if entrada == "":
        elfo.append(soma)
        soma = 0
    else:
        soma += int(entrada)

# Se a soma atual for maior que 0, insere no array também
if(soma > 0):
    elfo.append(soma)

# Imprime a maior soma
print(max(elfo))

#### PARTE 02 ####

# Ordena o array de forma descrescente e soma os 3 primeiros índices
elfo.sort(reverse=True)
print(elfo[0]+elfo[1]+elfo[2])