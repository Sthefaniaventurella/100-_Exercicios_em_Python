lista = [[], [], []]
for c in range(0,3):
    for i in range(0,3):
        lista[c].append(int(input(f'Digite o valor da posição {c}, {i}: ')))
print('-=' * 20)
for c in range(0,3):
    for i in range(0,3):
        print(f'[{lista[c][i]:^5}]', end='')
    print()
