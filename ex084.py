pessoas = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(dados) == 0:
        maiorpeso = menorpeso == dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? S/N: ')).upper()
    if resp == 'N':
        break
print('-='*20)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maiorpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menorpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end='')
print()
