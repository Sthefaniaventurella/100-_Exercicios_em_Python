numero = int(input('Digite um número para ver a tabuada: '))
print("=-="*5)
print(f'TABUADA {numero} ')
for c in range(0,11):
    print(f'{c} x {numero}: {c * numero}')
print('=-='*5)
