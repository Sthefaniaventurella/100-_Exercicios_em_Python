def area(x,y):
    AreaTot = x * y
    print(f'A área de um terreno {x}x{y} é de {AreaTot}m²')

print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
