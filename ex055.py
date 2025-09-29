peso = float(input('Digite o peso em KG: '))
maior = peso
menor = peso
for c in range(2, 6):
    peso = float(input('Digite o peso em KG: '))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print(f'O maior peso foi {maior} KG')
print(f'O menor peso foi {menor} KG')
