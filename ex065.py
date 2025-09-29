resp = 'S'
soma = quant = maior = menor = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
média = soma / quant
print(f'Foram digitados {quant} números, totalizando {soma} e com média de {média}.')
print(f'O maior número digitado foi {maior}, e o menor número foi {menor}')


