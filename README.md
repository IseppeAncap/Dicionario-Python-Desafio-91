
'''
Objetivo 91 
    Crie um programa onde 4ª jogadores, joguem um dado obtenham resultados
aléatorios.
Guarde esses resultados em um dicionário.
No final coloque esse dicionário em ordem decrescente .
Sabendo que o vencêndor tirou o maior número do dado.

Passo a passo
# Etapa 1 - Definindo algumas estruturas e variáveis

    . Importar as bibliotecas random e time.
    . Criar um dicionário "sorteio", que será atualizado a partir de outro dicionário "dados".
    . Utilizaremos um contador para exibir o valor da posição ao final.
-----------------------------------------------------------------------------------------------
## Etapa 2 - Preenchendo o dicionário com Valores Sorteados
    . Usaremos um laço para até 4 jogadores.
    . Como o nome da chave/key será "jogador1", teremos que converter o tipo da variável e concatená-la 
    e guardar esse valor.
    . Utilizamos o método "randint" para simular um sorteio de um dado, após isso adicionamos esse valor depois do nome
    chave/key.
    . Atualizamos o valor do dicionário "sorteio" a partir do dicionário "dados".
-----------------------------------------------------------------------------------------------
## Etapa 3 - Exibindo o sorteio.
    . Usamos um laço que itera sobre os itens key/values do dicionário {sorteio}.
    . Exibimos a mensagem "jogador1 tirou 4".
    . Usamos o método "sleep(.5)" para pausar entre essas iterações.
----------------------------------------------------------------------------------------------    
## Etapa 4 - Exibindo um Ranking, de acordo com os resultados do sorteio em ordem descrecente!

    . Começamos exibindo a mensagem (::::RANKING:::::).
    . Decidimos usar um laço "for" para percorrer cada elemento. Antes disso, usamos o método "sort" com o parâmetro "key" que especifica a função usada para extrair 
    uma chave de comparação dos elementos. 
    Nesse caso, usamos "sorteio.get" para obter o valor associado a cada chave. 
    O parâmetro "reverse=True" faz com que a ordenação seja feita em ordem decrescente.
    
    . Usando o contador para mostrar a posição do pódio, incrementamos +1 a cada iteração do resultado.
    . Exibimos a posição, chave e o valor.
    . Usamos também o método "sleep" para pausar a cada mensagem.
    . Implementamos o uso de um teste de decisão para imprimir a mensagem com emojis.
'''
            Seja bem vindo 
 ::::Chamada da Sorte::::: 
Esse programa simula uma disputa entre 4 jogadores num jodo de 🎲, adiciona esses valores a um dicionario exibi um raking ao final!

               Valores Sorteados               
O jogador1 tirou 1 🎲
O jogador2 tirou 6 🎲
O jogador3 tirou 6 🎲
O jogador4 tirou 6 🎲


:::::::::::::::::::: Ranking  ::::::::::::::::::::
🥇1 Posiçãoª : jogador2 com  6 🎲
------------------------------
🥈2 Posiçãoª : jogador3 com  6 🎲
------------------------------
🥉3 Posiçãoª : jogador4 com  6 🎲
------------------------------
😭4 Posiçãoª : jogador1 com  1 🎲
------------------------------
Obrigado Pro usar nosso Programa!



