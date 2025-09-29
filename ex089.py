alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno = [nome, nota1, nota2]
    alunos.append(aluno)
    resp = str(input('Deseja continuar? S/N: ')).upper()
    if resp == 'N':
        break
print('-' * 30)
print('        BOLETIM ESCOLAR     ')
print()
print(f'{'No.':<4} {'Nome':<15} {'Média':>6}')
print('-' * 30)
for c, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2]) / 2
    print(f'{c:<4} {aluno[0]:<15}{media:>6.2f}')
while True:
    indice = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if indice == 999:
        break
    else:
        print(f'As notas de {alunos[indice][0]} são: {alunos[indice][1]}, {alunos[indice][2]}')






