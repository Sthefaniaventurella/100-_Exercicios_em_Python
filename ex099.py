from time import sleep
def maior(a):
    num = 0
    print('='*40)
    print('Analisando os valores passados...')
    for v in range(len(a)):
        print(a[v], end=' ')
        sleep(0.5)
    print(f'Foram informados {len(a)} valores ao todo.')
    for c in a:
        if c > num:
            num = c
    print(f'O maior valor informado foi {num}.')


valores = [2,9,4,5,7,1]
maior(valores)
valores = [4,7,0]
maior(valores)
valores = [1,2]
maior(valores)
valores = [6]
maior(valores)
valores = []
maior(valores)
