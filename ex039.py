from datetime import date
#ano = int(input('Em que ano você nasceu? '))
#idade = date.today().year - ano
#if idade < 18:
    #print(f'Falta {18-idade} anos para você se alistar no exército.')
#elif idade == 18:
    #print('Já está na hora de você se alistar no exército.')
#else:
    #print(f'Já passou do tempo do alistamento. Você está {idade-18} anos atrasado.')

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Voce não tem 18 anos. Ainda faltam {saldo} para o alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')
