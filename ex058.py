from random import randint
from time import  sleep
tentativas = 1
computador = randint(0,10) #Faz o sorteio dos números
print('-=-'*20)
print('Pensei em um número entre 0 e 10...Tente adivinhar! ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
while jogador != computador:
    jogador = int(input('Ops, reposta errada. Em que número eu pensei? '))
    tentativas += 1
    print('PROCESSANDO...')
    sleep(1)
print(f'Parabéns! O número que pensei foi {computador}. Voce adivinhou em {tentativas} tentativas.')

