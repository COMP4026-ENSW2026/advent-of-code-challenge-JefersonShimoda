import os

# Lê o arquivo e coloca todas as linhas em um array
with open(os.path.dirname(os.path.abspath(__file__)) + '/entrada.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    rodadas = [entrada.strip() for entrada in linhas]

# Define as pontuações
ponto_por_movimento = {'Pedra': 1, 'Papel': 2, 'Tesoura': 3}
ponto_por_resultado = {'Perdeu': 0, 'Empatou': 3, 'Ganhou': 6}

#### PARTE 01 ####
# Mapeia o padrão
mapeamento = {'A': 'Pedra', 'B': 'Papel', 'C': 'Tesoura',
              'X': 'Pedra', 'Y': 'Papel', 'Z': 'Tesoura'}

# Soma a pontuação total das rodadas
soma = 0
for entrada in rodadas:
    oponente = mapeamento[entrada[0]]
    aliado = mapeamento[entrada[2]]

    if oponente == aliado:
        soma += (ponto_por_resultado['Empatou'] + ponto_por_movimento[aliado])
    elif (oponente, aliado) in [('Papel', 'Pedra'), ('Pedra', 'Tesoura'), ('Tesoura', 'Papel')]:
        soma += ponto_por_resultado['Perdeu'] + ponto_por_movimento[aliado]
    else:
        soma += ponto_por_resultado['Ganhou'] + ponto_por_movimento[aliado]

print("Parte 1: " + str(soma))

#### PARTE 02 ####
# Mapeia o padrão
mapeamento = {'A': 'Pedra', 'B': 'Papel', 'C': 'Tesoura',
              'X': 'Perdeu', 'Y': 'Empatou', 'Z': 'Ganhou'}

soma = 0
for entrada in rodadas:
    oponente = mapeamento[entrada[0]]
    objetivo = mapeamento[entrada[2]]

    if (oponente, objetivo) in [('Pedra', 'Empatou'), ('Papel', 'Perdeu'), ('Tesoura', 'Ganhou')]:
        soma += ponto_por_resultado[objetivo] + ponto_por_movimento['Pedra']
    elif (oponente, objetivo) in [('Pedra', 'Ganhou'), ('Papel', 'Empatou'), ('Tesoura', 'Perdeu')]:
        soma += ponto_por_resultado[objetivo] + ponto_por_movimento['Papel']
    else:
        soma += ponto_por_resultado[objetivo] + ponto_por_movimento['Tesoura']

print("Parte 2: " + str(soma))
