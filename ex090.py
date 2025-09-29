alunos = {}
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['status'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['status'] = 'Recuperação'
else:
    alunos['status'] = 'Reprovado'
print('-'*30)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')

