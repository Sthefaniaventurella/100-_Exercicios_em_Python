velocidade = float(input('Em qual velocidade o carro estava? \n km/h: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Voce estava acima da velocidade permitida que é 80km/h! \n Voce receberá uma multa no valor de {multa:.2f}')
else:
    print('Voce não ultrapassou a velocidade permitida.')
