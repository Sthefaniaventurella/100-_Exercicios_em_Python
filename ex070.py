print('=========== SUPERMERCADO DA TETY ===========')
total = maisdemil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=========== FIM DO PROGRAMA ===========')
print(f'O total de compra foi R${total:.2f}\n'
      f'Temos {maisdemil} produtos custando mais de R$1000.00.\n'
      f'O produto mais barato foi {barato} que custa R${menor}')
