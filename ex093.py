jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas =  int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    total += gols[c]
    jogador['gols'] = gols
jogador['total'] = total
print('-=-'*25)
print(jogador)
print('-=-'*25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*25)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.' )
for k,v in enumerate(jogador['gols']):
    print(f'=> Na partida {k +1}, fez {v}')
print(f'Foi um total de {total} gols.')