from random import randint
from time import  sleep
computador = randint(0,5) #Faz o sorteio dos números
print('-#-'*20)
print('Pensei em um número entre 0 e 5...Tente adivinhar! ')
print('-#-'*20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Voce acertou!')
else:
    print(f'Ops...não foi dessa vez. Eu pensei no número {computador} e não no número {jogador}')
