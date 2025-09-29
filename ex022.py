nome = str(input('Digite seu nome completo: ')).strip()
print('Tudo em maiúsculo: ', nome.upper())
print('Tudo em minúsculo: ', nome.lower())
print('Seu nome ao todo possui ',len(nome)-nome.count(' '),'letras')
#print('O primeiro nome possui', nome.find(' '), 'letras')
divide = nome.split()
print(f'Seu primeiro nome é {divide[0]} e ele possui {len(divide[0])} letras')



