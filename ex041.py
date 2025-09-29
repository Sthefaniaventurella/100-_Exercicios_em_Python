from datetime import date
print('=='*18)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO \n CATEGORIAS')
print('=='*18)
ano = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - ano
if idade <= 9:
    print('Sua categoria é \033[34m MIRIM')
elif idade <= 14:
    print('Sua categoria é \033[34m INFANTIL')
elif idade <= 19:
    print('Sua categoria é \033[34m JUNIOR')
elif idade <= 25:
    print('Sua categoria é \033[34m SÊNIOR')
else:
    print('Sua categoria é \033[34m MASTER')

