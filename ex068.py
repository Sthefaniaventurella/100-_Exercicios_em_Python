from random import randint
print('='*25)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('='*25)
venceu = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Diga um valor: '))
    p_i = ' '
    while p_i not in 'PI':
        p_i = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    total = computador + jogador
    print('-'*20)
    if total % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} DEU {result}')
    if (result == 'PAR' and p_i == 'P') or (result == 'IMPAR' and p_i == 'I'):
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        venceu += 1
    else:
        print('VOCÊ PERDEU')
        print('='*20)
        print(f'GAME OVER! Você venceu {venceu} vezes.')
        break


