distancia = int(input('Qual será a distância da viagem em km? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
    print(f'O valor da passagem para {distancia}km é R${preço:.2f}')

