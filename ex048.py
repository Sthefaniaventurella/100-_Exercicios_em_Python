s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print(f'A soma total de {cont} dos números ímpares que são múltiplos de 3 é {s}')
     