from datetime import date
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu: '))
    idade = date.today().year - ano
    if idade <= 20:
        menor += 1
    else:
        maior += 1
print(f'Número total de pessoas de maior idade: {maior} \n '
      f'Número total de pessoas de menor idade: {menor}')