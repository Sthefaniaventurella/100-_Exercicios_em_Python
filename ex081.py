resp = 'S'
lista = []
while resp == 'S':
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    resp = str(input('Deseja continuar? (S/N): ')).upper()
print('-='*25)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são:  {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O número 5 não está na lista.')
