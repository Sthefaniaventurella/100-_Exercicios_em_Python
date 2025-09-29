from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
escolha = 0
while escolha != 5:
    print('[1] somar \n'
    '[2] multiplicar \n'
    '[3] maior \n'
    '[4] novos números \n'
    '[5] sair do programa \n')
    escolha = int(input('>>>>>> Qual é a sua opção: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else: maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 30)
    sleep(2)
print('Fim do programa! Volte sempre!')

