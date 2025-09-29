print('='*30)
print('{:^30}'.format('TABELA DO BRASILEIRÃO'))
print('='*30)
times = ('','Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza','Internacional',
'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama',
'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá', '')
print('20 PRIMEIROS COLOCADOS: ')
for c in range(1,21):
    print(f'{c}° - {times[c]}')
print('-'*20)
print('5 PRIMEIROS COLOCADOS: ')
for c in range(1,6):
    print(f'{c}° - {times[c]}')
print('-'*20)
print('4 ÚLTIMOS COLOCADOS: ')
for c in range(17, 21):
    print(f'{c}° - {times[c]}')
print('-'*20)
times_ordenados = sorted(times[1:21])
print("TIMES EM ORDEM ALFABÉTICA:")
for time in times_ordenados:
    print(time)
print('-'*20)
seu_time = str(input('Qual time você quer ver a posição? ')).strip()
if seu_time in times:
    posicao = times.index(seu_time) + 1
    print(f'{seu_time} se encontra na {times.index(seu_time)}° posição')
else:
    print('Time não encontrado. Verifique se digitou corretamente. ')

