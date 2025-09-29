from time import sleep


def contador(i,f,p):
    print('-' * 30)
    print(f'Contando de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            cont += p
            sleep(0.6)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            cont -= p
            sleep(0.6)
        print('FIM!')


contador(1,10,1)
contador(10,0, 2)
print('Agora é a sua vez de personalizar a contagem!')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
contador(n1, n2, n3)

