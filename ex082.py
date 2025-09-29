lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resp = str(input('Deseja continuar? S/N: ')).upper()
    if resp == 'N':
        break
for i,v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-'*30)
print(f'A lista completa é: {lista}')
print(f'Lista par: {par}')
print(f'Lista ímpar: {impar}')



