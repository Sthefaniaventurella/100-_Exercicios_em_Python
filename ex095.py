jogador = {}
jogadores = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    gols = []

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols
    jogadores.append(jogador.copy())
    while True:
        resp  = str(input('Deseja continuar? [S/N] ')).upper()
        if resp not in ('S', 'N'):
            print('ERRO! Resposta inválida.')
        else:
            break
    if resp == 'N':
        break
    print('-' * 30)
print('=' * 30)
print('Cod.  Nome     Gols        Total')
for k, v in enumerate(jogadores):
    print(f'{k}  {v['nome']:^10} {v['gols']:^} {(sum(v['gols'])):^10}')
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if jog == 999:
        print('<<< VOLTE SEMPRE! >>>')
        break
    if jog < 0 or jog >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {jog}! Tente novamente.')
    else:
        print(f'-- LEVATAMENTO DO JOGADOR {jogadores[jog]['nome']}:')
        for k, v in enumerate(jogadores[jog]["gols"]):
            print(f'No jogo {k + 1} fez {v} gols')
