print('-'* 25)
print('Sequência de Fibonacci')
print('-'* 25)
termos = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2} ', end='')
cont = 3
while cont <= termos:
    n3 = n1 + n2
    print(f'-> {n3}', end='')
    n1 = n2
    n2 = n3
    cont += 1
print('-> FIM')