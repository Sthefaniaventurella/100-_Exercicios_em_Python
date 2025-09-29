from datetime import datetime
ano_atual = datetime.now().year
registro = {}
registro['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = ano_atual - ano
registro['idade'] = idade
registro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if registro['CTPS'] != 0:
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = float(input('Salário: R$'))
    tempo_servico = ano_atual - registro['contratação']
    registro['aposentar'] = (35 - tempo_servico ) + idade
else:
    registro['aposentar'] = 'Não possui carteira assinada'
print('-=-'*30)
for k, v in registro.items():
    print(f'-{k} tem o valor {v}')


