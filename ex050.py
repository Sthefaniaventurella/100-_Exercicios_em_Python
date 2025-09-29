s = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont += 1
        s += n
print(f'Você digitou {cont} números pares, a soma total é {s}')
