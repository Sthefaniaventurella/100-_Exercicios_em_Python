while True:
    print('-'*30)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{tab} X {c} = {tab * c}')
print('PROGRAMA TABUADA ENCERADO! Volte sempre!')



