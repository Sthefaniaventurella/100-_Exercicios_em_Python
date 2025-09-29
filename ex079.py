valores = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Esse valor não será adicionado pois ele já existe na sua lista.')
    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp == 'N':
        break
print(f'{sorted(valores)}')
