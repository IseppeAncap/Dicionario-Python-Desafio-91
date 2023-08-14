
# Definição de cores para outupt
reset = '\033[0m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
magenta= '\033[35m'
ciano = '\033[36m'
# Apresentação.
print(f'{azul} {"Seja bem vindo":>25} {reset}')
print(f'{amarelo} {"Chamada da Sorte"::^25} {reset}')
print(f'Esse programa simula uma disputa entre 4 jogadores num jodo de 🎲,',end=' ') 
print('adiciona esses valores a um dicionario exibi um raking ao final!')
print()
## Etapa 1- Declarando algumas estruturas.

import random # biblioteca para chamar metodo 
import time # Biblioteca para chamar metodó sleep
# Cria um diconário vazio, para guardar 4 par de chave:valor
sorteio = {}
pos = 0 # Contador para posição
## ETAPA 2 Preenchendo o dicionário com Valores Sorteados
# laço para 4 jogadores.
for i in range(1,5):  
    nome_jogador = 'jogador'+ str(i) # Criar o nome para chave
    # Gera u número aleátorio , adiciona a chave e o valor, ao dicionário temporário
    dados= {nome_jogador:random.randint(1,6)}
    sorteio.update(dados) # Atualiza o diconário alvo
print(f'{vermelho} {"Valores Sorteados":^45} {reset}')
# Exibi o resultado para cada jogador.
for k, v in sorteio.items():
    print(f'O {k} tirou {ciano}{v}{reset} 🎲')
    time.sleep(.5)
print()
# Exibi um ranking o maior valor em ordem decrescente!
print(f'\n{":"::>20}{magenta}{"Ranking":^10}{reset}{":"::<20}')
##ETAPA 4
# Loop para iterar os resultado com base nos resultados!
for resultado in sorted(sorteio, key=sorteio.get, reverse=True):
    pos +=1 # incrementa o valor a posição 
    if pos == 1:
        print(f'🥇{pos}{verde} Posiçãoª {reset}: {resultado} com {ciano} {sorteio[resultado]}{reset} 🎲')
    elif pos ==2:
        print(f'🥈{pos}{verde} Posiçãoª {reset}: {resultado} com {ciano} {sorteio[resultado]}{reset} 🎲')
    elif pos == 3:
        print(f'🥉{pos}{verde} Posiçãoª {reset}: {resultado} com {ciano} {sorteio[resultado]}{reset} 🎲')
    else:
        print(f'😭{pos}{verde} Posiçãoª {reset}: {resultado} com {ciano} {sorteio[resultado]}{reset} 🎲')
    print('---'*10)
    time.sleep(.5)

print(f'Obrigado Pro usar nosso Programa!')
print('-=-=-'*10)
