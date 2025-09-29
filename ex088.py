from random import randint
from time import sleep
print('-'*30)
print('      JOGO NA MEGA SENA      ')
print('-'*30)
resp = int(input('Quantos jogos você quer que eu sorteie? '))
if resp < 1:
    print('Erro: a quantidade minima é 1.')
else:
    print(f'SORTEANDO {resp} JOGOS')
    for c in range(resp):
        jogo = []
        while len(jogo) < 6:
            num = randint(1, 61)
            if num not in jogo:
                jogo.append(num)
        jogo.sort()
        print(f'Jogo {c+1}: {jogo}')
        print('=' * 30)
        sleep(1)
    print('-=-' * 3,'> BOA SORTE! <', '-=-' * 3)


