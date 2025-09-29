lista= [[], []]  # lista_principal[0] para pares, lista_principal[1] para ímpares
for c in range(1, 8):
        num = int(input(f'Digite o {c}° valor: '))
        if num % 2 == 0:
            lista[0].append(num)  # Adiciona à sub-lista de pares
        else:  # num % 2 == 1 (ímpar)
            lista[1].append(num)  # Adiciona à sub-lista de ímpares
lista[0].sort()
lista[1].sort()
print(f"Números pares: {lista[0]}")
print(f"Números ímpares: {lista[1]}")

