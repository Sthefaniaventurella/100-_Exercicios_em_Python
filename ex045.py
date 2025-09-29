from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 11)
print(f'O computador escolheu {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=-' * 11)
if computador == 0: # Computador joga PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('COMANDO INVÁLIDO. TENTE NOVAMENTE')
elif computador == 1: # Computador joga PAPEL
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('COMANDO INVÁLIDO. TENTE NOVAMENTE')
elif computador == 2: # Computador joga TESOURA
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    else:
        print('COMANDO INVÁLIDO. TENTE NOVAMENTE')



