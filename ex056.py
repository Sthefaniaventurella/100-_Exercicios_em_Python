somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20= 0
for c in range(1,5):
    print(f'----- {c}° PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'Ff' and idade < 20:
        mulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Nesse grupo existem {mulher20} com menos de 20 anos.')
