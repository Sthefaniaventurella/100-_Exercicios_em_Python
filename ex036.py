print('=-='*12)
print('EMPRÉSTIMO BANCÁRIO')
print('=-='*12)
casa = float(input('Qual valor da casa a ser financiada? R$'))
salario = float(input('Qual valor do salário do comprador? R$'))
anos = int(input('Em quantos anos o comprador quer parcelar? '))
parcela = casa / (anos * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos ', end='')
print(f'a prestação será de R${parcela:.2f}')
if parcela >= (salario*30)/100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
