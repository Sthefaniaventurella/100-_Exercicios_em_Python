lista = [[], [], []]
somap = maior = scol = 0
for c in range(0,3):
    for i in range(0,3):
        lista[c].append(int(input(f'Digite o valor da posição {c}, {i}: ')))
print('-=' * 20)
for c in range(0,3):
    for i in range(0,3):
        print(f'[{lista[c][i]:^5}]', end='')
        if lista[c][i] % 2 == 0:
            somap += lista[c][i]
        scol = lista[0][2] + lista[1][2] + lista[2][2]
    print()
print('-='*25)
print(f'A soma dos números pares é {somap}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {max(lista[1])}')

