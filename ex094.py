pessoasdic = {}
pessoaslist = []
media = soma = 0
while True:
    pessoasdic['nome'] = str(input('Nome: '))
    while True:
        pessoasdic['sexo'] = str(input('Sexo: [F/M]')).upper()
        if pessoasdic['sexo'] not in ('F', 'M'):
            print('ERRO!Responda apenas com "F" ou "M".')
        else:
            break
    pessoasdic['idade'] = int(input('Idade: '))
    soma += pessoasdic['idade']
    pessoaslist.append(pessoasdic.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).upper()
        if continua not in ('S', 'N'):
            print('ERRO!Responda apenas com "S" ou "N".')
        else:
            break
    if continua == 'N':
        break
print(pessoaslist)
print(f'- O grupo tem {len(pessoaslist)} pessoas')
media = soma / len(pessoaslist)
print(f'- A média de idade é de {media:5.2f}')
print('As mulheres cadastradas foram: ')
for p in pessoaslist:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} \n', end='')
print(f'As pessoas que estão acima da média são: ')
for p in pessoaslist:
    if p['idade'] >= media:
        print('     ', end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>>>>>>> ENCERRADO <<<<<<<<')