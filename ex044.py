produto = float(input('Digite o valor da compra: R$'))
print('[1] - Á vista/ Cheque \n' # 10% de desconto
      '[2] - Á vista no cartão \n' # 5% de desconto
      '[3] - Em até 2x no cartão \n' # Preço normal
      '[4] - 3x ou mais no cartão \n') # 20% de juros
pagamento = int(input('Qual será a forma de pagamento? '))
if pagamento == 1:
    print(f'Você ganhou 10% de desconto! Valor total a pagar: {produto - (produto * 10) / 100 :.2f}')
elif pagamento == 2:
    print(f'Você ganhou 5% de desconto! Valor total a pagar: {produto - (produto * 5) / 100 :.2f}')
elif pagamento == 3:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra de {produto:.2f} será parcelada em {parcelas}x de R${produto/parcelas :.2f} SEM JUROS!')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = produto + (produto * 20 / 100)
    totparc = total / parcelas
    print(f'Sua compra será parcelada em {parcelas} de {totparc:.2f} COM JUROS\n'
          f'Sua compra de {produto} vai custar {total:.2f} no final')


