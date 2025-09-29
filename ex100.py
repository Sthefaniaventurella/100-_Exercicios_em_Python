from random import randint
from time import sleep

numeros = []
def sorteia(a):
    print(f'Sorteando 5 valores da lista:', end=' ')
    while len(a) < 5:
        valor = randint(1,10)
        if valor not in a:
            a.append(valor)
    for c in range(len(a)):
        print(a[c], end=' ')
        sleep(0.8)
    print('PRONTO!')


def somaPar(b):
    soma = 0
    for c in range(len(b)):
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {b}, temos {soma}')
sorteia(numeros)
somaPar(numeros)

