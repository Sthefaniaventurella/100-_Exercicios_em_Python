nota1 = float(input('Insira sua 1° nota: '))
nota2 = float(input('Insira sua 2° nota: '))
média = (nota1 + nota2) / 2
if 7 > média >= 5:
    print('Recuperação. Você pode mais!')
elif média < 5:
    print('Reprovado. Sua nota está abaixo da média.')
elif média >= 7:
    print('Aprovado. Parabéns!')


