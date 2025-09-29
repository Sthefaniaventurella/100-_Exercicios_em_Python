from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print('Valores sorteados:')
for c in range(1,5):
    jogadores[f'Jogador{c}'] = randint(1, 6)
for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor}')
    sleep(1)
print('-'*25)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador} com {valor}')