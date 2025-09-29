mais18 = 0
tothomem = 0
mulhermenor = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ' )).upper().strip()[0]
    if sexo == 'M':
       tothomem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    print('-'*20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('========= FIM DO PROGRAMA =========')
print(f'Total de pessoas com mais de 18 anos: {mais18} \n '
      f'Ao todo temos {tothomem} homens cadastrados \n'
      f'E temos {mulhermenor} mulheres com menos de 20 anos.')
