numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
          'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze','Treze', 'Quatorze', 'Quinze',
          'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
resp = 'S'
while resp == 'S':
    while True:
        escolha = int(input('Digite um número entre 0 e 20: '))
        if 0 <= escolha <= 20:
            break
        print('Tente novamente.', end='')
    print(f'Você digitou o número {numero[escolha]}')
    resp = str(input('Deseja continuar? [S/N] ')).upper()
