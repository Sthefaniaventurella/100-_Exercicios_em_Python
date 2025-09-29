numeros = []
for i in range(0,5):
    valor = int(input(f"Digite um valor: "))
    if i == 0 or valor > numeros[-1]:
        numeros.append(valor)
        print('Valor adicionado no final da lista!')
    else:
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                print(f'Adionado na posição {pos} da lsita...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {numeros}')

