sexo = str(input('Informe seu sexo: [F/M] ')).upper()[0].strip()
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
