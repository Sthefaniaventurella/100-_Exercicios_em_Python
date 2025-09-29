frase = str(input('Escreva uma frase: ').strip()).upper()
print(f'A letra A parece ', frase.count('A'), 'na frase')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}')



