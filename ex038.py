n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O \033[33m primeiro valor\033[m é \033[34m maior')
elif n2 > n1:
    print('O \033[33m segundo valor \033[33m é \033[34m maior')
else:
    print('\033[33m Não existe \033[m valor maior, os dois são iguais.')
